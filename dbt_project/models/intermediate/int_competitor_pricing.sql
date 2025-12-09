/*
    Intermediate Model: int_competitor_pricing
    Description: Aggregates pricing metrics by Brand and Condition to identify market benchmarks.
*/

WITH listings AS (
    SELECT * FROM {{ ref('stg_ebay_listings') }}
),

market_stats AS (
    SELECT
        brand,
        standard_condition,
        
        -- Calculated Metrics
        COUNT(listing_id) AS total_listings,
        ROUND(AVG(price), 2) AS avg_market_price,
        MIN(price) AS min_market_price,
        MAX(price) AS max_market_price
        
    FROM listings
    -- Filter out unknown brands to keep analytics clean
    WHERE brand != 'Unknown'
    GROUP BY brand, standard_condition
)

SELECT * FROM market_stats