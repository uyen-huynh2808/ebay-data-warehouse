import os
import json
import pandas as pd
import re
import spacy
from google.cloud import storage, bigquery

# Paths to service account keys
CLOUD_STORAGE_KEY = "PATH_TO_CLOUD_STORAGE_KEY"
BIGQUERY_KEY = "PATH_TO_BIGQUEY_KEY"

# GCS Bucket & File Paths
BUCKET_NAME = "ebay-project-github"
FACT_FILE = "ebay/fact_laptop_listings_raw.json"
DIM_LAPTOPS_FILE = "ebay/dim_laptops_raw.json"
DIM_SELLERS_FILE = "ebay/dim_sellers_raw.json"
DIM_CONDITIONS_FILE = "ebay/dim_conditions_raw.json"

# BigQuery Dataset & Table Names
BQ_DATASET = "laptop_listings"
FACT_TABLE = "fact_laptop_listings"
DIM_LAPTOPS_TABLE = "dim_laptops"
DIM_SELLERS_TABLE = "dim_sellers"
DIM_CONDITIONS_TABLE = "dim_conditions"

# Function to download JSON file from Cloud Storage
def download_json_from_gcs(gcs_key, bucket_name, file_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcs_key  # Set key for Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()
    return json.loads(content)

# Function to clean and transform data
def clean_data(data, table_name):
    df = pd.DataFrame(data)

    df.dropna(inplace=True)  # Drop null values 

    df.drop_duplicates(inplace=True)  # Remove duplicates
    return df.to_dict(orient="records")

# Load NLP model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Function to transform data in dim_laptops table
def transform(data):
    df_laptops = pd.DataFrame(data)
    
    # Known brands
    KNOWN_BRANDS = {
        "Dell", "HP", "Lenovo", "Apple", "Acer", "Asus", "Microsoft", "Razer", "Compaq", "DynaBook",
        "MSI", "Samsung", "LG", "Toshiba", "Jumper", "SGIN", "CHUWI", "ThinkPad", "Intel", "Hyundai",
        "Inspiron", "Gateway", "Huawei", "Sony", "Vaio", "Xiaomi", "Google", "Alienware", "GPD", "Sharp",
        "Getac", "Vizio", "Panasonic", "Packard Bell", "Fujitsu", "MobileDemand", "iView", "Haier", "Bytespeed"
    }

    BRAND_ALIASES = {
        "Galaxy Book": "Samsung",
        "Macbook": "Apple",
        "Dell": "Latitude"
    }
    def extract_brand(title, brand_from_api=None):
        """Extracts laptop brand from API data, title keywords, or NLP if needed."""
        if brand_from_api and brand_from_api not in {"Unknown", ""}:  
            return brand_from_api.strip()

        # Check for known brands in the title
        for brand in KNOWN_BRANDS:
            if re.search(rf'\b{brand}\b', title, re.IGNORECASE):
                return brand

        # Alias Mapping
        for alias, brand in BRAND_ALIASES.items():
            if alias.lower() in title.lower():
                return brand
        
        # NLP model for additional brand detection
        doc = nlp(title)
        for ent in doc.ents:
            if ent.label_ == "ORG" and ent.text in KNOWN_BRANDS:
                return ent.text

        return "Unknown"  # Default if no brand found
    
    def extract_storage_type(title):
        """Identifies whether storage is SSD or HDD."""
        title_upper = title.upper()

        if "NO HDD" in title_upper and "SSD" in title_upper:
            return "SSD"
        elif "NO SSD" in title_upper and "HDD" in title_upper:
            return "HDD"
        elif "NO SSD" in title_upper or "NO HDD" in title_upper:
            return "Unknown"
        elif "HDD" in title_upper:
            return "HDD"
        elif "SSD" in title_upper:
            return "SSD"

        return "Unknown"
    
    def extract_storage_and_ram(title):
        """Extracts storage and RAM separately, ensuring storage is always larger than RAM."""
        storage_capacity, ram_size = "Unknown", "Unknown"
        tmp = -1  # Temporary variable to track RAM size

        # Find all GB/TB values (including variations like '16 GB', '8G', '1 T', etc.)
        matches = re.findall(r'\b(\d+)\s*(GB|TB|G|T)\b', title, re.IGNORECASE)

        if matches:
            values = []
            for size, unit in matches:
                size = int(size)
                unit = unit.upper().strip()

                # Standardize unit: Convert 'G' -> 'GB' and 'T' -> 'TB'
                unit = "GB" if unit in ["G", "GB"] else "TB"

                values.append((size, unit))

            values.sort()  # Sort ascending: smaller values first

            for size, unit in values:
                size_str = f"{size}{unit}"  # Convert back to GB/TB format

                # Assign RAM first if it's ≤ 64GB (RAM can't have TB)
                if ram_size == "Unknown" and size <= 64 and unit == "GB":
                    ram_size = size_str
                    tmp = size
                # Assign Storage if it's TB, ≥ 128GB, or larger than RAM
                elif storage_capacity == "Unknown" and (unit == "TB" or size > tmp):
                    storage_capacity = size_str
                # Ensure Storage is always larger than RAM
                elif storage_capacity == "Unknown" and unit == "GB" and size < tmp:
                    storage_capacity = ram_size
                    ram_size = size_str

            # If only one GB/TB value exists & storage type is known, assign it to storage
            if len(values) == 1 and extract_storage_type(title) != "Unknown":
                storage_capacity = f"{values[0][0]}{values[0][1]}"
                ram_size = "Unknown"

        return ram_size, storage_capacity
    
    # Apply extraction functions
    df_laptops["Brand"] = df_laptops.apply(lambda row: extract_brand(row["Title"], row.get("Brand", None)), axis=1)
    df_laptops["StorageType"] = df_laptops["Title"].apply(extract_storage_type)
    df_laptops["RamSize"], df_laptops["StorageCapacity"] = zip(*df_laptops["Title"].apply(extract_storage_and_ram))

    # Drop the original Title column
    df_laptops.drop(columns=["Title"], inplace=True)

    return df_laptops.to_dict(orient="records")  # FIX: Returning transformed data

# Function to upload JSON data to BigQuery
def load_json_to_bigquery(bq_key, dataset_id, table_id, data):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = bq_key  # Set key for BigQuery
    bigquery_client = bigquery.Client()
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    # Define schemas for each table
    TABLE_SCHEMAS = {
        "fact_laptop_listings": [
            bigquery.SchemaField("ListingID", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("SellerID", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("ConditionID", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("Price", "FLOAT", mode="REQUIRED"),
            bigquery.SchemaField("Currency", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("ShippingCost", "FLOAT", mode="REQUIRED"),
        ],
        "dim_laptops": [
            bigquery.SchemaField("LaptopID", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("Brand", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("RamSize", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("StorageType", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("StorageCapacity", "STRING", mode="REQUIRED"),
        ],
        "dim_sellers": [
            bigquery.SchemaField("SellerID", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("FeedbackScore", "FLOAT", mode="REQUIRED"),
        ],
        "dim_conditions": [
            bigquery.SchemaField("ConditionID", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("ConditionName", "STRING", mode="REQUIRED"),
        ]
    }

    if table_id not in TABLE_SCHEMAS:
        raise ValueError(f"Schema for table {table_id} is not defined!")

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=False,  # Disable schema auto-detection
        schema=TABLE_SCHEMAS[table_id]  # Assign correct schema
    )

    job = bigquery_client.load_table_from_json(data, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete
    print(f"Uploaded {len(data)} records to {dataset_id}.{table_id}")


# Main ETL process
def etl_process():
    print("Starting ETL process...")

    # Extract Data from Cloud Storage
    print("Extracting data from Cloud Storage...")
    fact_data = download_json_from_gcs(CLOUD_STORAGE_KEY, BUCKET_NAME, FACT_FILE)
    dim_laptops_data = download_json_from_gcs(CLOUD_STORAGE_KEY, BUCKET_NAME, DIM_LAPTOPS_FILE)
    dim_sellers_data = download_json_from_gcs(CLOUD_STORAGE_KEY, BUCKET_NAME, DIM_SELLERS_FILE)
    dim_conditions_data = download_json_from_gcs(CLOUD_STORAGE_KEY, BUCKET_NAME, DIM_CONDITIONS_FILE)
    
    # Transform dim_laptops
    dim_laptops_data = transform(dim_laptops_data)  # FIX: Assign transformed data

    # Clean Data
    print("Cleaning data...")
    fact_data = clean_data(fact_data, FACT_TABLE)
    dim_laptops_data = clean_data(dim_laptops_data, DIM_LAPTOPS_TABLE)
    dim_sellers_data = clean_data(dim_sellers_data, DIM_SELLERS_TABLE)
    dim_conditions_data = clean_data(dim_conditions_data, DIM_CONDITIONS_TABLE)
    
    # Load Data into BigQuery
    print("Loading data into BigQuery...")
    load_json_to_bigquery(BIGQUERY_KEY, BQ_DATASET, FACT_TABLE, fact_data)
    load_json_to_bigquery(BIGQUERY_KEY, BQ_DATASET, DIM_LAPTOPS_TABLE, dim_laptops_data)
    load_json_to_bigquery(BIGQUERY_KEY, BQ_DATASET, DIM_SELLERS_TABLE, dim_sellers_data)
    load_json_to_bigquery(BIGQUERY_KEY, BQ_DATASET, DIM_CONDITIONS_TABLE, dim_conditions_data)

    print("ETL process completed successfully!")

# Run ETL Process
if __name__ == "__main__":
    etl_process()