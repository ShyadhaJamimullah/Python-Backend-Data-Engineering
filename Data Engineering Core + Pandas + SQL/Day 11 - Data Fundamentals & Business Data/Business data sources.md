# Identifying Business Data Sources in an E-Commerce Enterprise

This document identifies key business data sources in an e-commerce enterprise and explains their role in operations and business analysis.

## Core Business Operations

- User Registration
- Product Listing
- Order Placement
- Payment
- Delivery
- Feedback
- User Behavior
- Log Data

## Data Generated

**User Registration**

- User ID
- Name
- Email ID
- Contact Number
- Address Details
- Signup Time

**Product Listing**

- Product ID
- Product Name
- Product Description
- Category
- Brand
- Specifications
- Price
- Discount / Offer Price
- Stock Quantity
- Product Images
- Seller Name
- Product Rating

**Order Placement**

- Order ID
- User ID
- Product ID
- Quantity
- Item Price
- Total Amount
- Discount Applied
- GST
- Order status (placed / shipped / delivered / cancelled)

**Payment**

- Payment ID
- Order ID
- Payment Mode (UPI / Card / NetBanking / Wallet)
- Payment Status (success / failed / pending)
- Amount Paid
- Transaction Reference Number
- Payment Timestamp

**Delivery**

- Delivery ID
- Order ID
- Delivery Address
- Delivery Partner Name
- Tracking number
- Estimated delivery date
- Actual delivery date
- Delivery status (in transit / delivered / delayed)

**Feedback/Review**

- User ID
- Product ID
- Review ID
- Ratings
- Review Text
- Review Images
- Review Timestamp

**User Behavior -** *Used for recommendations and analytics*

- Page views
- Product Clicks
- Search Queries
- Time spent on pages

**Log Data -** *Used for system monitoring*

- Login attempts
- Errors
- API requests
 
## Data Type Classification (Structured vs Unstructured)

| Data | Data Format | Type | 
|---|---|---|
| User Data | CSV, SQL tables | Structured | 
| Product data | CSV, SQL tables | Structured | 
| Order data | CSV, SQL tables | Structured |
| Payment data | JSON | Semi-Structured |
| Review Text | TXT, JSON (text field) | Unstructured |
| Product/Review images | JPG,PNG,WEBP | Unstructured |
| User Behavior/Logs | JSON, Log files | Semi-Structured |

## Operational vs Analytical Data

**Operational Data (Real-time)**

Supports day-to-day business operations, real-time transactions, running the business.

*Examples*

- New order
- Payment success
- Login event
- Stock update
- Customer review
- Delivery data


**Analytical Data (Decision-making)**

Used for analysis, reporting, forecasting, decision-making, usually aggregated or processed

*Examples*

- Daily sales report
- Monthly revenue
- Customer behavior trends
- Top-Selling products
- Sentiment analysis on customer reviews
- Churn Prediction

## Business Use of Data

| Data | Business Value | 
|---|---|
| Purchase history | Personalized offers and recommendations| 
| Click behavior | UI improvemnet | 
| Reviews | Product improvement |
| Sales trend | Forecasting | 
| Stock data | Inventory management | 


  

  




