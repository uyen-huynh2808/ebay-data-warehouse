from google.cloud import storage
import os

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = "PATH_TO_KEY"  # Update this to your actual file path

# Your GCS bucket
BUCKET_NAME = "ebay-project-github"  # Replace with your actual bucket name

# Local JSON files to upload (fact & dimension tables)
FILES_TO_UPLOAD = {
    "ebay/fact_laptop_listings_raw.json": "PATH_TO_fact_laptop_listings_raw.json",
    "ebay/dim_sellers_raw.json": "PATH_TO_dim_sellers_raw.json",
    "ebay/dim_conditions_raw.json": "PATH_TO_dim_conditions_raw.json",
    "ebay/dim_laptops_raw.json": "PATH_TO_dim_laptops_raw.json"
}

def upload_to_gcs():
    try:
        # Authenticate using the service account JSON key
        client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
        bucket = client.bucket(BUCKET_NAME)

        for destination_blob_name, local_file_path in FILES_TO_UPLOAD.items():
            if not os.path.exists(local_file_path):
                print(f"File not found: {local_file_path}, skipping...")
                continue

            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(local_file_path)
            print(f"Uploaded {local_file_path} to gs://{BUCKET_NAME}/{destination_blob_name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    upload_to_gcs()
