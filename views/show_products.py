import database.database


def show_products_screen():
    print("#### Todos os produtos cadastrados ####")
    products = database.database.get_products()
    for product in products:
        print(product)