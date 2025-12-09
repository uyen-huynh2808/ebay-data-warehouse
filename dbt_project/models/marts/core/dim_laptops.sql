/*
    Dimension Model: dim_laptops
    Description: 
        Contains technical specifications for each laptop listing.
        Maps listing_id to laptop_id as a 1:1 relationship in this schema design.
*/

WITH staging AS (
    SELECT * FROM {{ ref('stg_ebay_listings') }}
)

SELECT
    listing_id AS laptop_id, -- Surrogate key for the laptop entity
    brand,
    ram_size,
    storage_type,
    storage_capacity
FROM staging