from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.exceptions import AccountNotExistException, DataBaseException
from accounts.accounts.domain.account import Account


class ExistAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, idAccount):
   
        try:
            exists = self.repository.exist_account(idAccount)
            if not exists:
                raise AccountNotExistException("Account not exist")
            
            return exists
        except DataBaseException as ex:
            raise DataBaseException(ex)
        