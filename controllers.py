from models import Account, Transaction

def handle_choice(choice, db):
    if choice == '1':
        add_account(db)
    elif choice == '2':
        view_accounts(db)
    elif choice == '3':
        add_transaction(db)
    elif choice == '4':
        view_transactions(db)
    elif choice == '5':
        exit()

def add_account(db):
    name = input("Enter account name: ")
    balance = float(input("Enter initial balance: "))
    with db.conn:
        db.conn.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))

def view_accounts(db):
    with db.conn:
        accounts = db.conn.execute("SELECT * FROM accounts").fetchall()
        for account in accounts:
            print(account)

def add_transaction(db):
    account_id = int(input("Enter account ID: "))
    amount = float(input("Enter amount: "))
    type = input("Enter type (debit/credit): ")
    with db.conn:
        db.conn.execute("INSERT INTO transactions (account_id, amount, type) VALUES (?, ?, ?)", (account_id, amount, type))

def view_transactions(db):
    with db.conn:
        transactions = db.conn.execute("SELECT * FROM transactions").fetchall()
        for transaction in transactions:
            print(transaction)
