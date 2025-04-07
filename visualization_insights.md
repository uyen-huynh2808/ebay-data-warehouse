# eBay Laptop Listings: Visualization & Insights

This document summarizes the visual insights obtained from three analytical data marts: `mart_seller_performance`, `mart_competition_price`, and `mart_price_trends`. Each section includes observations and actionable findings derived from the charts.

---

## 1. Seller Performance (`mart_seller_performance`)

### **Chart 1: Total Listings by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier` (Top Seller, Rising Seller, New Seller)  
- **Y-axis**: `Total_Listings`

![Total-Listings-by-Seller-Tier](https://github.com/user-attachments/assets/94776d2f-dffa-488e-b74c-1d7b32bda75f)

**Insights**:


### **Chart 2: Average Price by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier`  
- **Y-axis**: `Avg_Price`

![Average-Price-by-Seller-Tier](https://github.com/user-attachments/assets/38e6f2b8-7c0e-4456-acfa-783369d3bf14)

**Insights**:

---

## 2. Competition Price Analysis (`mart_competition_price`)

### **Chart 1: Average Price by Condition Category (Bar Chart)**
- **X-axis**: `Condition_Category` (New, Used, Refurbished)  
- **Y-axis**: `Avg_Price`

![Average-Price-by-Condition-Category](https://github.com/user-attachments/assets/470c1c42-1de0-4808-a577-011bf5f8acd9)

**Insights**:


### **Chart 2: Min and Max Price by Condition Category (Line Chart)**
- **X-axis**: `Condition_Category`  
- **Y-axis**: `Min_Price`, `Max_Price`

![Min-and-Max-Price-by-Condition-Category](https://github.com/user-attachments/assets/fa84667c-63d1-43c7-b65e-e5644d8949c2)

**Insights**:


---

## 3. Price Trends (`mart_price_trends`)

### **Chart 1: Price Tendency Distribution (Bar Chart)**
- **X-axis**: `Price_Tendency` (Price Spike, Price Drop, Stable Price)  
- **Y-axis**: `Total_Listings`

![Price-Tendency-Distribution](https://github.com/user-attachments/assets/ffee25c7-ae5b-419e-8348-03e1eb806336)

**Insights**:


### **Chart 2: Min and Max Price by Price Tendency (Line Chart)**
- **X-axis**: `Price_Tendency`  
- **Y-axis**: `Min_Price`, `Max_Price`

![Min-and-Max-Price-by-Price-Tendency](https://github.com/user-attachments/assets/ee78f429-5731-48b9-af5e-129df4291b3c)

**Insights**:
