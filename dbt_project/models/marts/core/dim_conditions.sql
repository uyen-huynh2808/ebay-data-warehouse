/*
    Dimension Model: dim_conditions
    Description: 
        A lookup table for item conditions (New, Used, Refurbished, etc.).
        Derived from distinct values in the staging layer.
*/

WITH distinct_conditions AS (
    SELECT DISTINCT
        condition_id,
        condition_name,
        standard_condition -- Included for broader categorical grouping
    FROM {{ ref('stg_ebay_listings') }}
)

SELECT
    condition_id,
    condition_name,
    standard_condition
FROM distinct_conditions
WHERE condition_id IS NOT NULL