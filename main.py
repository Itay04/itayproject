import ipdb

from models import display_menu, Productlist
from util import *


def show_main_products():
    main_product_class = load("products.data")
    for product in main_product_class.show_all_products:
        print(product)


all_products_in_store = load("products.data")
for product in all_products_in_store.my_list:
    print(product)

a = Productlist()

display_menu(a)
#search product in shop
all_products_in_store.search_product()
#delete produc from shop
all_products_in_store.delete_a_product()

# add_to_customer_list
all_products_in_store.add_to_customer_list()
#remove from customer list
all_products_in_store.delete_a_product_customer()

