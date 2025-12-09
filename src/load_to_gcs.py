from google.cloud import storage
import os

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

# Path to the Google Cloud Service Account JSON key
# Ensure this file is added to .gitignore to prevent exposure
SERVICE_ACCOUNT_FILE = "credentials/google_credentials.json" 

# Target Google Cloud Storage Bucket Name
BUCKET_NAME = "ebay-project-github" 

# Source file path (Output from scraper.py)
SOURCE_FILE_PATH = "data/raw_ebay_data.csv"

# Destination path within the GCS bucket (Key name)
# Storing in a 'raw' directory is best practice for ELT pipelines
DESTINATION_BLOB_NAME = "raw_data/ebay_laptop_listings.csv"

# -----------------------------------------------------------------------------
# Upload Function
# -----------------------------------------------------------------------------

def upload_to_gcs():
    """
    Uploads the raw CSV data file to Google Cloud Storage.
    Authentication is handled via the Service Account JSON key.
    """
    # 1. Validate source file existence
    if not os.path.exists(SOURCE_FILE_PATH):
        print(f"Error: Source file not found at '{SOURCE_FILE_PATH}'.")
        print("Please run the scraper script first to generate the data.")
        return

    try:
        print(f"Initializing upload for: {SOURCE_FILE_PATH}")

        # 2. Authenticate and Initialize Client
        client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(DESTINATION_BLOB_NAME)

        # 3. Upload File
        # usage of upload_from_filename handles opening/closing the file automatically
        blob.upload_from_filename(SOURCE_FILE_PATH)

        print(f"Success: File uploaded to gs://{BUCKET_NAME}/{DESTINATION_BLOB_NAME}")

    except Exception as e:
        print(f"An error occurred during GCS upload: {str(e)}")

if __name__ == "__main__":
    upload_to_gcs()