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


    ![architecture](https://private-user-images.githubusercontent.com/201462828/425805884-cad0fd0e-f014-41e2-969e-67be50d4931a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDI3MTYwMjYsIm5iZiI6MTc0MjcxNTcyNiwicGF0aCI6Ii8yMDE0NjI4MjgvNDI1ODA1ODg0LWNhZDBmZDBlLWYwMTQtNDFlMi05NjllLTY3YmU1MGQ0OTMxYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzIzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMyM1QwNzQyMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00YjZjMTJhYTZjOWYwYjg1MTRiM2Q5ODgyM2ZkOGUxNmNlZDU2MDY0MWNlZjU0Nzk1YmFiNzAzNjliNTc4MzE4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.GmMZlE2IrViySmX7GtrWDgjdUKt4TTAtO49LEaVKYvY)


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
  - Sale ID (Unique transaction identifier)
  - Seller ID & feedback score
  - Model name & specifications
  - Item condition (New/Refurbished)
  - Sale price & currency
  - Listing price (Before sale)

## Data Model
### **Fact Table**
##### `fact_laptop_sales`
Stores transaction-level details of laptop sales.
- `sale_id` (PK) – Unique identifier for the sale (from eBay).
- `seller_id` (FK) – Reference to the seller.
- `model_name` (FK) – Reference to the laptop model.
- `sale_price` – Final sale price of the laptop.
- `currency` – Currency of the sale.
- `listing_price` – Original listing price before sale.
- `item_condition` – Condition of the laptop (e.g., New, Refurbished).

### **Dimension Tables**
##### `dim_laptops`
Stores essential details about laptop models.
- `model_name` (PK) – Full model name with specifications.

##### `dim_sellers`
Stores seller-related information.
- `seller_id` (PK) – Unique identifier for the seller.
- `seller_feedback_score` – Seller's feedback score from customers.

(=================**ADD DIAGRAM**=================)

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
1. `scraper.py` – Scrape laptop sales data from eBay.
2. `load_to_gcs.py` – Upload raw data to Google Cloud Storage. 
3. `bigquery_schema.sql` – Define BigQuery table schema. 
4. `etl_pipeline.py` – Extract, transform, and load data using Mage. 
5. `dbt_models/` – dbt SQL models for data transformations. 
6. `airflow_dag.py` – Airflow DAG to automate the pipeline.
7. `dashboard_setup.lookml` – Configure Looker dashboard.

---
This EDW solution enables scalable and insightful **laptop sales analytics** using cloud-native technologies.
