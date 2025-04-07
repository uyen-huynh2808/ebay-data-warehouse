# eBay Laptop Listings: Visualization & Insights

This document summarizes the visual insights obtained from three analytical data marts: `mart_seller_performance`, `mart_competition_price`, and `mart_price_trends`. Each section includes observations and actionable findings derived from the charts.

---

## 1. Seller Performance (`mart_seller_performance`)

### **Chart 1: Total Listings by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier` (Top Seller, Rising Seller, New Seller)  
- **Y-axis**: `Total_Listings`

![Total-Listings-by-Seller-Tier](https://github.com/user-attachments/assets/94776d2f-dffa-488e-b74c-1d7b32bda75f)

**Insights**:
- New Sellers contribute the highest number of listings (2,997), more than double those of Rising (1,435) or Top Sellers (1,230).
- This is likely due to a larger number of New Sellers overall — each contributing a small number of listings — whereas Top Sellers, though fewer in number, may focus on quality, strategic pricing, or higher-value items.
- The relatively lower listing count for Top Sellers does not indicate inactivity, but rather a concentrated seller base with optimized inventories.

### **Chart 2: Average Price by Seller Tier (Bar Chart)**
- **X-axis**: `Seller_Tier`  
- **Y-axis**: `Avg_Price`

![Average-Price-by-Seller-Tier](https://github.com/user-attachments/assets/38e6f2b8-7c0e-4456-acfa-783369d3bf14)

**Insights**:
- Top Sellers have the highest average price ($374.71), followed closely by Rising Sellers ($373.45), while New Sellers list items at a significantly lower average price ($281.64).
- This suggests that experienced sellers are able to command higher prices, likely due to better product quality, trust, and optimized listings. Rising Sellers are already approaching Top Seller pricing, indicating growing confidence and value perception.
- The lower average price from New Sellers may reflect entry-level strategies—such as underpricing to attract buyers, limited reputation, or lower-value inventory.

---

## 2. Competition Price Analysis (`mart_competition_price`)

### **Chart 1: Average Price by Condition Category (Bar Chart)**
- **X-axis**: `Condition_Category` (New, Used, Refurbished)  
- **Y-axis**: `Avg_Price`

![Average-Price-by-Condition-Category](https://github.com/user-attachments/assets/470c1c42-1de0-4808-a577-011bf5f8acd9)

**Insights**:
- New items have the highest average price ($849.17), significantly more than Used ($353.23) and Refurbished ($329.43) items.
- This reflects the premium buyers are willing to pay for brand-new products, which often come with full warranties and no prior usage. Used and Refurbished items are priced similarly, indicating they target more budget-conscious buyers seeking value over novelty.
- The lower average prices for Refurbished and Used items suggest strong demand in the secondary market, where price sensitivity plays a bigger role in purchasing decisions.

### **Chart 2: Min and Max Price by Condition Category (Line Chart)**
- **X-axis**: `Condition_Category`  
- **Y-axis**: `Min_Price`, `Max_Price`

![Min-and-Max-Price-by-Condition-Category](https://github.com/user-attachments/assets/fa84667c-63d1-43c7-b65e-e5644d8949c2)

**Insights**:
- New items show the widest price range ($55.08 to $5000), followed by Used ($50 to $3500) and Refurbished ($50 to $2999).
- This indicates that new products span both entry-level and premium segments, justifying their broader price spread. Used and Refurbished items also cover a wide range but are generally capped at lower maximum prices, reflecting market expectations for second-hand or restored goods.
- The similar minimum prices (~$50) across all conditions suggest competitive entry-level pricing, but the max price differences highlight the higher perceived value and pricing flexibility of brand-new items.

### **Conclusion:**
- New items dominate the high-price end, inflating their average.
- Used and Refurbished are more value-driven, leading to lower averages despite some higher-priced listings.

---

## 3. Price Trends (`mart_price_trends`)

### **Chart 1: Price Tendency Distribution (Bar Chart)**
- **X-axis**: `Price_Tendency` (Price Spike, Price Drop, Stable Price)  
- **Y-axis**: `Total_Listings`

![Price-Tendency-Distribution](https://github.com/user-attachments/assets/ffee25c7-ae5b-419e-8348-03e1eb806336)

**Insights**:
- Spike Price listings are the most common (2,870), followed closely by Stable Price listings (2,694), while Drop Price listings are rare (only 98).
- This suggests that most sellers either maintain consistent pricing or experiment with sudden price increases—possibly to test market response, create urgency, or reflect high demand. The scarcity of Drop Price listings indicates that few sellers adopt markdown strategies, potentially favoring perceived value retention or avoiding pricing wars.
- The dominance of Spike and Stable trends highlights a seller preference for either static pricing or dynamic pricing tactics aimed at maximizing visibility or profit, rather than gradual price drops.

### **Chart 2: Min and Max Price by Price Tendency (Line Chart)**
- **X-axis**: `Price_Tendency`  
- **Y-axis**: `Min_Price`, `Max_Price`

![Min-and-Max-Price-by-Price-Tendency](https://github.com/user-attachments/assets/ee78f429-5731-48b9-af5e-129df4291b3c)

**Insights**:
- Stable Price listings span the full price range ($50 to $5000), while Drop Price and Spike Price patterns also start around $50 but peak at $1953.43 and $4877.70, respectively.
- This suggests that listings with stable pricing cover a wide spectrum, including both low- and high-end products. Drop Price listings, with a lower max price, likely represent items undergoing price reductions to attract buyers—often in mid-range segments.
- Spike Price listings, reaching up to ~$4877.70, may reflect sudden, short-term increases in value—potentially due to rarity, demand surges, or pricing errors. Despite similar starting prices, the variations in max price reflect distinct pricing strategies or market behaviors tied to product type and seller tactics.
