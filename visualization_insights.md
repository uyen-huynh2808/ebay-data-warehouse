# eBay Laptop Listings: Visualization & Insights

This document summarizes the visual insights obtained from three analytical data marts: `mart_seller_performance`, `mart_competition_price`, and `mart_price_trends`. Each section includes observations and actionable findings derived from the charts.

---

## 1. Seller Performance (`mart_seller_performance`)

### **Chart 1: Average Total Listings by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier` (Top Seller, Rising Seller, New Seller)  
- **Y-axis**: `Total_Listings`

[!Average Total Listings by Seller Tier](https://private-user-images.githubusercontent.com/201462828/430766340-30f9461b-8a25-4bde-90f6-74b18d7f995d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTMxOTMsIm5iZiI6MTc0Mzk5Mjg5MywicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2MzQwLTMwZjk0NjFiLThhMjUtNGJkZS05MGY2LTc0YjE4ZDdmOTk1ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjI4MTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZWFjYzA4ZWI0N2JkZjA5OTliZmVhZDg2MTRmY2FkMWEyOGRiZjg2NTc5NTA3ZGM4ODg3NTlmMTcwNGFjYmVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aTDBC7y0xoFZGnozQdjHwxASQatm_i2V8b9w_FOo4FQ)

**Insights**:
- Top Sellers account for the majority of listings, indicating their strong foothold in the marketplace.
- Rising Sellers make up a moderate share, suggesting potential for growth.
- New Sellers have the fewest listings, which may reflect barriers to entry or early-stage participation.

### **Chart 2: Average Price by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier`  
- **Y-axis**: `Avg_Price`

[!Average Price by Seller Tier](https://private-user-images.githubusercontent.com/201462828/430766416-bf1d7312-d31b-4f12-93e4-1c3bf1b25955.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTMyNTksIm5iZiI6MTc0Mzk5Mjk1OSwicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2NDE2LWJmMWQ3MzEyLWQzMWItNGYxMi05M2U0LTFjM2JmMWIyNTk1NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjI5MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01YjUyYzdjOGIxMjAxZWU1OWUzOGI3YzMxMmE3ODBkYmM3ZTkyMzE5Y2Y5YTBiNGE3ZTU1Y2Q3OTljNjMzYzFiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.f2SGxDp0rBn7SccQkAfmrtPFl-LSQ6TLldr5-HBUfo0)

**Insights**:
- Top Sellers tend to list products at higher average prices, likely leveraging trust and quality to command premium pricing.
- New Sellers offer the lowest average prices, potentially using competitive pricing to attract buyers.
- Rising Sellers fall in between, hinting at a transitional pricing strategy.

---

## 2. Competition Price Analysis (`mart_competition_price`)

### **Chart 1: Average Price by Condition Category (Bar Chart)**
- **X-axis**: `Condition_Category` (New, Used, Refurbished)  
- **Y-axis**: `Avg_Price`

[!Average Price by Condition Category](https://private-user-images.githubusercontent.com/201462828/430766515-e24f3c70-3d1d-425d-abb8-d6b1d5d50e55.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTMzMjEsIm5iZiI6MTc0Mzk5MzAyMSwicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2NTE1LWUyNGYzYzcwLTNkMWQtNDI1ZC1hYmI4LWQ2YjFkNWQ1MGU1NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjMwMjFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MTI0ZGRjNGY4YmQzOTI1NzkxYjYwNDViN2VjYjkwOTRkMjc5MzJmOWU0NTE5Y2EyY2E5MzEwMWIyYWVmMmIxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.z-QA83LXxVacIaozpQWFici-pHbOPrkVjswg-1UFYLI)

**Insights**:
- New Listings have the highest average prices, reflecting their pristine condition and original packaging.
- Refurbished items are priced lower than new but higher than used, offering a balance of quality and affordability.
- Used Listings have the lowest average prices, appealing to budget-conscious buyers.

### **Chart 2: Min and Max Price by Condition Category (Line Chart)**
- **X-axis**: `Condition_Category`  
- **Y-axis**: `Min_Price`, `Max_Price`

[!Min and Max Price by Condition Category](https://private-user-images.githubusercontent.com/201462828/430766612-7cffd267-583c-4a58-b83c-bd6ab2a98f8b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTMzNTMsIm5iZiI6MTc0Mzk5MzA1MywicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2NjEyLTdjZmZkMjY3LTU4M2MtNGE1OC1iODNjLWJkNmFiMmE5OGY4Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjMwNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MzhiNTc0ZDE0NGNmYjFhM2MyNGIzYzliNjJhMDNhMjI3MTY5NTM0N2ExMzVlMDc3YjQ4NDU3ZWEwODg2YzVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.NSEIAZnOJumtfyYYIqw7HldzhQnHOwlomGs74dl1CPI)

**Insights**:
- New items have a wide price range, suggesting varying specifications and models.
- Refurbished listings show a narrower range, possibly due to standardized repair/refurbishing practices.
- Used items show the highest price variability, which may stem from differences in wear, age, or seller credibility.

---

## 3. Price Trends (`mart_price_trends`)

### **Chart 1: Price Tendency Distribution (Bar Chart)**
- **X-axis**: `Price_Tendency` (Price Spike, Price Drop, Stable Price)  
- **Y-axis**: `Total_Listings`

[!Price Tendency Distribution](https://private-user-images.githubusercontent.com/201462828/430766673-61d69386-08c7-4b5a-91b5-40dfcc05b86a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTM0NTYsIm5iZiI6MTc0Mzk5MzE1NiwicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2NjczLTYxZDY5Mzg2LTA4YzctNGI1YS05MWI1LTQwZGZjYzA1Yjg2YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjMyMzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNWNmOGVhZTYzYzU1YWQ3MTY4N2IxZDg1YTRjMjlhYmJjY2M5Y2Q2NDA5MGJmNTcyNTBiY2YxYTliZWMyNjViJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.nLaQ1Y_HgbN9gq10fBFavpWMH9gGJRGXBRGEoMk6z74)

**Insights**:
- Most listings fall into the "Stable Price" category, indicating a relatively steady market.
- A significant number of "Price Drops" may imply competitive pricing behavior or excess inventory clearance.
- "Price Spikes" are less frequent, potentially representing limited-time deals or exclusive models.

### **Chart 2: Min and Max Price by Price Tendency (Line Chart)**
- **X-axis**: `Price_Tendency`  
- **Y-axis**: `Min_Price`, `Max_Price`

[!Min and Max Price by Price Tendency](https://private-user-images.githubusercontent.com/201462828/430766737-ad78bd79-b10b-41f2-9d17-895d6532c300.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5OTM1MzEsIm5iZiI6MTc0Mzk5MzIzMSwicGF0aCI6Ii8yMDE0NjI4MjgvNDMwNzY2NzM3LWFkNzhiZDc5LWIxMGItNDFmMi05ZDE3LTg5NWQ2NTMyYzMwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwN1QwMjMzNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYmYyMDk0NmU5ZGFiYTkyN2Q0NzkyZmU4OGJmOWU2N2FiMWUxZjFjYjFjMzM4OTBlNWRlMjEwODZjYzdkMGQyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.NTRacvgvWysjJCbPnj3uYNez2hdfWhapkRLIwzr_g1Y)

**Insights**:
- Listings with "Price Spikes" exhibit the highest max prices, possibly due to premium models or demand surges.
- "Price Drops" show a lower minimum price range, consistent with discounting strategies.
- "Stable Price" listings maintain a consistent range, reinforcing their reliability in pricing.
