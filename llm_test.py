import unittest
from bson.objectid import ObjectId

import io
import sys

import my_llm.llm_cli as llm_cli

class TestLLM(unittest.TestCase):
    def test_create_order(self):
        """
        Test that it can create an order
        """
        new_order_id = llm_cli.create_order("New From", "New To")
        new_order = llm_cli.orders.find_one({"_id":ObjectId(new_order_id)})
        self.assertIsNotNone(new_order, "Order should be created")
        llm_cli.orders.delete_one({"_id":ObjectId(new_order_id)})
    
    def test_take_available_order(self):
        """
        Test that it can take an order
        """
        new_order_id = llm_cli.create_order("New From", "New To")
        llm_cli.take_order(new_order_id)
        new_order = llm_cli.orders.find_one({"_id":ObjectId(new_order_id), "taken": True})
        self.assertIsNotNone(new_order, "Should not be None")
        llm_cli.orders.delete_one({"_id":ObjectId(new_order_id)})


    def test_take_unavailable_order(self):
        """
        Test that it cannot take an already taken order
        """
        new_order_id = llm_cli.create_order("New From", "New To")
        llm_cli.take_order(new_order_id)

        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        llm_cli.take_order(new_order_id)              # Call unchanged function.
        sys.stdout = sys.__stdout__ 

        self.assertEqual(capturedOutput.getvalue(), f"order \"{new_order_id}\" already taken\n", "Should say: order already taken")
        llm_cli.orders.delete_one({"_id":ObjectId(new_order_id)})
    
    def test_take_nonexisting_order(self):
        """
        Test that it cannot take a nonexisting order
        """                  
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        llm_cli.take_order('80aa1ac73ca20dec00e0890f')
        sys.stdout = sys.__stdout__ 

        self.assertEqual(capturedOutput.getvalue(), f"order \"80aa1ac73ca20dec00e0890f\" does not exist\n", "Should say: order does not exist")

if __name__ == '__main__':
    unittest.main()