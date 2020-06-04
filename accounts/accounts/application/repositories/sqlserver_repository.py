from accounts.accounts.domain.account import Account
from accounts.accounts.application.repositories.repositorie_account import AccountRepository


class SqlServerAccountRepository(AccountRepository):
    def __init__(self, connection):
        self.connection = connection

    def save(self, account: Account):
        pass

    def update(self, account: Account):
        pass

    def delete(self, accountId: str):
        pass