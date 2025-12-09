import requests
import json
import os
import pandas as pd

# -----------------------------------------------------------------------------
# Configuration & Constants
# -----------------------------------------------------------------------------

# eBay API credentials (Placeholder)
EBAY_APP_TOKEN = "YOUR_APP_TOKEN" 

# API Endpoints and Parameters
API_ENDPOINT = "https://api.ebay.com/buy/browse/v1/item_summary/search"
SEARCH_QUERY = "laptop"
MAX_RESULTS = 7000
ENTRIES_PER_PAGE = 200

# Headers for authentication and marketplace selection
HEADERS = {
    "Authorization": f"Bearer {EBAY_APP_TOKEN}",
    "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
    "Content-Type": "application/json"
}

# List of keywords to exclude non-laptop items (accessories, parts, etc.)
EXCLUDED_KEYWORDS = ["tablet", "webcam", "dock", "monitor", "screen", "adapter", "case", "charger"]

# Output configuration
OUTPUT_DIR = "data"
OUTPUT_FILE = "raw_ebay_data.csv"

# -----------------------------------------------------------------------------
# Data Extraction Functions
# -----------------------------------------------------------------------------

def fetch_ebay_data(query, max_items, per_page):
    """
    Fetches item summaries from the eBay Browse API with pagination.
    
    Args:
        query (str): The search keyword.
        max_items (int): The maximum number of items to retrieve.
        per_page (int): Number of items per API call (limit).

    Returns:
        list: A list of item dictionaries returned by the API.
    """
    all_items = []
    offset = 0  

    while len(all_items) < max_items:
        params = {
            "q": query,
            "limit": per_page,
            "offset": offset,
            # Filter for fixed price items in the Laptops & Netbooks category
            "filter": "buyingOptions:{FIXED_PRICE}, categoryIds:{175672}"
        }

        try:
            response = requests.get(API_ENDPOINT, headers=HEADERS, params=params)
            
            if response.status_code == 200:
                data = response.json()
                if "itemSummaries" in data:
                    items = data["itemSummaries"]
                    all_items.extend(items)
                    print(f"Fetched {len(items)} items. Total: {len(all_items)}")
                else:
                    print("No more items found in response.")
                    break
            else:
                print(f"Error fetching data: Status {response.status_code} - {response.text}")
                break

        except Exception as e:
            print(f"Exception occurred during API request: {str(e)}")
            break

        offset += per_page  

    return all_items[:max_items]

# -----------------------------------------------------------------------------
# Main Execution Flow
# -----------------------------------------------------------------------------

def main():
    print("Starting data extraction process...")
    
    # 1. Fetch raw data from API
    raw_items = fetch_ebay_data(SEARCH_QUERY, MAX_RESULTS, ENTRIES_PER_PAGE)
    
    if not raw_items:
        print("No data fetched. Exiting.")
        return

    print(f"Processing {len(raw_items)} raw items...")
    
    processed_records = []

    # 2. Process and Flatten Data
    for item in raw_items:
        # Filter out unwanted items based on title keywords
        title = item.get("title", "")
        if any(keyword in title.lower() for keyword in EXCLUDED_KEYWORDS):
            continue 

        # Extract Price
        price_obj = item.get("price", {})
        price_value = float(price_obj.get("value", 0.0))
        currency = price_obj.get("currency", "USD")

        # Extract Seller Info
        seller_obj = item.get("seller", {})
        seller_username = seller_obj.get("username", "Unknown")
        seller_feedback = float(seller_obj.get("feedbackPercentage", 0.0))

        # Extract Shipping Cost
        # Handle nested structure for shipping options
        shipping_options = item.get("shippingOptions", [])
        shipping_cost = 0.0
        if shipping_options:
            cost_obj = shipping_options[0].get("shippingCost", {})
            shipping_cost = float(cost_obj.get("value", 0.0))

        # Flatten the record into a single dictionary
        record = {
            "listing_id": item.get("itemId"),
            "title": title,
            "price": price_value,
            "currency": currency,
            "condition_id": item.get("conditionId", "Unknown"),
            "condition_name": item.get("condition", "Unknown"),
            "seller_username": seller_username,
            "seller_feedback_score": seller_feedback,
            "shipping_cost": shipping_cost,
            "item_url": item.get("itemWebUrl", "")
        }
        
        processed_records.append(record)

    # 3. Save Data to CSV
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    # Convert to DataFrame and save
    df = pd.DataFrame(processed_records)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    
    df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Data extraction complete.")
    print(f"Total records saved: {len(processed_records)}")
    print(f"File saved to: {output_path}")

if __name__ == "__main__":
    main()