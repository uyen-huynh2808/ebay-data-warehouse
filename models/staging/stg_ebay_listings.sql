WITH base AS (
    SELECT
        l.ListingID AS Listing_ID,
        l.SellerID AS Seller_ID,
        l.ConditionID AS Condition_ID,
        s.FeedbackScore AS Feedback_Score,
        c.ConditionName AS Condition_Name,

        -- Derived: Standardized condition category
        CASE 
            WHEN c.ConditionName LIKE '%Refurbished%' THEN 'Refurbished'
            WHEN c.ConditionName = 'New' THEN 'New'
            WHEN c.ConditionName IN ('Used', 'Open box') THEN 'Used'
            WHEN c.ConditionName = 'For parts or not working' THEN 'Broken'
            ELSE 'Other'
        END AS Standard_Condition,

        d.LaptopID AS Laptop_ID,  
        d.Brand,
        d.RamSize AS Ram_Size,
        d.StorageType AS Storage_Type,
        d.StorageCapacity AS Storage_Capacity,
        l.Price,
        l.Currency,
        l.ShippingCost AS Shipping_Cost,

        -- Derived field: Total cost
        ROUND(l.Price + l.ShippingCost, 2) AS Total_Cost
    FROM `ebay-bigquery.laptop_listings.fact_laptop_listings` AS l
    LEFT JOIN `ebay-bigquery.laptop_listings.dim_sellers` AS s USING (SellerID)
    LEFT JOIN `ebay-bigquery.laptop_listings.dim_conditions` AS c USING (ConditionID)
    LEFT JOIN `ebay-bigquery.laptop_listings.dim_laptops` AS d
        ON l.ListingID = d.LaptopID  -- Join on ListingID matching LaptopID
    WHERE 
        -- Remove 'unknown' values and filter invalid fields
        l.ListingID != 'Unknown' AND
        l.SellerID != 'Unknown' AND
        c.ConditionName != 'Unknown' AND
        d.LaptopID != 'Unknown' AND
        d.Brand != 'Unknown' AND
        l.Currency != 'Unknown' AND

        -- Validation conditions
        s.FeedbackScore BETWEEN 0.0 AND 100.0 AND
        l.Price >= 0 AND
        l.ShippingCost >= 0
)

SELECT
    Listing_ID,
    Seller_ID,
    Feedback_Score,
    Condition_ID,
    Condition_Name,
    Standard_Condition,
    Laptop_ID,  
    Brand,
    Ram_Size,
    Storage_Type,
    Storage_Capacity,
    Price,
    Currency,
    Shipping_Cost,
    Total_Cost
FROM base
