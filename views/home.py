import os
import emoji
import views

def home_screen():
    print("#### Bem Vindo ao Sistema de Controle de Estoque! ####")
    print("Escolha uma das opçoes abaixo:")
    print(emoji.emojize("1 :right_arrow: Adicionar produto"))
    print(emoji.emojize("2 :right_arrow: Editar produto"))
    print(emoji.emojize("3 :right_arrow: Mostrar todos os produtos"))
    print(emoji.emojize("0 :cross_mark:  Fechar o programa"))
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