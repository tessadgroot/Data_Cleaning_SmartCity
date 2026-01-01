# Smart City Sensor Data Cleaning & Aggregation Pipeline (Python)

## 📌 Project Overview
This project is a Python-based data engineering pipeline that reads, cleans, validates, aggregates, and exports Smart City sensor time-series data.

The goal of this project is to demonstrate:

- Object-Oriented Programming (OOP)
- Data cleaning and validation with pandas
- Time series processing and aggregation
- Outlier detection using statistical methods
- Logging and error handling
- Writing modular, reusable Python code

This project was built as part of a structured learning path toward a data engineering / data analytics role.


## 🧱 Project Architecture

    sensor-cleaning-pipeline/

    ├── reading/
    │   └── Reader.py           # CSV ingestion
    ├── cleaning/
    │   ├── Cleaner.py          # Data cleaning & type conversion
    │   └── Outliers.py         # Outlier detection (IQR method)
    ├── aggregating/
    │   └── Aggregater.py       # Time-based aggregation & resampling
    ├── writing/
    │   └── Writer.py           # Export to Excel
    ├── data/
    │   ├── raw_data/           # Raw sensor CSV files
    │   └── processed_data/     # Cleaned and aggregated output
    ├── main.py                 # Pipeline orchestration
    └── README.md


## ⚙️ Features

✔ Reads raw Smart City sensor data from CSV files

✔ Cleans and standardizes the dataset:
- Normalizes column names
- Converts timestamps and numeric values
- Removes empty rows and invalid records

✔ Detects and removes outliers:
- Uses the Interquartile Range (IQR) method
- Applied to temperature and humidity sensor readings

✔ Performs time-based aggregation:
- Groups data by sensor and location
- Resamples time series at fixed intervals
- Calculates minimum, maximum, and mean values

✔ Exports cleaned and aggregated data:
- Writes processed datasets to Excel files

✔ Logs important processing steps and errors

✔ Optional data visualization using matplotlib



## 📊 Dataset Description
The dataset contains Smart City environmental and air quality sensor measurements, including:

- Timestamped readings
- Multiple sensors and locations
- Temperature and humidity
- Traffic and environmental indicators
- Air quality metrics (CO₂, NO₂, PM2.5, PM10)

The data represents real-world sensor time series and includes missing values and outliers.



## 🧠 What This Project Demonstrates
This project demonstrates the ability to:

- Design reproducible data processing pipelines
- Work with real-world time-series data
- Apply statistical methods for data quality improvement
- Use advanced pandas features (`groupby`, `resample`)
- Structure Python projects using OOP principles
- Implement logging and basic fault tolerance


