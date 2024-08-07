class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

class Transaction:
    def __init__(self, id, account_id, amount, type):
        self.id = id
        self.account_id = account_id
        self.amount = amount
        self.type = type
