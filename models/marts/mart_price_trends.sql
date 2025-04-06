WITH price_trends AS (
    SELECT
        Brand,
        Seller_ID,
        Avg_Price,
        Min_Price,
        Max_Price,
        Total_Listings,
        CASE
            WHEN Max_Price > Avg_Price * 1.2 THEN 'Price Spike'
            WHEN Min_Price < Avg_Price * 0.8 THEN 'Price Drop'
            ELSE 'Stable Price'
        END AS Price_Tendency
    FROM {{ ref('int_price_trends') }}
)

SELECT * FROM price_trends