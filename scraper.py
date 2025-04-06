import requests
import json
import os

# eBay API credentials
EBAY_APP_TOKEN = "YOUR_APP_TOKEN"  # Replace with your actual OAuth token

# eBay Browse API Endpoint
API_ENDPOINT = "https://api.ebay.com/buy/browse/v1/item_summary/search"

# Search parameters
search_query = "laptop"
max_results = 7000
entries_per_page = 200

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {EBAY_APP_TOKEN}",
    "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
    "Content-Type": "application/json"
}

def fetch_ebay_data(query, max_items, per_page):
    all_items = []
    offset = 0  

    while len(all_items) < max_items:
        params = {
            "q": query,
            "limit": per_page,
            "offset": offset,
            "filter": "buyingOptions:{FIXED_PRICE}, categoryIds:{175672}"
        }

        response = requests.get(API_ENDPOINT, headers=HEADERS, params=params)

        if response.status_code == 200:
            data = response.json()
            if "itemSummaries" in data:
                all_items.extend(data["itemSummaries"])
            else:
                print("No more items found.")
                break
        else:
            print(f"Error fetching data: {response.status_code}, {response.text}")
            break

        offset += per_page  

    return all_items[:max_items] 

# Fetch data
items = fetch_ebay_data(search_query, max_results, entries_per_page)

# Normalized tables
fact_laptop_listings = []
dim_laptops = []
dim_sellers = {}
dim_conditions = {}

excluded_keywords = ["tablet", "webcam", "dock", "monitor", "screen", "adapter"]

# Process data into schema
for item in items:
    
    title_check = item["title"].lower()
    if any(keyword in title_check for keyword in excluded_keywords):
        continue  # Skip items that match unwanted keywords
    
    listing_id = item["itemId"]
    title = item["title"]
    price = float(item["price"]["value"])
    currency = item["price"]["currency"]
    seller_name = item["seller"]["username"]
    condition_id = item["conditionId"] if "conditionId" in item else "Unknown"
    shipping_id = listing_id  
    
    shipping_info = item.get("shippingOptions", [])
    if shipping_info:  # Check if there is any shipping information
        shipping_info = shipping_info[0]  # Get the first shipping option
        shipping_cost = float(shipping_info.get("shippingCost", {}).get("value", 0.0))
    else:
        shipping_cost = 0.0  # Default to 0.0 if no shipping options are found    

    # Add fact table entry
    fact_laptop_listings.append({
        "ListingID": listing_id,
        "SellerID": seller_name,
        "ConditionID": condition_id,
        "Price": price,
        "Currency": currency,
        "ShippingCost": shipping_cost,
    })

    # Add seller details
    dim_sellers[seller_name] = {
        "SellerID": seller_name,
        "FeedbackScore": item["seller"].get("feedbackPercentage", 0),
    }

    # Add condition details
    if condition_id not in dim_conditions:
        dim_conditions[condition_id] = {
            "ConditionID": condition_id,
            "ConditionName": item.get("condition", "Unknown")
        }

    # Add item details
    dim_laptops.append({
        "LaptopID": listing_id,
        "Title": title
    })   

# Function to save data as JSON
def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(list(data.values()) if isinstance(data, dict) else data, file, indent=4)

# Save tables
save_to_json(fact_laptop_listings, "PATH_TO_fact_laptop_listings_raw.json")
save_to_json(dim_sellers, "PATH_TO_dim_sellers_raw.json")
save_to_json(dim_conditions, "PATH_TO_dim_conditions_raw.json")
save_to_json(dim_laptops, "PATH_TO_dim_laptops_raw.json")

print("Data extraction and normalization complete. JSON files saved.")