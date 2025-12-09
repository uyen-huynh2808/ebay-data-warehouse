/*
    Dimension Model: dim_sellers
    Description: 
        Contains unique records for each seller. 
        Sourced from the intermediate seller performance model to include pre-calculated 
        tiers and aggregated feedback scores.
*/

WITH seller_performance AS (
    SELECT * FROM {{ ref('int_seller_performance') }}
)

SELECT
    seller_id,
    feedback_score,
    -- Including seller_tier as it provides valuable context for the seller dimension
    seller_tier
FROM seller_performance