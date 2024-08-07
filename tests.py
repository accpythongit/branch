import unittest
from utils import validate_amount, validate_account_id
from database import Database
from config import Config

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.db = Database(Config.DB_URI)

    def test_validate_amount(self):
        self.assertTrue(validate_amount(100))
        self.assertFalse(validate_amount(-1))

    def test_validate_account_id(self):
        self.assertFalse(validate_account_id(1, self.db))
        self.db.conn.execute("INSERT INTO accounts (id, name, balance) VALUES (?, ?, ?)", (1, "Test Account", 100))
        self.assertTrue(validate_account_id(1, self.db))

if __name__ == "__main__":
    unittest.main()
