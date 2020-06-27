from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.exceptions import DataBaseException
from accounts.accounts.domain.account import Account


class ExistAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, idAccount):
   
        try:
            return self.repository.exist_account(idAccount)
        except DataBaseException as ex:
            raise DataBaseException(ex)
        