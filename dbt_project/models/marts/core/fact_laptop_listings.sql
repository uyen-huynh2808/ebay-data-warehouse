/*
    Fact Model: fact_laptop_listings
    Description: 
        The central transactional table containing listing prices, shipping costs,
        and foreign keys connecting to dimensions (Sellers, Conditions, Laptops).
*/

WITH staging AS (
    SELECT * FROM {{ ref('stg_ebay_listings') }}
)

SELECT
    -- Primary Key
    listing_id,

    -- Foreign Keys
    listing_id AS laptop_id,      -- FK to dim_laptops
    seller_username AS seller_id, -- FK to dim_sellers
    condition_id,                 -- FK to dim_conditions

    -- Metrics / Measures
    price,
    currency,
    shipping_cost,
    total_cost

FROM staging