import sqlite3
import exceptions


def is_user_exists_in_config(user_id: int) -> bool:
    """
    Check whether user exists in config
    :param user_id:
    :return: bool
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    res = cursor.execute(
        f"SELECT * FROM user_config WHERE user_id={user_id}").fetchall()
    connection.close()
    return len(res) != 0


def set_config(user_id: int, language: str = "en", theme: str = "default") -> dict:
    """
    Set config data for user (if user exists - update them)
    :param user_id:
    :param language:
    :param theme:
    :return: nothing
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    if language not in exceptions.LANGUAGES:
        return {"msg": "Invalid language"}
    if theme not in exceptions.THEMES:
        return {"msg": "Invalid theme"}
    if is_user_exists_in_config(user_id):
        query = f'UPDATE user_config SET language="{language}", theme="{theme}" WHERE user_id={user_id}'
    else:
        query = f"INSERT INTO user_config VALUES({user_id}, '{language}', '{theme}')"
    cursor.execute(query)
    connection.commit()
    connection.close()
    return {"msg": "Success"}


def set_language(user_id: int, language: str = "en") -> dict:
    """
    sets language for user (if user does not exist - creates new user with theme=default)
    :param user_id:
    :param language:
    :return: nothing
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    if not is_user_exists_in_config(user_id):
        return {"msg": "User not found"}
    if language not in exceptions.LANGUAGES:
        return {"msg": "Invalid language"}
    if is_user_exists_in_config(user_id):
        query = f"UPDATE user_config SET language='{language}' WHERE user_id={user_id}"
    else:
        query = f"INSERT INTO user_config VALUES({user_id}, {language}, {exceptions.THEME_DEFAULT})"
    cursor.execute(query)
    connection.commit()
    connection.close()
    return {"msg": "Success"}


def set_theme(user_id: int, theme: str = "default") -> dict:
    """
    sets theme for user (if user does not exist - creates new user with language=en)
    :param user_id:
    :param theme:
    :return:
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    if not is_user_exists_in_config(user_id):
        return {"msg": "User not found"}
    if theme not in exceptions.THEMES:
        return {"msg": "Invalid theme"}
    if is_user_exists_in_config(user_id):
        query = f"UPDATE user_config SET theme='{theme}' WHERE user_id={user_id}"
    else:
        query = f'INSERT INTO user_config VALUES({user_id}, "{exceptions.LANGUAGE_EN}", "{exceptions.THEME_DEFAULT}")'
    cursor.execute(query)
    connection.commit()
    connection.close()
    return {"msg": "Success"}


def get_user_config(user_id: int) -> dict:
    """
    Get user config object
    :param user_id:
    :return: object {
        "language": "VALUE",
        "theme": "VALUE" }
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    res = cursor.execute(
        f"SELECT * FROM user_config WHERE user_id={user_id}").fetchall()
    connection.close()
    if len(res) == 0:
        return {"msg": "User not found"}
    return {
        "language": res[0][1],
        "theme": res[0][2]
    }


def create_new_account(user_id: int, name: str = "Account",
                       description: str = "Description") -> int:
    """
    Creates new account attached to user_id
    :param user_id:
    :param name:
    :param description:
    :return: new account id
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute(
        f"INSERT INTO accounts VALUES(NULL, {user_id}, '{name}', '{description}')")
    connection.commit()
    res = cursor.execute(f"SELECT max(account_id) FROM accounts").fetchone()[0]
    connection.close()
    return res


def get_account_list(user_id: int) -> list:
    """
    Get account list by user id
    :param user_id:
    :return: list of accounts [account_id, user_id, name, description]
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    res = cursor.execute(f"SELECT * FROM accounts WHERE user_id={user_id}").fetchall()
    connection.close()
    return res


def add_new_income(account_id: int, sum: float, name: str = "Income", description: str = "Description",
                   category: str = "Category") -> None:
    """
    Add new income to database
    :param account_id:
    :param sum:
    :param name:
    :param description:
    :param category:
    :return:
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO incomes VALUES({account_id}, {sum}, '{name}', '{description}', '{category}')")
    connection.commit()
    connection.close()


def add_new_outcome(account_id: int, sum: float, name: str = "Income", description: str = "Description",
                    category: str = "Category") -> None:
    """
    Add new outcome to database
    :param account_id:
    :param sum:
    :param name:
    :param description:
    :param category:
    :return:
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO outcomes VALUES({account_id}, {sum}, '{name}', '{description}', '{category}')")
    connection.commit()
    connection.close()


def add_new_transaction(from_account_id: int, to_account_id: int, sum: float, description: str = "Description") -> None:
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO transactions VALUES({from_account_id}, {to_account_id}, {sum}, '{description}')")
    connection.commit()
    connection.close()


def get_account_balance(account_id: int) -> int:
    """
    Calculates account balance based on transactions, outcomes and incomes attached to it
    :param account_id:
    :return: account balance
    """
    connection = sqlite3.connect("database.sqlite", isolation_level=None)
    cursor = connection.cursor()
    sum = 0
    # getting incomes
    incomes = cursor.execute(f"SELECT * FROM incomes WHERE account_id={account_id}").fetchall()
    for income in incomes:
        sum += income[1]
    outcomes = cursor.execute(f"SELECT * FROM outcomes WHERE account_id={account_id}").fetchall()
    for outcome in outcomes:
        sum -= outcome[1]
    transactions_to = cursor.execute(f"SELECT * FROM transactions WHERE to_account_id={account_id}").fetchall()
    for transaction_to in transactions_to:
        sum += transaction_to[2]
    transactions_from = cursor.execute(f"SELECT * FROM transactions WHERE from_account_id={account_id}").fetchall()
    for transaction_from in transactions_from:
        sum -= transaction_from[2]
    connection.close()
    return sum
