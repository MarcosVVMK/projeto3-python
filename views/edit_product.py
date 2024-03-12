import os

import emoji

import database.database
import home

def edit_product_screen_header(product_name, current_product_data):
    print("##### Edição de quantidade do produto: " + product_name + " #####")
    print("Estoque atual: " + str(current_product_data["quantity"]))

def edit_product_screen_selection():
    print("#### Tela de edição de produto ####")
    print(emoji.emojize("Digite o nome do produto que deseja editar: :magnifying_glass_tilted_right: "))
    product_name = input()

    current_product_data = database.database.get_product_quantity_by_name( product_name )

    os.system('clear')

    edit_product_screen( product_name, current_product_data )

def edit_product_screen( product_name, current_product_data ):

    edit_product_screen_header( product_name, current_product_data )

    print("Você deseja adicionar ou remover o produto do estoque?")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Voltar")
    print("4 - Sair")
    choice = int(input())

    os.system("clear")

    if choice == 1:

        new_product_data = add_product_screen(product_name, current_product_data)

        database.database.edit_product(new_product_data)

    elif choice == 2:

        new_product_data = remove_product_screen(product_name, current_product_data)

        database.database.edit_product(new_product_data)

    elif choice == 3:

        home.home_screen()

    elif choice == 4:

        exit()

    else:
        print("Erro opção inválida!")
        edit_product_screen(product_name, current_product_data)


def add_product_screen(product_name, current_product_data):

    edit_product_screen_header(product_name, current_product_data)
    print("Digite a quantidade do produto: " + product_name + " que você deseja adicionar: ")
    quantity = int(input())

    current_product_data['quantity'] = current_product_data['quantity'] + quantity

    return current_product_data


def remove_product_screen( product_name, current_product_data ):

    edit_product_screen_header(product_name, current_product_data)
    print("Digite a quantidade do produto: " + product_name + " que você deseja remover: ")
    quantity = int(input())

    current_product_data['quantity'] = current_product_data['quantity'] - quantity

    return  current_product_data

