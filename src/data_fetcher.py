'''
Author: Ilias Adamidis
Date: 09 / 08 / 2024

This python file can be used to fetch data from 2 sources

source 1: https://bigdatalab.ai/assignment_pd001_data/

source 2: https://fakestoreapi.com

The script solves the first 4 tasks of the assignment, the other 2 are going to be solved in the save_data.py

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests

# Constants
WAIT_TIME = 7

# Task 1: Fetch store clients using Selenium
def fetch_store_clients():
    '''
    Fetches client data from a web page using Selenium.
    
    This function automates the browser to navigate to a specific webpage,
    extracts client information from a table, and handles pagination 
    to retrieve data from multiple pages. 

    Returns:
        - Headers of the data
        - The actual data
    '''
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Open the webpage
    driver.get("https://bigdatalab.ai/assignment_pd001_data/")

    # Function to extract data from the table
    def get_data_from_table():
        # Wait for the table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userTable"))
        )

        # Extract table rows
        table = driver.find_element(By.ID, "userTable")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Initialize lists for headers and data
        headers = []
        clients = []

        # Extract headers from the first row
        headers = [header.text for header in rows[0].find_elements(By.TAG_NAME, "th")]

        # Iterate over the remaining rows to extract data
        for row in rows[1:]:  # Start from the second row
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:  # Only add rows with data
                data = [col.text for col in cols]
                clients.append(data)

        return headers, clients

    # Fetch data from the first page
    all_headers, all_clients = get_data_from_table()

    # Wait for the pagination to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pagination"))
    )

    # Extract pagination elements and ignore the first page (already scraped)
    pagination = driver.find_element(By.ID, "pagination")
    all_pages = pagination.find_elements(By.TAG_NAME, 'a')
    needed_pages = all_pages[1:]

    # Iterate over the remaining pages
    for page in needed_pages:
        page.click()  # Click on each page link
        time.sleep(2)  # Small delay to load the new page
        _, clients_on_page = get_data_from_table()  # Get data from the new page
        all_clients.extend(clients_on_page)  # Add the new data to the list
        time.sleep(3)  # Small delay between page clicks

    # Close the WebDriver
    driver.quit()

    #return the data
    return all_headers, all_clients

# Task 2: Fetch all carts for users
def fetch_user_carts():
    '''
    Fetches all user carts from the specified API.

    This function sends a GET request to the carts endpoint of the Fake Store API.
    If the response is successful, it extracts the cart data and returns it along
    with headers. If the request fails, it raises an exception with the
    appropriate status code.

    '''
    url = 'https://fakestoreapi.com/carts'
    response = requests.get(url)
    if response.status_code == 200:
        carts = response.json()
        # Extract headers from the first cart for consistency
        headers = ["id", "userId", "date", "products"]
        return headers, carts
    else:
        raise Exception(f"Failed to fetch carts. Status code: {response.status_code}")

# Task 3: Fetch extra data for each user
def fetch_user_details(users):
    '''
    Fetches detailed user information based on user IDs.

    This function iterates over a list of users, sending a GET request to the
    Fake Store API for each user's details. It collects the user data in a list
    and returns the headers and the data. The function
    implements a delay between requests to avoid overwhelming the server.

    Args:
        users (list): A list of users that the fetch_store_clients() function scraped.

    '''
    user_details = []
    for user in users:
        user_id = user[0]  # Assuming the first element is user ID
        url = f'https://fakestoreapi.com/users/{user_id}'
        response = requests.get(url)
        if response.status_code == 200:
            user_details.append(response.json())
        time.sleep(WAIT_TIME)  # Wait between requests

    # Extract headers from the first user details
    if user_details:
        headers = list(user_details[0].keys())
    else:
        headers = []

    return headers, user_details

# Task 4: Fetch product details for products in carts
def fetch_product_details(carts):
    '''
    Fetches detailed product information based on product IDs in user carts.

    This function gathers unique product IDs from all user carts, sends GET
    requests to the Fake Store API for each product's details, and returns
    the headers and product details. A delay is implemented between requests
    to ensure the server is not overloaded.

    Args:
        carts (list): A list of carts, where each cart contains product details.

    '''
    product_ids = set()
    for cart in carts:
        for product in cart['products']:
            product_ids.add(product['productId'])

    product_details = []
    for product_id in product_ids:
        url = f'https://fakestoreapi.com/products/{product_id}'
        response = requests.get(url)
        if response.status_code == 200:
            product_details.append(response.json())
        time.sleep(WAIT_TIME)  # Wait between requests

    # Extract headers from the first product details
    if product_details:
        headers = list(product_details[0].keys())
    else:
        headers = []

    return headers, product_details
