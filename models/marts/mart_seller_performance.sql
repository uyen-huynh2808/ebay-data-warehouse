WITH seller_stats AS (
    SELECT
        Seller_ID,
        Total_Listings,
        Avg_Price,
        Feedback_Score,
        CASE
            WHEN Total_Listings >= 50 AND Feedback_Score >= 90 THEN 'Top Seller'
            WHEN Total_Listings BETWEEN 10 AND 50 AND Feedback_Score >= 80 THEN 'Rising Seller'
            ELSE 'New Seller'
        END AS Seller_Tier
    FROM {{ ref('int_seller_performance') }}
)

SELECT * FROM seller_stats