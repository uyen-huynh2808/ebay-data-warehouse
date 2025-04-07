WITH seller_stats AS (
    SELECT
        Seller_ID,
        COUNT(Listing_ID) AS Total_Listings,
        ROUND(AVG(Price), 2) AS Avg_Price,
        Feedback_Score
    FROM {{ ref('stg_ebay_listings') }}
    GROUP BY Seller_ID, Feedback_Score
)

SELECT * FROM seller_stats