"""
Author: Ilias Adamidis
Date: 09 / 08 / 2024

Description: This script processes product and user data from Excel files.
It updates the product data by splitting ratings into separate columns,
ensures data types are correct, and processes user data by splitting 
address information into separate columns and converting 'Last Login' 
to a datetime format. The updated data is then saved back to the respective Excel files.

This is an additional and optional script, it is not run in main with others. It can be used 
after main finishes and converts the excel files into more detailed by spliting columns.

"""

import pandas as pd

def process_product_data(file_path):
    """
    Process product data from an Excel file.

    This function performs the following operations:
    - Loads product data from the specified file.
    - Splits the rating into separate columns for rating and votes.
    - Ensures the correct data types for relevant columns.
    - Saves the updated product data back to the Excel file.

    Args:
        file_path (str): Path to the Excel file containing product data.
    """
    # Load the product data
    df_products = pd.read_excel(file_path)
    
    # Split rating into separate columns: rating and votes
    df_products['rating'] = df_products['rating'].apply(eval)
    df_products['votes'] = df_products['rating'].apply(lambda x: x['count'])
    df_products['rating'] = df_products['rating'].apply(lambda x: x['rate'])
    
    # Ensure data types are correct
    df_products['price'] = df_products['price'].astype(float)
    df_products['rating'] = df_products['rating'].astype(float)
    df_products['votes'] = df_products['votes'].astype(int)
    df_products['id'] = df_products['id'].astype(int)
    
    # Save the updated product data back to the Excel file
    df_products.to_excel(file_path, index=False)
    print(f"Product data updated and saved to {file_path}")

def process_user_data(file_path):
    """
    Process user data from an Excel file.

    This function performs the following operations:
    - Loads user data from the specified file.
    - Splits address information into separate columns.
    - Converts the 'Last Login' field to a datetime format.
    - Saves the updated user data back to the Excel file.

    Args:
        file_path (str): Path to the Excel file containing user data.
    """
    # Load the user data
    df_users = pd.read_excel(file_path)
    
    # Split address into separate columns
    df_users['address'] = df_users['address'].apply(eval)
    df_users['Address-latitude'] = df_users['address'].apply(lambda x: float(x['geolocation']['lat']))
    df_users['Address-longitude'] = df_users['address'].apply(lambda x: float(x['geolocation']['long']))
    df_users['Address-city'] = df_users['address'].apply(lambda x: x['city'])
    df_users['city-street'] = df_users['address'].apply(lambda x: x['street'])
    df_users['street-number'] = df_users['address'].apply(lambda x: x['number'])
    df_users['Address-zipcode'] = df_users['address'].apply(lambda x: x['zipcode'])
    df_users['id'] = df_users['id'].astype(int)
    # Drop the original address column
    df_users.drop(columns=['address'], inplace=True)
    
    # Split name into full name
    df_users['name'] = df_users['name'].apply(eval)
    df_users['full_name'] = df_users['name'].apply(lambda x: f"{x['firstname']} {x['lastname']}")
    
    # Drop the original name column
    df_users.drop(columns=['name'], inplace=True)
    # Convert 'Last Login' to datetime
    df_users['Last Login'] = pd.to_datetime(df_users['Last Login'])
    
    # Save the updated user data back to the Excel file
    df_users.to_excel(file_path, index=False)
    print(f"User data updated and saved to {file_path}")

if __name__ == "__main__":
    product_file = 'product_data.xlsx'  # Path to your product data file
    user_file = 'combined_user_data.xlsx'  # Path to your user data file

    process_product_data(product_file)
    process_user_data(user_file)
