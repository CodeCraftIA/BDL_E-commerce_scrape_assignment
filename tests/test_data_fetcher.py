"""
Author: Ilias Adamidis
Date: 09 / 08 / 2024

Description: This module contains unit tests for the data fetching functions defined in the 
data_fetcher module. Each test class corresponds to a function being tested and ensures 
that the returned data adheres to the expected structure and format.
"""

import unittest
from src.data_fetcher import fetch_store_clients, fetch_user_carts, fetch_user_details, fetch_product_details 
class TestFetchStoreClients(unittest.TestCase):
    """
    Test suite for the fetch_store_clients function.
    
    """
    def test_fetch_store_clients(self):
        """
        Test the fetch_store_clients function to ensure it returns valid data.
        
        """
        # Run the function to fetch store clients
        headers, clients = fetch_store_clients()

        # Check that headers and clients are not empty
        self.assertIsNotNone(headers)
        self.assertGreater(len(headers), 0)
        self.assertIsNotNone(clients)
        self.assertGreater(len(clients), 0)

        # Check that the headers contain expected columns
        expected_columns = ["ID", "Age", "Occupation", "Account Status", "Last Login", "Account Balance"]
        for column in expected_columns:
            self.assertIn(column, headers)

        # Check that clients contain data in the expected format
        for client in clients:
            self.assertEqual(len(client), len(headers))  # Each client row should have the same number of columns as headers


class TestFetchUserCarts(unittest.TestCase):
    """
    Test suite for the fetch_user_carts function.
    
    """
    def test_fetch_user_carts(self):
        """
        Test the fetch_user_carts function to ensure it returns valid data.
       
        """
        # Run the function to fetch user carts
        headers, carts = fetch_user_carts()

        # Check that headers and carts are not empty
        self.assertIsNotNone(headers)
        self.assertGreater(len(headers), 0)
        self.assertIsNotNone(carts)
        self.assertGreater(len(carts), 0)

        # Check that the headers contain expected columns
        expected_columns = ["id", "userId", "date", "products"]
        for column in expected_columns:
            self.assertIn(column, headers)

        # Check that carts contain data in the expected format
        for cart in carts:
            self.assertEqual(len(cart), len(headers) + 1)  # Each cart should have the same number of columns as headers


class TestFetchUserDetails(unittest.TestCase):
    """
    Test suite for the fetch_user_details function.
    
    """
    def test_fetch_user_details(self):
        """
        Test the fetch_user_details function to ensure it returns valid data.
        
        """
        # Sample user data for testing
        users = [[1], [2], [3]]  # small sample testing
        
        # Run the function to fetch user details
        headers, user_details = fetch_user_details(users)

        # Check that headers and user details are not empty
        self.assertIsNotNone(headers)
        self.assertGreater(len(headers), 0)
        self.assertIsNotNone(user_details)
        self.assertGreater(len(user_details), 0)

        # Check that user details contain data in the expected format
        for user in user_details:
            self.assertIn("id", user)  # Check for specific expected fields
            self.assertIn("name", user)


class TestFetchProductDetails(unittest.TestCase):
    """
    Test suite for the fetch_product_details function.
    
    """
    def test_fetch_product_details(self):
        """
        Test the fetch_product_details function to ensure it returns valid data.
        
        """
        # Sample carts data for testing
        carts = [
            {'products': [{'productId': 1}, {'productId': 2}]},
            {'products': [{'productId': 3}]}
        ]
        
        # Run the function to fetch product details
        headers, product_details = fetch_product_details(carts)

        # Check that headers and product details are not empty
        self.assertIsNotNone(headers)
        self.assertGreater(len(headers), 0)
        self.assertIsNotNone(product_details)
        self.assertGreater(len(product_details), 0)

        # Check that product details contain data in the expected format
        for product in product_details:
            self.assertIn("id", product)  # Check for specific expected fields
            self.assertIn("title", product)

if __name__ == '__main__':
    unittest.main()
