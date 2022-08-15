import pickle



def save(obj_to_save, filename):
    with open(filename, "wb") as myfile:
        pickle.dump(obj_to_save, myfile)


def load(filename):
    with open(filename, "rb") as myfile:
        return pickle.load(myfile)

def read_products_file():
    from itay_shop_project.models import Product
    all_products = []
    with open("products.csv") as products_file:
        products_file.readline()
        for line in products_file:
            temp_list = line.split(",")
            product = Product(inventory=int(temp_list[0]),
                              product_name=temp_list[1],
                              unit=int(temp_list[2]),
                              price=int(temp_list[3]))
            all_products.append(product)
    return all_products

def first_time_read_data():
    are_you_sure = input("are_you_sure? yes/no")
    if are_you_sure != "yes":
        return
    from itay_shop_project.models import Productlist
    all_products = read_products_file()
    main_product_class = Productlist()
    main_product_class.my_list = all_products
    save(main_product_class, "products.data")
    print("saved file!")

if __name__ == "__main__":
    first_time_read_data()
