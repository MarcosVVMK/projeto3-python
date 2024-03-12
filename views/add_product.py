import os

import emoji

import database.database
import views.home


def add_product_header_screen():
    print("#### Adição de produto ####")

def add_product_screen():
    product = {}

    add_product_header_screen()

    print("Digite o nome do produto: ")
    product['name'] = input()

    database.database.verify_if_product_exist( product['name'] )

    print("Digite o preço do produto: ")
    product['price'] = float(input())

    print("Digite a quantidade do produto: ")
    product['quantity'] = int(input())

    print("Digite o código EAN do produto: ")
    product['ean'] = input()

    print("Digite a categoria do produto: ")
    product['category'] = input()

    os.system('clear')

    database.database.add_product( product )


def add_more_product_screen():
    add_product_header_screen()
    print(emoji.emojize("Produto Adicionado com sucesso! :check_mark_button:  "))
    print("Deseja adicionar mais produtos?")
    print(emoji.emojize("1 :right_arrow: Sim"))
    print(emoji.emojize("2 :left_arrow: Voltar"))
    option = int(input())

    os.system('clear')

    if option == 1:
        add_product_screen()
    elif option == 2:
        views.home.home_screen()
    else:
        exit()

def product_already_exists_screen():

    os.system('clear')

    print("Produto já existe!")
    add_product_screen()