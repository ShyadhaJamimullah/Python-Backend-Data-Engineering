# Titanic Dataset – ETL Process & SQL Validation


## Workflow
- Extract → Load CSV data into staging table
- Transform → Clean & convert data types
- Load → Store processed data into final table
- Validate → Perform ETL testing queries
- Analyze → Apply business SQL logic


## Database Used
Database name: ```titanic```
```sql
USE titanic;
SELECT DATABASE();
```


## Staging Table (Raw Data Load)
The staging table stores raw CSV data without cleaning.
```sql
CREATE TABLE titanic_staging (
    PassengerId varchar(20),
    Survived varchar(10),
    Pclass varchar(10),
    Name TEXT,
    Sex varchar(10),
    Age varchar(20),
    SibSp varchar(10),
    Parch varchar(10),
    Ticket varchar(50),
    Fare varchar(20),
    Cabin varchar(50),
    Embarked varchar(10)
);
```
**Record Count Validation**
```sql
SELECT COUNT(*) FROM titanic_staging;
```


## Transformation (Data Cleaning)
Convert string values → proper numeric types and handle missing values.
```sql
CREATE TABLE titanic_clean AS
SELECT
    CAST(PassengerId AS UNSIGNED) AS PassengerId,
    CAST(Survived AS UNSIGNED) AS Survived,
    CAST(Pclass AS UNSIGNED) AS Pclass,
    Name,
    Sex,
    CAST(NULLIF(Age, '') AS DECIMAL(5,2)) AS Age,
    CAST(SibSp AS UNSIGNED) AS SibSp,
    CAST(Parch AS UNSIGNED) AS Parch,
    Ticket,
    CAST(NULLIF(Fare, '') AS DECIMAL(10,2)) AS Fare,
    NULLIF(Cabin, '') AS Cabin,
    NULLIF(Embarked, '') AS Embarked
FROM titanic_staging;
```


## ETL Testing & Validation
**Source vs Target Validation**
Check whether records were loaded correctly.
```sql
SELECT COUNT(*) FROM titanic_staging;
SELECT COUNT(*) FROM titanic_clean;
```
**Null Value Checks**
```sql
SELECT COUNT(*) FROM titanic_clean WHERE PassengerId IS NULL;
SELECT COUNT(*) FROM titanic_clean WHERE Age IS NULL;
SELECT COUNT(*) FROM titanic_clean WHERE Cabin IS NULL;
```


## SQL Analysis Queries
**GROUP BY Example**
Passenger survival count:
```sql
SELECT COUNT(*) FROM titanic_clean GROUP BY Survived;
```
**Business Logic — Survival Percentage**
```sql
SELECT ROUND(SUM(Survived)/COUNT(*) * 100, 2) AS survival_percentage
FROM titanic_clean;
```
Add column for storing metric:
```sql
ALTER TABLE titanic_clean ADD survival_percentage DECIMAL(5,2);
SHOW COLUMNS FROM titanic_clean;
```


## Table Alterations
**Add Primary Key**
```sql
ALTER TABLE titanic_clean ADD PRIMARY KEY (PassengerID);
```


## Data Cleaning Updates
Update missing cabin values safely:
```sql
SET sql_safe_updates = 0;

UPDATE titanic_clean
SET Cabin = 'Unknown'
WHERE Cabin IS NULL;

SET sql_safe_updates = 1;
```


## Final Output
```sql
SELECT * FROM titanic_clean;
```
