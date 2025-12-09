import os
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

# Service Account Key Path
# Ensure this file is added to .gitignore
KEY_FILE_PATH = "credentials/google_credentials.json"

# Google Cloud Resources
PROJECT_ID = "your-gcp-project-id"  # Update with your actual Project ID
BUCKET_NAME = "ebay-project-github"
SOURCE_FILE_PATH = "raw_data/ebay_laptop_listings.csv" # Path inside GCS Bucket

# BigQuery Configuration
BQ_DATASET_ID = "raw_ebay"          # Dataset for raw data
BQ_TABLE_ID = "laptop_listings"     # Raw table name

# -----------------------------------------------------------------------------
# BigQuery Schema Definition
# -----------------------------------------------------------------------------

# Strictly defined schema to match the CSV output from scraper.py
RAW_SCHEMA = [
    bigquery.SchemaField("listing_id", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("price", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("currency", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("condition_id", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("condition_name", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("seller_username", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("seller_feedback_score", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("shipping_cost", "FLOAT", mode="NULLABLE"),
    bigquery.SchemaField("item_url", "STRING", mode="NULLABLE"),
]

# -----------------------------------------------------------------------------
# Ingestion Logic
# -----------------------------------------------------------------------------

def create_dataset_if_not_exists(client, dataset_id):
    """
    Checks if the dataset exists in BigQuery, creates it if not.
    """
    dataset_ref = f"{client.project}.{dataset_id}"
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset '{dataset_id}' already exists.")
    except NotFound:
        print(f"Dataset '{dataset_id}' not found. Creating...")
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"  # Match GCS bucket location
        client.create_dataset(dataset)
        print(f"Created dataset '{dataset_id}'.")

def load_gcs_to_bigquery():
    """
    Loads data directly from GCS to BigQuery without local download.
    Follows ELT pattern: Load Raw first, Transform later.
    """
    # Authenticate
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_FILE_PATH
    client = bigquery.Client()

    # Ensure dataset exists
    create_dataset_if_not_exists(client, BQ_DATASET_ID)

    # Configure the Load Job
    table_ref = f"{client.project}.{BQ_DATASET_ID}.{BQ_TABLE_ID}"
    uri = f"gs://{BUCKET_NAME}/{SOURCE_FILE_PATH}"

    job_config = bigquery.LoadJobConfig(
        schema=RAW_SCHEMA,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,       # Skip the CSV header row
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE, # Overwrite table on each run
        field_delimiter=",",
        quote_character='"',
        allow_quoted_newlines=True # Handle descriptions with newlines if any
    )

    print(f"Starting import from {uri} to {table_ref}...")

    try:
        load_job = client.load_table_from_uri(
            uri,
            table_ref,
            job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()

        # Retrieve and print job statistics
        destination_table = client.get_table(table_ref)
        print(f"Job Finished. Loaded {destination_table.num_rows} rows to table '{BQ_TABLE_ID}'.")

    except Exception as e:
        print(f"BigQuery Load Job Failed: {str(e)}")
        # Check for error details if available
        if hasattr(e, 'errors'):
            print(f"Detailed Errors: {e.errors}")

if __name__ == "__main__":
    load_gcs_to_bigquery()