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
    def get(self):
        pass