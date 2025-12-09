# E-Commerce Laptop Listings Analytics Data Warehouse (eBay - BigQuery - dbt - Looker)

## Introduction
This project builds an **Enterprise Data Warehouse (EDW) for E-Commerce Laptop Listings Analytics**, leveraging cloud data warehousing, ETL, and BI tools to analyze **seller performance, competition, and price trends**. The data is sourced from **eBay API**, transformed using **dbt**, and visualized in **Looker Studio**. The solution is built on **Google BigQuery**.

## Project Goals
### 1. **Seller Performance & Competition**
- Identify top-performing laptop sellers based on metrics such as listing volume, and feedback score.
- Analyze the **distribution of seller tiers**: *New Sellers*, *Rising Sellers*, and *Top Sellers*.
    - **New Sellers** contribute the highest total listings, likely due to their large numbers.
    - **Top Sellers**, while fewer, may offer **higher-quality listings** and demonstrate **greater efficiency per seller**.
   
### 2. **Price Trends & Competitor Pricing**
- Track **price variations** for laptop models across different sellers.
- Analyze pricing strategies based on **condition** (New, Used, Refurbished), including price averages, min/max ranges, and tendency.
- Compare **pricing patterns** across different seller tiers and identify opportunities for competitive pricing.

## Architecture
### **1. Data Ingestion (EL)**
- **Extraction:** Python scripts (`src/scraper.py`) query the **eBay API** to retrieve laptop listings, flattening the JSON response into a raw CSV format to preserve data fidelity.
- **Loading:** The raw data is uploaded to **Google Cloud Storage (GCS)** and immediately loaded into **Google BigQuery** as a raw staging table (`raw_ebay.laptop_listings`).

### **2. Data Transformation (T)**
- **dbt (Data Build Tool)** is used for the entire transformation layer inside BigQuery:
    - **Staging Layer:** Cleans raw data, standardizes naming conventions, and extracts features (e.g., parsing RAM and Storage from titles using Regex).
    - **Intermediate Layer:** Aggregates data to calculate complex metrics such as **Seller Tiers** and **Price Trends**.
    - **Marts Layer:** Produces the final Star Schema (Fact/Dimensions) for reporting.

### **3. Business Intelligence (BI)**
- Insights such as **listing counts by seller tier**, **average prices by seller tier and condition**, and **price tendencies (Spike, Stable, Drop)** are visualized for deeper analysis in Looker Studio.

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

![dbdiagram](https://github.com/user-attachments/assets/cdd34865-1a80-4495-a71a-77b8a2be1b9f)

## Project Files
## Project Structure
```text
├── data/                       # Sample raw data for testing
├── dbt_project/                # dbt project directory (Transformation Logic)
│   ├── dbt_project.yml         # dbt configuration
│   ├── models/                 
│   │   ├── staging/            # Cleaning and feature extraction
│   │   ├── intermediate/       # Business logic and aggregations
│   │   └── marts/              # Final Star Schema (Core & Analytics)
├── src/                        # Python scripts (Ingestion Logic)
│   ├── scraper.py              # Extracts data from eBay API to CSV
│   ├── load_to_gcs.py          # Uploads raw files to GCS
│   └── ingestion.py            # Loads data from GCS to BigQuery Raw
├── visualization_dashboard/    # BI assets
└── requirements.txt            # Python dependencies
```

## Limitations

- Limited Historical Depth: The eBay API only provides recent listing data, making long-term trend analysis challenging without continuous data collection over time.
- Sampling Bias: Data collected may not fully represent all laptop listings due to rate limits and API pagination constraints.
- Static Seller Tier Classification: Current seller tier segmentation is based on snapshot metrics (e.g., feedback score), which may not reflect ongoing seller performance changes.
- No Real-Time Pipeline: The ETL process is batch-based; real-time monitoring of listing or pricing dynamics is not currently supported.

## Future Developments

- Incremental Loading with Change Data Capture (CDC): Implement CDC logic in dbt to support incremental transformations and reduce processing time.
- Historical Snapshot Layer: Create a time-partitioned snapshot table in BigQuery to capture listing state over time for robust trend and survival analysis.
- Enhanced Seller Profiling: Integrate additional seller metadata (e.g., shipping speed, return policy) to enrich seller segmentation.
- Real-Time Dashboard: Integrate Dataflow or Pub/Sub to enable streaming ingestion and near real-time dashboard updates.
- Automated Reporting: Set up scheduled Looker Studio reports or Slack alerts for sudden pricing changes or top seller activity spikes.

## Conclusion

- Demonstrated the development of an end-to-end cloud-based data warehouse solution tailored for e-commerce analytics.
- Successfully integrated eBay API, Google Cloud Storage, BigQuery, dbt, and Looker Studio to deliver actionable insights on seller behavior and pricing dynamics.
- Enabled strategic decision-making through interactive dashboards on seller segmentation, pricing trends, and competitive positioning.
- This project highlights core data engineering competencies, from data ingestion and modeling to transformation, visualization, and business impact.
- **For detailed results and data-driven insights, please refer to `visualization_insights.md`.**
---
