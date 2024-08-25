# BDL_E-commerce_scrape_assignment
This project is designed to fetch, process, and analyze data from a web source using Python. It utilizes Selenium for web scraping and the `requests` library to interact with a RESTful API. The gathered data is then stored in Excel files for easy access and analysis.

## Features
- Fetch store client data using Selenium.
- Retrieve user cart data from a public API.
- Fetch additional user details and product information.
- Combine and save user and product data to Excel files.
- Process the Excel files to structure the data better.

## Technologies Used
- Python 3.x
- Selenium
- Requests
- Pandas
- Unittest
- OpenPyXL (for Excel file handling)

# Install req
pip install -r requirements.txt

# Running the Scripts
To run the main data fetching and processing script, execute the following command in your terminal:

- python main.py

This script will perform the following tasks:

- Fetch store client data.
- Fetch user cart data.
- Fetch user details.
- Fetch product details.
- Save the collected user data to an Excel file named combined_user_data.xlsx.
- Save the product data to an Excel file named product_data.xlsx.

# Using the Optional Script
- python final_data_filtering.py

This script will:
processes product and user data from Excel files.
It updates the product data by splitting ratings into separate columns,
ensures data types are correct, and processes user data by splitting 
address information into separate columns and converting 'Last Login' 
to a datetime format. The updated data is then saved back to the respective Excel files.

# Running the Tests
- python -m unittest tests/test_data_fetcher.py
