/*
    Intermediate Model: int_seller_performance
    Description: 
        Evaluates seller performance based on listing volume and feedback.
        Classifies sellers into tiers (Top, Rising, New) for segmentation.
*/

WITH listings AS (
    SELECT * FROM {{ ref('stg_ebay_listings') }}
),

seller_aggregation AS (
    SELECT
        seller_username AS seller_id,
        -- Taking MAX in case feedback score changes slightly between listings, 
        -- though usually it's consistent per ingestion.
        MAX(seller_feedback_score) AS feedback_score,
        
        -- Performance Metrics
        COUNT(listing_id) AS total_listings,
        ROUND(AVG(price), 2) AS avg_item_price,
        SUM(price) AS total_gross_merchandise_value -- GMV (Doanh thu tổng)
        
    FROM listings
    GROUP BY seller_username
),

ranked_sellers AS (
    SELECT 
        *,
        -- BUSINESS LOGIC: Seller Classification
        CASE 
            WHEN feedback_score >= 98.0 AND total_listings >= 50 THEN 'Top Seller'
            WHEN feedback_score >= 90.0 AND total_listings BETWEEN 10 AND 49 THEN 'Rising Seller'
            WHEN total_listings < 10 THEN 'New Seller'
            ELSE 'Regular Seller'
        END AS seller_tier
    FROM seller_aggregation
)

SELECT * FROM ranked_sellers