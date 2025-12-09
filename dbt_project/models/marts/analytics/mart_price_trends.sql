/*
    Analytics Model: mart_price_trends
    Description: 
        Final presentation layer for analyzing seller pricing volatility.
        Calculates 'Price Tendency' to highlight significant deviations (Spikes/Drops) 
        from the seller's average price for a specific brand.
*/

WITH source AS (
    SELECT * FROM {{ ref('int_price_trends') }}
)

SELECT
    brand,
    seller_id,
    avg_selling_price,
    min_selling_price,
    max_selling_price,
    total_listings,

    -- Presentation Logic: Identify pricing anomalies
    -- Spike: Max price is >20% higher than average
    -- Drop: Min price is <20% lower than average
    CASE 
        WHEN max_selling_price > (avg_selling_price * 1.2) THEN 'Price Spike'
        WHEN min_selling_price < (avg_selling_price * 0.8) THEN 'Price Drop'
        ELSE 'Stable Price'
    END AS price_tendency

FROM source