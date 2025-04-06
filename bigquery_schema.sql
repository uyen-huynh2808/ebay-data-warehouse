-- Create the dataset (if not created already)
CREATE SCHEMA IF NOT EXISTS `ebay-bigquery.laptop_listings`;

-- Create dimension table for laptops
CREATE TABLE `ebay-bigquery.laptop_listings.dim_laptops` (
    LaptopID STRING NOT NULL,
    Brand STRING NOT NULL,
    RamSize STRING NOT NULL,
    StorageType STRING NOT NULL,
    StorageCapacity STRING NOT NULL,

    PRIMARY KEY (LaptopID) NOT ENFORCED
);

-- Create dimension table for sellers
CREATE TABLE `ebay-bigquery.laptop_listings.dim_sellers` (
    SellerID STRING NOT NULL,
    FeedbackScore FLOAT64 NOT NULL,

    PRIMARY KEY (SellerID) NOT ENFORCED
);

-- Create dimension table for conditions
CREATE TABLE `ebay-bigquery.laptop_listings.dim_conditions` (
    ConditionID INT64 NOT NULL,
    ConditionName STRING NOT NULL,

    PRIMARY KEY (ConditionID) NOT ENFORCED
);

-- Create fact table
CREATE TABLE `ebay-bigquery.laptop_listings.fact_laptop_listings` (
    ListingID STRING NOT NULL,
    SellerID STRING NOT NULL,
    ConditionID INT64 NOT NULL,
    Price FLOAT64 NOT NULL,
    Currency STRING NOT NULL,
    ShippingCost FLOAT64 NOT NULL,
    
    PRIMARY KEY (ListingID) NOT ENFORCED
);