/*
    Staging Model: stg_ebay_listings
    Description: 
        This model cleans, deduplicates, and standardizes raw laptop listing data.
        It performs feature extraction from unstructured titles (Brand, RAM, Storage)
        and normalizes currency/pricing fields.
*/

WITH raw_source AS (
    SELECT 
        listing_id,
        title,
        price,
        currency,
        condition_id,
        condition_name,
        seller_username,
        seller_feedback_score,
        shipping_cost
    FROM {{ source('ebay_source', 'laptop_listings') }}
    WHERE listing_id IS NOT NULL 
),

-- Deduplicate listings to ensure primary key uniqueness
deduplicated AS (
    SELECT *
    FROM raw_source
    QUALIFY ROW_NUMBER() OVER (PARTITION BY listing_id ORDER BY listing_id) = 1
),

-- Extract unstructured features from the listing title using Regex
extracted_features AS (
    SELECT 
        *,
        -- 1. Brand Extraction Logic
        -- Prioritizes specific aliases before matching against a standard list of manufacturers.
        CASE 
            WHEN REGEXP_CONTAINS(title, r'(?i)Galaxy Book') THEN 'Samsung'
            WHEN REGEXP_CONTAINS(title, r'(?i)Macbook') THEN 'Apple'
            WHEN REGEXP_CONTAINS(title, r'(?i)Latitude') THEN 'Dell'
            WHEN REGEXP_CONTAINS(title, r'(?i)\b(Dell|HP|Lenovo|Apple|Acer|Asus|Microsoft|Razer|Compaq|DynaBook|MSI|Samsung|LG|Toshiba|Jumper|SGIN|CHUWI|ThinkPad|Intel|Hyundai|Inspiron|Gateway|Huawei|Sony|Vaio|Xiaomi|Google|Alienware|GPD|Sharp|Getac|Vizio|Panasonic|Packard Bell|Fujitsu|MobileDemand|iView|Haier|Bytespeed)\b') 
                THEN REGEXP_EXTRACT(title, r'(?i)\b(Dell|HP|Lenovo|Apple|Acer|Asus|Microsoft|Razer|Compaq|DynaBook|MSI|Samsung|LG|Toshiba|Jumper|SGIN|CHUWI|ThinkPad|Intel|Hyundai|Inspiron|Gateway|Huawei|Sony|Vaio|Xiaomi|Google|Alienware|GPD|Sharp|Getac|Vizio|Panasonic|Packard Bell|Fujitsu|MobileDemand|iView|Haier|Bytespeed)\b')
            ELSE 'Unknown'
        END AS brand_extracted,

        -- 2. Storage Type Detection (SSD vs HDD)
        -- Analyzes title for presence/absence of storage keywords.
        CASE 
            WHEN REGEXP_CONTAINS(UPPER(title), r'NO HDD') AND REGEXP_CONTAINS(UPPER(title), r'SSD') THEN 'SSD'
            WHEN REGEXP_CONTAINS(UPPER(title), r'NO SSD') AND REGEXP_CONTAINS(UPPER(title), r'HDD') THEN 'HDD'
            WHEN REGEXP_CONTAINS(UPPER(title), r'HDD') THEN 'HDD'
            WHEN REGEXP_CONTAINS(UPPER(title), r'SSD') THEN 'SSD'
            ELSE 'Unknown'
        END AS storage_type_extracted,

        -- 3. Capacity Extraction
        -- Extracts all numeric values followed by storage units (GB/TB) into an array.
        REGEXP_EXTRACT_ALL(title, r'(?i)(\d+)\s*(?:GB|TB|G|T)\b') AS raw_capacities_array,
        REGEXP_EXTRACT_ALL(title, r'(?i)(?:GB|TB|G|T)\b') AS raw_units_array
    FROM deduplicated
),

-- Parse extracted capacity arrays into individual columns
parsed_capacities AS (
    SELECT 
        *,
        SAFE_CAST(raw_capacities_array[SAFE_OFFSET(0)] AS INT64) AS cap1_val,
        UPPER(raw_units_array[SAFE_OFFSET(0)]) AS cap1_unit,
        
        SAFE_CAST(raw_capacities_array[SAFE_OFFSET(1)] AS INT64) AS cap2_val,
        UPPER(raw_units_array[SAFE_OFFSET(1)]) AS cap2_unit
    FROM extracted_features
),

-- Normalize all storage units to Gigabytes (GB) for comparison
normalized_capacities AS (
    SELECT 
        *,
        CASE 
            WHEN cap1_unit IN ('TB', 'T') THEN cap1_val * 1024 
            ELSE cap1_val 
        END AS cap1_gb,
        
        CASE 
            WHEN cap2_unit IN ('TB', 'T') THEN cap2_val * 1024 
            ELSE cap2_val 
        END AS cap2_gb
    FROM parsed_capacities
),

-- Apply business logic to distinguish RAM from Storage and standardize fields
final_logic AS (
    SELECT 
        listing_id,
        title,
        price,
        currency,
        seller_username,
        seller_feedback_score,
        condition_id,
        condition_name,
        shipping_cost,
        brand_extracted AS brand,
        storage_type_extracted AS storage_type,
        
        -- Logic: Distinguish RAM vs Storage based on capacity size.
        -- Assumption: If two values exist, the smaller value (<= 64GB) is RAM.
        CASE 
            WHEN cap1_gb IS NOT NULL AND cap2_gb IS NOT NULL THEN
                CASE 
                    WHEN LEAST(cap1_gb, cap2_gb) <= 64 THEN CAST(LEAST(cap1_gb, cap2_gb) AS STRING) || 'GB'
                    ELSE 'Unknown'
                END
            ELSE 'Unknown'
        END AS ram_size,

        CASE 
            WHEN cap1_gb IS NOT NULL AND cap2_gb IS NOT NULL THEN
                CASE 
                    WHEN GREATEST(cap1_gb, cap2_gb) >= 128 THEN 
                        CAST(GREATEST(cap1_gb, cap2_gb) AS STRING) || 'GB'
                    ELSE 'Unknown'
                END
            -- If only one value exists, verify if it fits Storage criteria
            WHEN cap1_gb IS NOT NULL AND cap2_gb IS NULL AND storage_type_extracted != 'Unknown' THEN
                 CAST(cap1_gb AS STRING) || 'GB'
            ELSE 'Unknown'
        END AS storage_capacity,

        -- Calculate total acquisition cost
        (COALESCE(price, 0) + COALESCE(shipping_cost, 0)) AS total_cost,

        -- Standardize item conditions into primary categories
        CASE 
            WHEN condition_name LIKE '%Refurbished%' THEN 'Refurbished'
            WHEN condition_name = 'New' THEN 'New'
            WHEN condition_name IN ('Used', 'Open box') THEN 'Used'
            WHEN condition_name = 'For parts or not working' THEN 'Broken'
            ELSE 'Other'
        END AS standard_condition

    FROM normalized_capacities
)

SELECT * FROM final_logic
-- Exclude low-value outliers (accessories incorrectly categorized as laptops)
WHERE price >= 50