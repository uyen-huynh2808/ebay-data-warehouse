/*
    Analytics Model: mart_competitor_pricing
    Description: 
        Final presentation layer for competitor pricing analysis.
        Adds a reader-friendly 'Condition Category' label for visualization in Looker Studio.
*/

WITH source AS (
    SELECT * FROM {{ ref('int_competitor_pricing') }}
)

SELECT
    brand,
    standard_condition,
    avg_market_price,
    min_market_price,
    max_market_price,
    total_listings,
    
    -- Presentation Logic: Create user-friendly labels for dashboard filters
    CASE 
        WHEN standard_condition = 'New' THEN 'New Listings'
        WHEN standard_condition = 'Used' THEN 'Used Listings'
        ELSE 'Refurbished & Other'
    END AS condition_category

FROM source