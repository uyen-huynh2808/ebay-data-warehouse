# E-Commerce Laptop Listings Analytics Data Warehouse (eBay - BigQuery - Looker)

## Introduction
This project builds an **Enterprise Data Warehouse (EDW) for E-Commerce Laptop Listings Analytics**, leveraging cloud data warehousing, ETL, and BI tools to analyze **seller performance, competition, and price trends**. The data is sourced from **eBay API**, transformed using **dbt**, and visualized in **Looker Studio**. The solution is built on **Google BigQuery**.

## Project Goals
1. **Seller Performance & Competition**
   - Identify top-performing laptop sellers based on metrics such as listing volume, and feedback score.
   - Explore the **concentration of seller tiers**: New Sellers, Rising Sellers, and Top Sellers. New Sellers contribute the most listings, but Top Sellers might offer higher-quality products despite having fewer listings.
   
2. **Price Trends & Competitor Pricing**
   - Track **price variations** for laptop models across different sellers.
   - Analyze pricing strategies based on **condition** (New, Used, Refurbished), including price averages, min/max ranges, and tendency.
   - Compare **pricing patterns** across different seller tiers and identify opportunities for competitive pricing.

## Architecture
### **1. Data Ingestion**
- Extract **laptop listings data** from **eBay API**.
- Store raw JSON data in **Google Cloud Storage (GCS)**.

### **2. Data Processing & Transformation**
- Load data from GCS into **Google BigQuery**.
- Transform and structure data using **dbt (Data Build Tool)**.

### **3. Business Intelligence (BI)**
- Insights such as **listing counts by seller tier**, **average prices by seller tier and condition**, and **price tendencies (Spike, Stable, Drop)** are visualized for deeper analysis.

![architecture](https://github.com/user-attachments/assets/97f4f182-6190-4fa4-a417-1c697f8a47ad)

## Technology Stack
| Component        | Technology Used |
|-----------------|----------------|
| Data Source     | **eBay API** |
| Data Storage    | **Google Cloud Storage (GCS)** |
| Data Warehouse  | **Google BigQuery** |
| ETL Processing  | **dbt (IDE version)** |
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
   - price
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
   - feedback_score
   
4. **dim_conditions** (Stores item condition details)
   - condition_id (PK)
   - condition_name (New, Used, Refurbished, ...)

![dbdiagram](https://private-user-images.githubusercontent.com/201462828/430765383-cdd34865-1a80-4495-a71a-77b8a2be1b9f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTI1NzIsIm5iZiI6MTc0Mzk5MjI3MiwicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY1MzgzLWNkZDM0ODY1LTFhODAtNDQ5NS1hNzFhLTc3YjhhMmJlMWI5Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjE3NTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZjIwNzg4YmY2OWNjZGU0Njg2YmUzNWZlMDE4ZGZlYjBiNjRiNzI3NmU5NGI5NTlmYjdiYmNkMDkxMzBjMWIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.U_LdXMjpXJUCg9LsJ8eJoVj-z54wejwMcLRwjvGPkog)

## Project Files
1. `scraper.py` – Scrapes laptop listings from eBay.
2. `load_to_gcs.py` – Uploads raw data to Google Cloud Storage.
3. `bigquery_schema.sql` – Defines BigQuery table schema.
4. `etl_pipeline.py` – Extracts data from Google Cloud Storage, transforms and loads it into BigQuery.
5. `models/` – dbt SQL models for data transformations.
6. `visualization_insight.md` – Document outlining the visualizations and insights for Looker Studio.

---
