# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:45:43 2021

@author: Amritbaan-0001
"""

import unittest
from vendingMachine import Product, Denomination, Cart

class TestSum(unittest.TestCase):
    
    def setUp(self):
        self.product = Product()
        self.denomination = Denomination()
        self.cart  = Cart()
#        self.vending_machine = VendingMachine()

#        Product test cases
    def test_add_product(self):
        """
        Test that it is adding product
        """
        
        self.product.add_product("Coke",5)
        self.assertEqual(len(self.product.all_products), 1)
        self.assertEqual(self.product.all_products[0].name, "Coke")
        
    def test_remove_product(self):
        
        self.product.add_product("Coke",5)
        self.assertEqual(len(self.product.all_products), 1)
        
        self.product.remove_product("Coke")
        self.assertEqual(len(self.product.all_products), 0)
        
        
    def test_reset(self):
        self.product.add_product("Coke",5)
        self.product.add_product("Lays",50)

        self.assertEqual(len(self.product.all_products), 2)
        
        self.product.reset()
        self.assertEqual(len(self.product.all_products), 0)
        
#Denomination test case
    def test_add_denomination(self):
        """
        Test that it is adding product
        """
        
        self.denomination.add_denomination(5)
        self.assertEqual(len(self.denomination.all_denomination), 1)
        self.assertEqual(self.denomination.all_denomination[0], 5)
        
    def test_remove_denomination(self):
        
        self.denomination.add_denomination(9)
        self.assertEqual(len(self.denomination.all_denomination), 1)
        
        self.denomination.remove_denomination(9)
        self.assertEqual(len(self.denomination.all_denomination), 0)
        
        
    def test_reset_denomination(self):
        self.denomination.add_denomination(9)
        self.denomination.add_denomination(99)

        self.assertEqual(len(self.denomination.all_denomination), 2)
        
        self.denomination.reset()
        self.assertEqual(len(self.denomination.all_denomination), 0)
        
    def test_add_to_cart(self):
        
        prod = Product()
        
        prod.name = "Pepsi"
        prod.price = 55
        
        self.cart.add_to_cart(prod)
        self.assertEqual(self.cart.prod[0].name, "Pepsi")
        self.assertEqual(len(self.cart.prod), 1)
        
        self.assertEqual(self.cart.prod[0].price, 55)
        self.assertEqual(self.cart.cart_value, 55)
    
    def test_edit_cart(self):
        
        prod = Product()
        
        prod.name = "Pepsi"
        prod.price = 55
        
        self.cart.add_to_cart(prod)
        self.assertEqual(self.cart.prod[0].name, "Pepsi")
        self.assertEqual(len(self.cart.prod), 1)
        
        self.cart.edit_order(prod.name)
        
        self.assertEqual(len(self.cart.prod), 0)
        self.assertEqual(self.cart.cart_value, 0)
    
   
   
if __name__ == '__main__':
    unittest.main()

        
        
