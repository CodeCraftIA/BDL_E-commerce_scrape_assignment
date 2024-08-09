"""
Author: Ilias Adamidis
Date: 09 / 08 / 2024

Description: This script orchestrates the fetching of store clients, user carts, user details, and product details,
then saves the combined data into Excel files. It coordinates tasks by calling functions from data_fetcher and save_data modules.

Tasks:
- Task 1: Fetch store clients using Selenium.
- Task 2: Fetch all carts for users via API.
- Task 3: Fetch additional data for each user.
- Task 4: Fetch product details for products in the carts.
- Task 5: Save combined user data to an Excel file.
- Task 6: Save product data to an Excel file.
"""


from data_fetcher import fetch_store_clients, fetch_user_carts, fetch_user_details, fetch_product_details
from save_data import save_user_data_to_excel, save_product_data_to_excel
import time

# Constants
WAIT_TIME = 3

def main():
    """
    Main function to orchestrate the data fetching and saving process.

    It performs the following tasks:
    - Fetches store client data.
    - Fetches user cart data.
    - Fetches additional details for users.
    - Fetches product details based on user carts.
    - Saves the aggregated user data into an Excel file.
    - Saves product data into another Excel file.
    """
    # Task 1: Fetch store clients
    client_headers, store_clients = fetch_store_clients()
    print("Task 1 complited, Found data: ", store_clients)
    time.sleep(WAIT_TIME)

    # Task 2: Fetch all carts for users
    cart_headers, user_carts = fetch_user_carts()
    print("")
    print("Task 2 complited, Found data: ", user_carts)
    time.sleep(WAIT_TIME)

    # Task 3: Fetch extra data for each user
    user_headers, user_details = fetch_user_details(store_clients)
    print("")
    print("Task 3 complited, Found data: ", user_details)
    time.sleep(WAIT_TIME)

    # Task 4: Fetch product details for products in carts
    product_headers, product_details = fetch_product_details(user_carts)
    print("")
    print("Task 4 complited, Found data: ", product_details)
    time.sleep(WAIT_TIME)

    # Task 5: Save user data to Excel
    save_user_data_to_excel(store_clients, client_headers, user_carts, cart_headers, user_details, user_headers)

    # Task 6: Save product data to Excel
    save_product_data_to_excel(user_carts, product_details, product_headers)

    print("Data gathering and processing complete. Files saved as 'combined_user_data.xlsx' and 'product_data.xlsx'.")

if __name__ == "__main__":
    main()

