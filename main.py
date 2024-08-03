import views.home
import database.create_product_table
import time

def main():

    database.create_product_table.run()
   
    views.home.home_screen()

    # Manter o contêiner em execução
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
