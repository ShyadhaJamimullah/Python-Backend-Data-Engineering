## Cafe Sales Data Cleaning & Analysis
This task focuses on cleaning, transforming, and analyzing a messy cafe sales dataset using Python and Pandas.

### About the Dataset
- Contains 10,000 cafe transactions
- Includes details like items sold, quantity, price, payment method, location, and transaction date
- The raw data has missing values, inconsistent text, and incorrect entries

### Data Cleaning Steps
The following steps were performed to improve data quality:
- Standardized column names (lowercase, snake_case)
- Replaced invalid values like ```ERROR```, ```UNKNOWN```, ```NULL```, etc. with proper missing values
- Removed extra spaces and fixed text formatting
- Converted numeric columns (```quantity```, ```price_per_unit```, ```total_spent```) to proper numeric types
- Converted transaction dates to datetime format
- **Handled missing values:**
  - Numeric columns filled using median values
  - Categorical columns filled with "Unknown"
  - Removed records with invalid transaction dates
  - Checked and confirmed there are no duplicate records

### Data Analysis Performed
After cleaning, several analyses were carried out:
- Sorted transactions by date and sales amount
- Filtered transactions based on payment method (e.g., ```Cash```)
- Identified high-value sales transactions
- Found the most frequently purchased items
- Renamed columns for clarity (```total_spent → sales_amount```)
- Removed unnecessary columns to keep the dataset clean

### Outcome
The final dataset is:
- Clean
- Consistent
- Free of missing values
- Ready for further analysis or visualization
