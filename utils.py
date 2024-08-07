def validate_amount(amount):
    return amount > 0

def validate_account_id(account_id, db):
    with db.conn:
        result = db.conn.execute("SELECT id FROM accounts WHERE id = ?", (account_id,)).fetchone()
    return result is not None
