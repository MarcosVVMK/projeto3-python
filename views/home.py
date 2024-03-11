import os

import views.add_product
import views.edit_product
import views.show_products


def home_screen():
    print("#### Bem Vindo ao Sistema de Controle de Estoque! ####")
    print("Escolha uma das opçoes abaixo:")
    print("1 - Adicionar produto")
    print("2 - Editar produto")
    print("3 - Mostrar todos os produtos")
    print("0 - Fechar o programa")
    option = int(input())

    os.system('clear')

    if option == 1:
        views.add_product.add_product_screen()
    elif option == 2:
        views.edit_product.edit_product_screen_selection()
    elif option == 3:
        views.show_products.show_products_screen()
    elif option == 0:
        exit()