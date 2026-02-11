## Sales Data Warehouse – Star Schema Implementation (MySQL)

### Star Schema Architecture
The schema follows a Star Schema structure:
- One central **Fact Table** → `sales_fact`
- Four surrounding Dimension Tables:
  - `date_dimension`
  - `product_dimension`
  - `customer_dimension`
  - `store_dimension`
 
### Database Used
Database name: `sales_dw`
```sql
USE sales_dw;
SELECT DATABASE();
```

### Dimension Tables
**1. Date Dimension**

Stores date-related information.
```sql
CREATE TABLE date_dimension(
    date_id INT PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    quarter INT
    );
```

**2. Product Dimension**

Stores product details.
```sql
CREATE TABLE product_dimension(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);
```

**3. Customer Dimension**

Stores customer information.
```sql
CREATE TABLE customer_dimension(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    gender VARCHAR(20),
    city VARCHAR(50),
    state VARCHAR(50)
);
```

**4. Store Dimension**

Stores store details.
```sql
CREATE TABLE store_dimension(
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50)
);
```

### Fact Table
**Sales Fact Table**
```sql
CREATE TABLE sales_fact(
    sales_id INT PRIMARY KEY,
    date_id INT,
    product_id INT,
    customer_id INT,
    store_id INT,
    quantity_sold INT,
    total_amount DECIMAL(10,2),

    FOREIGN KEY (date_id) REFERENCES date_dimension (date_id),
    FOREIGN KEY (product_id) REFERENCES product_dimension (product_id),
    FOREIGN KEY (customer_id) REFERENCES customer_dimension (customer_id),
    FOREIGN KEY (store_id) REFERENCES store_dimension (store_id)
);
```

### Insert Sample Data
**Date Dimension**
```sql
INSERT INTO date_dimension VALUES 
(1,20,1,2026,1),
(2,21,1,2026,1),
(3,22,1,2026,1),
(4,23,1,2026,1);
```
**Product Dimension**
```sql
INSERT INTO product_dimension VALUES
(1,"Pen","Stationary","Cello",20),
(2,"Pencil","Stationary","Doms",10),
(3,"Bottle","Utensils","Milton",600),
(4,"Earphone","Audio devices","Boat",1000);
```
**Customer Dimension**
```sql
INSERT INTO customer_dimension VALUES
(1,"Tara","Female","Coimbatore","Tamilnadu"),
(2,"Thansika","Female","Palani","Dindigul"),
(3,"Shyadha","Female","Coonoor","The Nilgiris"),
(4,"Thanisha","Female","Aruvangadu","The Nilgiris");
```
**Store Dimension**
```sql
INSERT INTO store_dimension VALUES
(1,"A store","Coimbatore","Tamilnadu"),
(2,"Z store","Ooty","The Nilgiris");
```
**Sales Fact**
```sql
INSERT INTO sales_fact 
(sales_id, date_id, product_id, customer_id, store_id, quantity_sold, total_amount) 
VALUES 
(10,1,1,1,1,50,1000),
(20,2,2,2,2,40,2000);
```
### View All Records in Sales Fact Table
```sql
SELECT * FROM sales_fact;
```

