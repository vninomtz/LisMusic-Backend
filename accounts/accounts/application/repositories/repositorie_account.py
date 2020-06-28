import abc 
from accounts.accounts.domain.account import Account

class AccountRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, account: Account):
        pass

    @abc.abstractmethod
    def update(self, account: Account):
        pass

    @abc.abstractmethod
    def delete(self, accountId: str):
        pass

    @abc.abstractmethod
    def exist_account(self, accountId: str):
        pass

    @abc.abstractmethod
    def exist_email(self, email: str):
        pass

    @abc.abstractmethod
    def exist_userName(self, userName: str):
        pass

    @abc.abstractmethod
    def login_with_username(self, userName:str):
        pass

    @abc.abstractmethod
    def login_with_email(self,email: str, password: str):
        pass
