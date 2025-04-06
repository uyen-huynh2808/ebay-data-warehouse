WITH price_stats AS (
    SELECT 
        Brand,
        Seller_ID,
        ROUND(AVG(Price), 2) AS Avg_Price,
        MIN(Price) AS Min_Price,
        MAX(Price) AS Max_Price,
        COUNT(Listing_ID) AS Total_Listings
    FROM {{ ref('stg_ebay_listings') }}
    GROUP BY Brand, Seller_ID
)

SELECT * FROM price_stats