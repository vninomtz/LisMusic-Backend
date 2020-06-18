from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.exceptions import AccountInvalidException, DataBaseException, AccountNotExistException
from accounts.accounts.domain.account import Account
from dataclasses import dataclass


@dataclass
class DeleteAccountInputDto:
    idAccount: str = None


class DeleteAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, inputAccount: DeleteAccountInputDto):
        if not inputAccount.idAccount:
            raise AccountInvalidException("Campos vacíos")
        
        try:
            result = self.repository.delete(inputAccount.idAccount)
            return result
        except AccountNotExistException as ex:
            raise AccountNotExistException(ex)
        except DataBaseException as ex:
            raise DataBaseException(ex)
        