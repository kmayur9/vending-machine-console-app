# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:40:13 2021

@author: Mayur
"""
"""
Product class has all functinality related to adding/removing/displaying products
"""
class Product:
    name  = ""
    price = 0
    def __init__(self):
        self.all_products = []
        
    def reset(self):
        self.all_products.clear()
        
    def add_product(self,name, price):
       
        new_prod = Product()
        new_prod.name = name
        new_prod.price = price
        
        self.all_products.append(new_prod)  
    
    def remove_product(self,prod):
        
        for item in self.all_products:
            if(item.name == prod):
                self.all_products.remove(item)
    
    def display_all_products(self):
        print("List of all available products:\n*********************************")
        for item in self.all_products:
            print(item.name)
        
        print("******************************")


"""
Denomination class has all functinality related to adding/removing/displaying products
"""
class Denomination:
    def __init__(self):
        self.all_denomination = []
        
    def add_denomination(self, denom):
        self.all_denomination.append(denom)
    
    def remove_denomination(self, denom):
        
        for item in self.all_denomination:
            if(item==denom):
                self.all_denomination.remove(item)        
    
    def reset(self):
        self.all_denomination.clear()
    
    def display_all_denomination(self):
       print("Below are all Available denominations: \n")
       for item in self.all_denomination:
           print (item)
           print("\n")

      
"""
Cart class has all functinality related to adding/removing/displaying products in the cart, paying/placing/caceling order
"""
class Cart:   
    def __init__(self):
        self.prod = []
        self.cart_value = 0
        
    def add_to_cart(self, item):
        self.prod.append(item)
        self.cart_value = self.cart_value + item.price

       
    def edit_order(self, remove_prod):
        for item in self.prod:
            if(item.name == remove_prod):
                self.prod.remove(item)      
                self.cart_value = self.cart_value - item.price
                print("Product removed successfully")
                break
           
    
    def pay_order(self, denomination): 
        try:
            print("Below is the Your Cart")
            cash_collected = 0
            
            if len(self.prod)>0:
                for i, x in enumerate(self.prod):
                    print(x.name + "\t")
                print("Total cart value is \t", self.cart_value)                
            else:
                print("Cart is empty")
                return False
            
            if len(denomination.all_denomination)>0:
                while True:
                    denomination.display_all_denomination()
                    print("Type denominations you wish to pay cash in \n")
                    selected_denomin = float(input())
                    
                    
                    for i, x in enumerate(denomination.all_denomination):
                        if selected_denomin == x:
                            if cash_collected < cash_collected + x:
                                cash_collected = cash_collected + x
                                print("Total cash collected is ",cash_collected)
                                
                                if cash_collected == self.cart_value:
                                    cancel_place = int(input("1. Cancel order and take refund \n2. Confirm Order\n"))
                                    
                                    if cancel_place == 1:
                                        self.cancel_order()
                                        return False
                                    elif cancel_place == 2:
                                        self.place_order()                                
                                        return False
                                    else:
                                        return False
                                break
                            else:
                                print("Money paid is more than Cart value, pls select denominations correctly.")
                                
                
                else:
                    print("No Denmonations set, contact admin")
                    return False
        except:
            print("Some error occured, please retry")
    
    def cancel_order(self):
        print("Your order is cancelled Successfully, please collect your cash of \t", self.cart_value)
        return False
    
    
    def place_order(self):
        print("Thanks for placing order with us. Don't forget to collect your Food...........")        
        return False
    

"""
VendingMachine class is the main class which consumes all the classes like Product/Cart/Denomination
"""
class VendingMachine:
        
    def __init__(self):
        self.product = Product()
        self.denomination = Denomination()
        self.cart  = Cart()
        
                
        while True:   
            try:
                print("***************Welcome to Awesome Vending Machine****************")
                
                user_or_admin = int(input("Select your input:\n 1. Place Order\n 2. Admin Login \n"))
                
                if user_or_admin == 1:
                    self.user_flow()
                    pass
                elif user_or_admin == 2:
                    self.admin_flow()
                else:
                    print("Invalid input, exiting..")
            except:
                print("Some error occured, please retry")
 

    def reset_machine(self):
        self.product.reset()
        self.denomination.reset()
        
    def admin_flow(self):       
        while True:
            try:
                admin_inp = int(input("Enter Your Choice\n1. Add Product\n2. Add Denomination \n3. Reset Machine  \n4. Remove Denomination \n5. Remove Product   \n6. Enter any key to go to main menu\n"))
                
                if admin_inp == 1:
                    name = input("Enter Product name\t")
                    price = float(input("Enter Product price \t"))
                    self.product.add_product(name, price)
                elif admin_inp == 2:
                    denom = float(input("Enter Denomination\t"))
                    self.denomination.add_denomination(denom)
                elif admin_inp == 3:
                    self.reset()
                elif admin_inp == 4:
                    self.display_all_denomination()
                    print("Type denomination to be deleted\n")
                    
                    denom = float(input("Enter Denomination\t"))
                    self.denomination.remove_denomination(denom)
                elif admin_inp == 5:
                    self.display_all_products()
                    print("Type product to be deleted\n")
                    
                    prod = input("Enter Product to be deleted \t")
                    self.product.remove_product(prod)
                else:
                    return False
            except:
                print("Some unexpected error occured, please conatct admin for any quries")
            
    
    def user_flow(self):  
        self.cart = Cart()
        while True:
            try:
                if len(self.product.all_products)==0:
                    print("No products available, contact admin...")
                    return False
                          
                self.product.display_all_products()
                
                selected_prod = input("\n 1. Type Name of product you wish to select\n 2. Type pay to checkout\n 3. Type exit to got to main menu \n 4. Type remove for removing product from cart \n")
                
                if selected_prod=="exit":
                    self.in_sub_menu = False
                    return False
    
                if selected_prod=="pay":
                    self.cart.pay_order(self.denomination)
                    return False
                
                if selected_prod=="remove":
                    remove_prod = input("Type name of product you wish to remove \n")
                    
                    self.cart.edit_order(remove_prod)
                    
                    
    
                for i, x in enumerate(self.product.all_products):
                    if selected_prod == x.name:
                        self.cart.add_to_cart(x)
                    else:
                        print("Invalid input\n")
            except:
                print("Some unexpected error occured, please conatct admin for any quries")

if __name__ == '__main__':    
    v = VendingMachine()




        
            
            


