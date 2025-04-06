WITH competitor_pricing AS (
    SELECT
        Brand,
        Standard_Condition,
        Avg_Price,
        Min_Price,
        Max_Price,
        Total_Listings,
        CASE
            WHEN Standard_Condition = 'New' THEN 'New Listings'
            WHEN Standard_Condition = 'Used' THEN 'Used Listings'
            ELSE 'Refurbished Listings'
        END AS Condition_Category
    FROM {{ ref('int_competitor_pricing') }}
)

SELECT * FROM competitor_pricing