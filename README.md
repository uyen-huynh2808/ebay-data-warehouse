# E-Commerce Laptop Listings Analytics Data Warehouse (eBay - BigQuery - Looker)

## Introduction
This project builds an **Enterprise Data Warehouse (EDW) for E-Commerce Laptop Listings Analytics**, leveraging cloud data warehousing, ETL, and BI tools to analyze **seller performance, competition, and price trends**. The data is sourced from **eBay API**, transformed using **dbt**, and visualized in **Looker Studio**. The solution is built on **Google BigQuery** but designed to be expandable to **AWS Redshift and Snowflake**.

## Project Goals
1. **Seller Performance & Competition**
   - Identify top-performing laptop sellers based on listing metrics.
   - Compare sellers based on listing volume, pricing, and feedback score.
   
2. **Price Trends & Competitor Pricing**
   - Track price variations for laptop models across different sellers.
   - Analyze pricing strategies by condition (New, Used, Refurbished).
   - Monitor trends for popular laptop brands and specifications.

## Architecture
### **1. Data Ingestion**
- Extract **laptop listings data** from **eBay API**.
- Store raw JSON data in **Google Cloud Storage (GCS)**.

### **2. Data Processing & Transformation**
- Load raw data from GCS into **Google BigQuery**.
- Transform and structure data using **dbt (Data Build Tool)**.

### **3. Business Intelligence (BI)**
- Build dashboards in **Looker Studio** to track seller performance and pricing trends.

![architecture](https://github.com/user-attachments/assets/97f4f182-6190-4fa4-a417-1c697f8a47ad)

## Technology Stack
| Component        | Technology Used |
|-----------------|----------------|
| Data Source     | **eBay API** |
| Data Storage    | **Google Cloud Storage (GCS)** |
| Data Warehouse  | **Google BigQuery** |
| ETL Processing  | **dbt (CLI version)** |
| BI & Reporting  | **Looker Studio** |

## Dataset Used
Data is collected from **eBay API**, specifically focusing on **laptop listings**, which includes:
  - Laptop brand, and specifications (RAM, Storage, etc.)
  - Seller details (Username, feedback score)
  - Listing price & currency
  - Item condition (New, Used, Refurbished)
  - Shipping cost

## Data Model
### **Fact Table**
1. **fact_laptop_listings** (Stores listing-level details)
   - listing_id (PK) (FK)
   - seller_id (FK)
   - condition_id (FK)
   - listing_price
   - currency
   - shipping_cost

### **Dimension Tables**
2. **dim_laptops** (Stores laptop details)
   - laptop_id (PK)
   - brand
   - ram_size
   - storage_type
   - storage_capacity

3. **dim_sellers** (Stores seller details)
   - seller_id (PK)
   - seller_feedback_score
   
4. **dim_conditions** (Stores item condition details)
   - condition_id (PK)
   - condition_name (New, Used, Refurbished, ...)

![dbdiagram](https://github.com/user-attachments/assets/079627ad-5c46-451a-beef-8d11b32aa49f)

## Future Enhancements
- Expand to **AWS Redshift & Snowflake** for multi-cloud compatibility.
- Enhance **competitor pricing analysis** using ML models.
- Implement **real-time listing monitoring** with streaming data pipelines.
- Include **customer sentiment analysis** from product reviews.

## Project Files
1. `scraper.py` – Scrape laptop listings from eBay.
2. `load_to_gcs.py` – Upload raw data to Google Cloud Storage.
3. `bigquery_schema.sql` – Define BigQuery table schema.
4. `etl_pipeline.py` – Extracts data from Google Cloud Storage, transforms and loads it into BigQuery.
5. `dbt_models/` – dbt SQL models for data transformations.
6. `dashboard_setup.lookml` – Configure Looker dashboard.

---
