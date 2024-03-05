import home

def edit_product_screen_header(product_name):
    print("##### Edição de quantidade do produto: " + product_name + " #####")

def edit_product_screen( product_name, current_product_quantity ):
    edit_product_screen_header( product_name )
    print("Estoque atual: " + current_product_quantity )

    print("Você deseja adicionar ou remover o produto do estoque?")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Voltar")
    print("4 - Sair")
    choice = int()

    handle_choice( choice, product_name, current_product_quantity )


def handle_choice(choice, product_name, current_product_quantity):
    if choice == 1:
        new_product_quantity = add_product_screen(product_name, current_product_quantity)
    elif choice == 2:
        new_product_quantity = remove_product_screen(product_name, current_product_quantity)
    elif choice == 3:
        home.home_screen()
    elif choice == 4:
        exit()
    else:
        print("Erro opção inválida!")
        edit_product_screen(product_name, current_product_quantity)

def add_product_screen(product_name, current_product_quantity):
    print("Digite a quantidade do produto: " + product_name + " que você deseja adicionar: ")
    quantity = int()
    new_product_quantity = current_product_quantity + quantity




def remove_product_screen( product_name, current_product_quantity ):
    print("Digite a quantidade do produto: " + product_name + " que você deseja remover: ")
    quantity = int()
    return current_product_quantity - quantity

