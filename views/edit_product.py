import os
import emoji
import database.database
import home
import views


def edit_product_screen_header(product_name, current_product_data):
    print("##### Edição de quantidade do produto: " + product_name + " #####")
    print("Estoque atual: " + str(current_product_data["quantity"]))

def edit_product_screen_selection():
    print("#### Tela de edição de produto ####")
    print(emoji.emojize("Digite o nome do produto que deseja editar: :magnifying_glass_tilted_right: "))
    product_name = input()

    current_product_data = database.database.get_product_quantity_by_name( product_name )

    os.system('clear')

    if current_product_data:
        return edit_product_screen( product_name, current_product_data )
    else:
        return product_not_found_screen()


def product_not_found_screen():
    print("Produto não encontrado")
    print(emoji.emojize("1 :left_arrow: Voltar para edição do produto"))
    print(emoji.emojize("2 :left_arrow: Voltar parao Menu Principal"))
    print(emoji.emojize("3 :cross_mark:  Sair"))
    choice = int(input())

    os.system('clear')

    if choice == 1:
        return edit_product_screen_selection()
    elif choice == 2:
        return views.home.home_screen()
    elif choice == 3:
        exit()
    else:
        exit()

def after_edit_product_screen():
    print("Deseja editar mais produtos?")
    print(emoji.emojize("1 :right_arrow: Sim"))
    print(emoji.emojize("2 :left_arrow: Voltar"))
    option = int(input())

    os.system('clear')

    if option == 1:
        edit_product_screen_selection()
    elif option == 2:
        views.home.home_screen()
    else:
        exit()

def edit_product_screen( product_name, current_product_data ):

    edit_product_screen_header( product_name, current_product_data )

    print("Você deseja adicionar ou remover o produto do estoque?")
    print(emoji.emojize("1 :right_arrow: Adicionar"))
    print(emoji.emojize("2 :right_arrow: Remover"))
    print(emoji.emojize("3 :left_arrow: Voltar"))
    print(emoji.emojize("4 :cross_mark:  Sair"))

    choice = int(input())

    os.system("clear")

    if choice == 1:

        new_product_data = add_product_screen(product_name, current_product_data)

        database.database.edit_product(new_product_data)
        return views.edit_product.after_edit_product_screen()

    elif choice == 2:

        new_product_data = remove_product_screen(product_name, current_product_data)

        database.database.edit_product(new_product_data)
        return views.edit_product.after_edit_product_screen()

    elif choice == 3:

        home.home_screen()

    elif choice == 4:

        exit()

    else:
        print(emoji.emojize(":cross_mark: Erro opção inválida! :cross_mark:"))
        edit_product_screen(product_name, current_product_data)


def add_product_screen(product_name, current_product_data):

    edit_product_screen_header(product_name, current_product_data)
    print("Digite a quantidade do produto: " + product_name + " que você deseja adicionar: ")
    quantity = int(input())

    current_product_data['quantity'] = current_product_data['quantity'] + quantity

    print(emoji.emojize("Produto adicionado com sucesso! :check_mark_button: "))
    print("Estoque atual: " + str(current_product_data['quantity']))

    return current_product_data


def remove_product_screen( product_name, current_product_data ):

    edit_product_screen_header(product_name, current_product_data)
    print("Digite a quantidade do produto: " + product_name + " que você deseja remover: ")
    quantity = int(input())

    current_product_data['quantity'] = current_product_data['quantity'] - quantity

    print(emoji.emojize("Produto removido com sucesso! :check_mark_button: "))
    print("Estoque atual: " + str(current_product_data['quantity']))

    return current_product_data


