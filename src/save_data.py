"""
Author: Ilias Adamidis
Date: 09 / 08 / 2024

Description: This module contains functions to process and save user and product data into Excel files.
It utilizes the pandas library to manage and analyze data in DataFrame format.

Tasks:
- Task 5: Combine user, client, and cart data into a single DataFrame and save to an Excel file.
- Task 6: Create a DataFrame for product details, calculate sales information, and save to an Excel file.
"""

import pandas as pd

# Task 5: Combine data into a DataFrame and save to Excel
def save_user_data_to_excel(client_data, client_headers, cart_data, cart_headers, user_details, user_headers):
    """
    Combines client, cart, and user data into a single DataFrame and saves it to an Excel file.

    Parameters:
        client_data (list): A list of client data records.
        client_headers (list): A list of headers for client data.
        cart_data (list): A list of cart data records.
        cart_headers (list): A list of headers for cart data.
        user_details (list): A list of user detail records.
        user_headers (list): A list of headers for user details.
    """
    # Create DataFrames
    df_clients = pd.DataFrame(client_data, columns=client_headers)
    df_carts = pd.DataFrame(cart_data, columns=cart_headers)
    df_users = pd.DataFrame(user_details, columns=user_headers)

    # Convert types if needed
    df_users['id'] = df_users['id'].astype(str)
    df_clients['ID'] = df_clients['ID'].astype(str)
    df_carts['userId'] = df_carts['userId'].astype(str)
    
    # Merge user and client data for user-based analysis
    df_combined = pd.merge(df_users, df_clients, left_on="id", right_on="ID", how="outer")
    
    # Calculate cart counts
    cart_counts = df_carts.groupby("userId")["id"].count().reset_index()
    cart_counts.columns = ['userId', 'cart_count']  # Rename columns to match for merge
    
    # Merge cart counts into combined DataFrame
    df_combined = pd.merge(df_combined, cart_counts, left_on="id", right_on="userId", how="left")
    
    # Fill NaN values in cart_count with 0
    df_combined['cart_count'] = df_combined['cart_count'].fillna(0)
    
    # Drop unnecessary columns
    df_combined = df_combined.drop(columns=['ID', 'userId'], errors='ignore')
    
    # Save to Excel
    df_combined.to_excel("combined_user_data.xlsx", index=False)

    print("User data saved to Excel file: combined_user_data.xlsx")


# Task 6: Create DataFrame for product details and save to Excel
def save_product_data_to_excel(cart_data, product_details, product_headers):
    """
    Creates a DataFrame for product details, computes total sales and unique user counts, 
    and saves the information to an Excel file.

    Parameters:
        cart_data (list): A list of cart data records containing product details.
        product_details (list): A list of product detail records.
        product_headers (list): A list of headers for product data.
    """
    # Create DataFrame for products
    df_products = pd.DataFrame(product_details, columns=product_headers)

    # Count how many items of each product have been sold in total
    product_sales_count = {}
    unique_users_count = {}

    for cart in cart_data:
        for product in cart['products']:
            product_id = product['productId']
            quantity = product['quantity']

            # Update total sold count
            if product_id in product_sales_count:
                product_sales_count[product_id] += quantity
            else:
                product_sales_count[product_id] = quantity

            # Update unique users count
            if product_id in unique_users_count:
                unique_users_count[product_id].add(cart['userId'])
            else:
                unique_users_count[product_id] = {cart['userId']}

    # Add the counts to the DataFrame
    df_products['total_sold'] = df_products['id'].map(product_sales_count)
    df_products['unique_users_count'] = df_products['id'].map(lambda x: len(unique_users_count.get(x, set())))

    # Save to Excel
    df_products.to_excel("product_data.xlsx", index=False)

    print("Product data saved to Excel file: product_data.xlsx")
