## Superstore Sales Data Pipeline & Analysis
This task demonstrates a complete data pipeline using Python, from raw data ingestion to cleaning, transformation, analysis, and storage.

### Dataset Overview
- Contains 9,800 sales records
- Includes order details, customer information, product categories, shipping dates, and sales values
- Data represents real-world retail transactions with minor inconsistencies

### Workflow Overview
**1. Data Ingestion**
- Loaded sales data from a CSV file

**2. Data Cleaning**
- Standardized column names
- Converted date columns to proper datetime format
- Removed invalid or zero sales records
- Handled missing postal codes
- Checked and confirmed no duplicate records
  
**3. Data Transformation**
- Extracted time-based features (```year```, ```month```, ```quarter```)
- Calculated ```shipping duration```
- Created shipping speed categories (```Fast```, ```Medium```, ```Slow```)
  
**4. Analysis & KPI Calculation**
- Calculated total and average sales
- Analyzed sales trends by month and quarter
- Identified top products, customers, regions, and categories
- Evaluated shipping performance
  
**5. Data Storage & Export**
- Stored cleaned data in a MySQL database
- Exported KPIs and analytical results as JSON files

### Outputs
**MySQL Table:** Cleaned sales data

**JSON Files:**
- KPI summary
- Monthly & quarterly sales
- Category-wise and region-wise sales
- Top products and customers
