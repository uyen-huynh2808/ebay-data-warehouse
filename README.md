# E-Commerce Sales Analytics Data Warehouse (eBay - BigQuery - Looker)

## Introduction
This project builds an **Enterprise Data Warehouse (EDW) for E-Commerce Sales Analytics**, leveraging cloud data warehousing, ETL, and BI tools to analyze sales performance, customer behavior, and product trends. The data is sourced from eBay using the **eBay API**, transformed using **dbt**, orchestrated with **Apache Airflow**, and visualized in **Looker Studio**. The solution is built on **Google BigQuery** but designed to be expandable to **AWS Redshift and Snowflake**.

## Architecture
### **1. Data Ingestion**
- Extract laptop sales data from **eBay API**.
- Store raw data in **Google Cloud Storage (GCS)**.

### **2. Data Processing & Transformation**
- Load raw data from GCS to **Google BigQuery**.
- Transform data using **dbt (Data Build Tool)**.

### **3. Orchestration & Scheduling**
- Automate workflows using **Apache Airflow**.

### **4. Business Intelligence (BI)**
- Build dashboards using **Looker Studio** to visualize laptop sales performance.

```
         +------------------+
         |  eBay API        |
         +--------+---------+
                  |
                  v
         +------------------+
         |  Google Cloud Storage |
         +--------+---------+
                  |
                  v
         +------------------+
         | Google BigQuery  |
         +--------+---------+
                  |
                  v
         +------------------+
         | dbt Transformation |
         +--------+---------+
                  |
                  v
         +------------------+
         | Looker Studio    |
         +------------------+
```
(ADD DIAGRAM)

## Technology Stack
| Component        | Technology Used |
|-----------------|----------------|
| Data Source     | **eBay API** |
| Data Storage    | **Google Cloud Storage (GCS)** |
| Data Warehouse  | **Google BigQuery** |
| ETL Processing  | **dbt (CLI version)** |
| Orchestration   | **Apache Airflow** |
| BI & Reporting  | **Looker Studio** |

## Dataset Used
- Data is collected from **eBay API**, specifically focusing on laptop sales, which includes:
  - Laptop brand (Dell, HP, Apple, etc.)
  - Model name and specifications (RAM, CPU, Storage, etc.)
  - Seller details
  - Price & currency
  - Listing status (Active/Sold)
  - Customer ratings & reviews
  - Item condition (New/Used)
  - Shipping details (Shipping cost, delivery time)
  
## Data Model
### **Fact Tables**
1. **fact_laptop_sales** (Stores transaction-level details)
   - sale_id (PK)
   - laptop_id (FK)
   - seller_id (FK)
   - sale_price
   - quantity_sold
   - sale_date

### **Dimension Tables**
2. **dim_laptops** (Stores laptop details)
   - laptop_id (PK)
   - brand
   - model_name
   - processor
   - ram_size
   - storage_capacity
   - gpu
   - screen_size
   - listing_price
   - item_condition

3. **dim_sellers** (Stores seller details)
   - seller_id (PK)
   - seller_name
   - seller_location
   - rating
   - seller_feedback_score

4. **dim_dates** (Stores date attributes for analysis)
   - date_id (PK)
   - full_date
   - day
   - month
   - year

(ADD DIAGRAM)

## Setup Instructions
1. **Set up Google Cloud Platform (GCP)** and enable **BigQuery**.
2. **Obtain eBay API Credentials** from [eBay Developer Portal](https://developer.ebay.com/).
3. **Install required tools:**
   ```sh
   pip install apache-airflow dbt-bigquery google-cloud-storage requests pandas
   ```
4. **Run the pipeline:**
   - **Extract Data:** Use Python to pull laptop sales data from eBay API.
   - **Load Data:** Store raw JSON in Google Cloud Storage (GCS).
   - **Transform Data:** Use dbt to clean and structure the data.
   - **Visualize:** Create dashboards in Looker Studio.

## Future Enhancements
- Expand to **AWS Redshift & Snowflake** for multi-cloud compatibility.
- Implement **real-time data streaming** using Kafka or Pub/Sub.
- Improve **pricing trend analysis** for laptops.
- Enhance product insights using **sentiment analysis on customer reviews**.
- Automate **data quality checks** using Great Expectations.

## Scripts for project
1. scraper.py – Scrape laptop sales data from eBay.
2. data_cleaning.py – Clean and transform scraped data.
3. load_to_gcs.py – Upload raw data to Google Cloud Storage.
4. etl_pipeline.py – Extract, transform, and load data using Mage.
5. dbt_models/ (Folder) – dbt SQL models for data transformations.
6. bigquery_schema.sql – Define BigQuery table schema.
7. dashboard_setup.lookml – Configure Looker dashboard.
8. airflow_dag.py – Airflow DAG to automate the pipeline.

---
This EDW solution enables scalable and insightful **laptop sales analytics** using cloud-native technologies.
