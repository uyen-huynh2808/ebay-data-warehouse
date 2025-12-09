/*
    Intermediate Model: int_price_trends
    Description: Analyzes pricing strategies per Seller for each Brand.
*/

WITH listings AS (
    SELECT * FROM {{ ref('stg_ebay_listings') }}
),

seller_brand_stats AS (
    SELECT 
        brand,
        seller_username AS seller_id, -- Mapping to standardized name
        
        -- Pricing Strategy Metrics
        COUNT(listing_id) AS total_listings,
        ROUND(AVG(price), 2) AS avg_selling_price,
        MIN(price) AS min_selling_price,
        MAX(price) AS max_selling_price
        
    FROM listings
    WHERE brand != 'Unknown'
    GROUP BY brand, seller_username
)

SELECT * FROM seller_brand_stats