from dotenv import load_dotenv

import views

if __name__ == '__main__':
    load_dotenv(".env")
    views.home.home_screen()
        

