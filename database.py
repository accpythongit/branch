import sqlite3

class Database:
    def __init__(self, db_uri):
        self.conn = sqlite3.connect(db_uri)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                balance REAL
            )''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                account_id INTEGER,
                amount REAL,
                type TEXT,
                FOREIGN KEY (account_id) REFERENCES accounts (id)
            )''')
