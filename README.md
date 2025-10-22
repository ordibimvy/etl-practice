# ETL Pipeline for Used Car Data

## Overview
This project implements a Python-based **Extract, Transform, Load (ETL)** pipeline that consolidates and cleans used car data from multiple file formats — **CSV**, **JSON**, and **XML** — into a single standardized dataset.

The script demonstrates core ETL concepts including **data extraction**, **data transformation**, **data loading**, and **process logging** using Python and Pandas.

---

## Project Structure
etl_practice.py
    ```bash
    ├── extract_from_csv() # Extracts data from CSV files
    ├── extract_from_json() # Extracts data from JSON files
    ├── extract_from_xml() # Extracts data from XML files
    ├── extract() # Combines all extracted data
    ├── transform() # Cleans and rounds price values
    ├── load_data() # Writes final dataset to CSV
    ├── log_progress() # Records timestamps and messages
    ├── log_file.txt # Logs ETL events
    └── transformed_data.csv # Output after transformation

---

## ETL Workflow

### 1. Extraction
The pipeline automatically scans the working directory for `.csv`, `.json`, and `.xml` files (excluding the output file).  
Each extraction function:
- Reads its respective file type.
- Extracts standardized columns:
  - `car_model`
  - `year_of_manufacture`
  - `price`
  - `fuel`

### 2. Transformation
Data cleaning and formatting steps include:
- Converting `price` values to numeric types.
- Rounding prices to two decimal places.
- Handling invalid numeric entries by coercing them to NaN.

### 3. Loading
After transformation, the cleaned dataset is exported to:
transformed_data.csv


### 4. Logging
Each major step in the ETL process is logged with timestamps in `log_file.txt`, for example:
2025-Oct-22-10:45:21,ETL Job Started
2025-Oct-22-10:45:22,Extract phase Started
2025-Oct-22-10:45:33,ETL Job Ended

---

## Technologies Used
- **Python 3.x**
- **Pandas** – data manipulation and cleaning  
- **xml.etree.ElementTree** – XML parsing  
- **glob** – file discovery  
- **datetime** – timestamp logging  

---

## How to Run

1. Place your source files (`.csv`, `.json`, `.xml`) in the same project folder.  
2. Open a terminal in the project directory.  
3. Run:
   ```bash
   python etl_practice.py
After execution:

The cleaned dataset will be saved as transformed_data.csv

Logs will be stored in log_file.txt

Example Output
car_model	year_of_manufacture	price	fuel
Toyota Camry	2018	15999.50	Gasoline
Honda Civic	2020	18450.00	Hybrid
Ford Focus	2016	9750.25	Diesel

### Learning Objectives
- Build and automate an ETL pipeline using Python.
- Work with multiple data formats (CSV, JSON, XML).
- Perform data cleaning and transformation with Pandas.
- Implement process logging for transparency and traceability.

### Future Enhancements
- Add advanced error handling and data validation.
- Store logs in a database instead of a flat file.
- Schedule automated runs with Apache Airflow or Cron.
- Extend support for Parquet or SQL-based sources.

Author
Ordi Bimvy Nganzobo
Data Engineering Student | Thomas College
