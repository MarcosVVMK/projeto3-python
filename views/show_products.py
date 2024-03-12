import database.database


def show_products_screen():
    print("#### Todos os produtos cadastrados ####")
    products = database.database.get_products()
    count = 1
    for product in products:
        format_product(product, count)
        count = count + 1

def format_product(product, count):
    print("________________________________________________________")
    print("#### Produto cadastrado: " + str(count) + " #### ")
    print("| Nome do produto: " + product[1])
    print("| Preço do produto: R$ {:,.2f}".format(product[2]))
    print("| Quantitdade do produto em estoque: " + str(product[3]))
    print("| Código de Barras EAN: " + str(product[4]))
    print("| Categoria do produto: " + str(product[5]))
    print("________________________________________________________")