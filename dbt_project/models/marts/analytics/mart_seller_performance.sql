/*
    Analytics Model: mart_seller_performance
    Description: 
        Final presentation layer for seller segmentation.
        The 'seller_tier' logic is inherited from the intermediate layer to ensure consistency
        across the data warehouse.
*/

WITH source AS (
    SELECT * FROM {{ ref('int_seller_performance') }}
)

SELECT
    seller_id,
    feedback_score,
    total_listings,
    avg_item_price,
    total_gross_merchandise_value,
    
    -- Inherited Business Logic: Tier is pre-calculated in int_seller_performance
    seller_tier

FROM source