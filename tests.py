import db

USER_ID = 69

ACCOUNT_ID = db.create_new_account(USER_ID)
db.add_new_income(ACCOUNT_ID, 100.0)
db.add_new_outcome(ACCOUNT_ID, 50.0)
db.add_new_transaction(ACCOUNT_ID, 96, 20.0)
db.add_new_transaction(96, ACCOUNT_ID, 69.0)
print(db.get_account_balance(ACCOUNT_ID))
