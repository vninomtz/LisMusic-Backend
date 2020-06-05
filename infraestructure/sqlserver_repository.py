from accounts.accounts.domain.account import Account
from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.application.repositories.connection import ConnectionSQL

class SqlServerAccountRepository(AccountRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, account: Account):
        print(account.idAccount + ": " + account.firstName)
        return account

    def update(self, account: Account):
        pass

    def delete(self, accountId: str):
        pass

    def get(self):
        self.connection.open()
        self.connection.cursor.execute("Select * from MusicGenders where GenderName = 'Pop'")
        rows = self.connection.cursor.fetchall() 
        for row in rows:
            print(row, end='\n')
        self.connection.close()

