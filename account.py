from typing import List


class Operation:
    pass


class Transaction:
    pass


class Account:
    def __init__(self, account_id: int, name: str, currency: str, incomes: List[Operation], outcomes: List[Operation],
                 transactions: List[Transaction]):
        self.account_id = account_id
        self.name = name
        self.currency = currency
        self.incomes = incomes
        self.outcomes = outcomes
        self.transactions = transactions

    def add_new_income(self, income: Operation):
        self.incomes.append(income)

    def add_new_outcome(self, outcome: Operation):
        self.outcomes.append(outcome)

    def delete_income(self, income_id: int):
        filter(lambda income: income.id != income_id, self.incomes)

    def delete_outcome(self, outcome_id: int):
        filter(lambda outcome: outcome.id != outcome_id, self.outcomes)
