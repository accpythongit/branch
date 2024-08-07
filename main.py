from config import Config
from database import Database
from views import show_menu
from controllers import handle_choice

def main():
    config = Config()
    db = Database(config.DB_URI)
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice, db)

if __name__ == "__main__":
    main()
