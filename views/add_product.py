from array import array


def add_product_screen():
    product = {}

    print("#### Adição de produto ####")

    print("Digite o nome do produto: ")
    product['name'] = input()

    print("Digite o preço do produto: ")
    product['price'] = float(input())

    print("Digite a quantidade do produto: ")
    product['quantity'] = int(input())

    print("Digite o código EAN do produto: ")
    product['ean'] = input()

    print("Digite a categoria do produto: ")
    product['category'] = input()


    return product
