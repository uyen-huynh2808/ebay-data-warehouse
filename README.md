# E-Commerce Sales Analytics Data Warehouse (eBay - BigQuery - Looker)

## Introduction
This project builds an **Enterprise Data Warehouse (EDW) for E-Commerce Sales Analytics**, leveraging cloud data warehousing, ETL, and BI tools to analyze sales performance, customer behavior, and product trends. The data is sourced from eBay using the **eBay API**, transformed using **dbt**, orchestrated with **Apache Airflow**, and visualized in **Looker Studio**. The solution is built on **Google BigQuery** but designed to be expandable to **AWS Redshift and Snowflake**.

## Architecture
### **1. Data Ingestion**
- Extract product sales data from **eBay API**.
- Store raw data in **Google Cloud Storage (GCS)**.

### **2. Data Processing & Transformation**
- Load raw data from GCS to **Google BigQuery**.
- Transform data using **dbt (Data Build Tool)**.

### **3. Orchestration & Scheduling**
- Automate workflows using **Apache Airflow**.

### **4. Business Intelligence (BI)**
- Build dashboards using **Looker Studio** to visualize sales performance.

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
- Data is collected from **eBay API**, which provides information on:
  - Product name
  - Category
  - Seller details
  - Price & currency
  - Listing status (Active/Sold)
  - Customer ratings & reviews
  
## Data Model
### **Fact Tables**
1. **fact_sales** (Stores transaction-level details)
   - sale_id (PK)
   - product_id (FK)
   - seller_id (FK)
   - sale_price
   - quantity_sold
   - sale_date

### **Dimension Tables**
2. **dim_products** (Stores product details)
   - product_id (PK)
   - product_name
   - category
   - brand
   - listing_price

3. **dim_sellers** (Stores seller details)
   - seller_id (PK)
   - seller_name
   - seller_location
   - rating

4. **dim_dates** (Stores date attributes for analysis)
   - date_id (PK)
   - full_date
   - day
   - month
   - year

## Setup Instructions
1. **Set up Google Cloud Platform (GCP)** and enable **BigQuery**.
2. **Obtain eBay API Credentials** from [eBay Developer Portal](https://developer.ebay.com/).
3. **Install required tools:**
   ```sh
   pip install apache-airflow dbt-bigquery google-cloud-storage requests pandas
   ```
4. **Run the pipeline:**
   - **Extract Data:** Use Python to pull data from eBay API.
   - **Load Data:** Store raw JSON in Google Cloud Storage (GCS).
   - **Transform Data:** Use dbt to clean and structure the data.
   - **Visualize:** Create dashboards in Looker Studio.

## Future Enhancements
- Expand to **AWS Redshift & Snowflake** for multi-cloud compatibility.
- Implement **real-time data streaming** using Kafka or Pub/Sub.

---
This EDW solution enables scalable and insightful e-commerce sales analytics using cloud-native technologies.
