WITH competitor_stats AS (
    SELECT
        Brand,
        Standard_Condition,
        ROUND(AVG(Price), 2) AS Avg_Price,
        MIN(Price) AS Min_Price,
        MAX(Price) AS Max_Price,
        COUNT(Listing_ID) AS Total_Listings
    FROM {{ ref('stg_ebay_listings') }}
    GROUP BY Brand, Standard_Condition
)

SELECT * FROM competitor_stats