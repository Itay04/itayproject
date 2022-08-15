from util import load, save, first_time_read_data
import ipdb


class Product:
    def __init__(self, inventory, product_name, unit, price):
        self.inventory = inventory
        self.product_name = product_name
        self.unit = unit
        self.price = price

    def __str__(self):
        return f"{self.inventory}, {self.product_name}, {self.unit}, {self.price}"


class Productlist:
    def __init__(self):
        self.my_list = []
        self.customer_list = []

    def search_product(self):
        search_str = input("enter search name")
        for product in self.my_list:
            if search_str in product.product_name:
                print(product)

    def add_product(self):
        product_list = input("enter product name to add to list: ")
        for product in self.my_list:
            if product_list in product.product_name:
                self.my_list.append(product)
                print(self.my_list)


    def add_to_customer_list(self):
        customer_p_list = input("enter product name to add to list: ")
        for product in self.my_list:
            if customer_p_list in product.product_name:
                self.customer_list.append(product)
                print(self.customer_list)

    def delete_a_product_customer(self):
        print(self.customer_list)
        delete_product_customer = input("enter the name of the product you want to delete")
        are_you_sure_cas_delete = input("are_you_sure_to_delete_from_customer_list? yes/no")
        if are_you_sure_cas_delete != "yes":
            print(("not deleted"))
        else:
            for product in self.customer_list:
                if delete_product_customer in product.product_name:
                    self.customer_list.remove(product)
                    save(self.customer_list, "products.data")
                    print(self.customer_list)
                    return

    def delete_a_product(self):
        print(self.my_list)
        delete_product = input("enter the name of the product you want to delete")
        are_you_sure_to_delete = input("are_you_sure_to_delete? yes/no")
        if are_you_sure_to_delete != "yes":
            print(("not deleted"))
        else:
            for product in self.my_list:
                if delete_product in product.product_name:
                    self.my_list.remove(product)
                    save(self.my_list, "products.data")
                    print(self.my_list)
                    return


## decreases the number inventory called each time



def display_menu(a):
    while True:
        print("\nchoose_action: \nto show products:1 \nto add product to shop:2 \n"
            "to add product to customer list:3 \n"
            "to search product click 4 \n"
            "to delete product from shop:5 \n"
            "to delete product from customer list:6 \n"
            "to quit press 7")

        choose_action = input()

        if choose_action == "1":
            blah = a.my_list()
            print(blah)
            continue

        elif choose_action == "2":
            b = a.add_product()
            print(b)
            continue

        elif choose_action == "3":
            return a.add_to_customer_list()
        elif choose_action == "4":
            return a.search_product()
        elif choose_action == "5":
            return a.delete_a_product()
        elif choose_action == "6":
            return a.delete_a_product_customer()
        elif choose_action == "7":
            break
        else:
            print("wrong choice please try again")
            continue




# class CashRegister:
#
#     def decrement_inventory(self):
#         if self.inventory > 0:
#             self.inventory -= 1
#         else:
#             self.inventory = 0
#
#     def __int__(self, purchase_item):
#         self.purchase_item = []
#         self.purchase_list = []
#
#     def purchase_item(self, product_name, inventory):
#         self.purchase_item.append(product_name)
#         return self.decrement_inventory(inventory)
#
#     def get_total(self, price, total):
#         total += price
#         return total
#
#     def show_items(customer_list):
#         for product in customer_list:
#             print(product.get_product())
#             print(product.get_inventory())
#             print(product.get_price())
#
#     def clear(self):
#         self.purchase_list[:] = []
#
#
# ##### adds an item to cash register.
# ####price = the price of the item
# def add_item_cashir(self):
#     self._item_count = self._item_count + 1
#     self._total_price = self._total_price + self.price
#
#     # gets price of all items in current sale
#     ##### return total price
#     def get_total(self):
#         return self._total_price
#
#     ##### gets the number of item in the current sale
#     def get_cout(self):
#         return self._item_count
#
#     #### clear the item count and the total
#     def clear(self):
#         self._item_count = 0
#         self._total_price = 0.0
