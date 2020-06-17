from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.exceptions import EmptyFieldsException, DataBaseException
from accounts.accounts.domain.account import Account
from dataclasses import dataclass


@dataclass
class DeleteAccountInputDto:
    idAccount: str = None


class DeleteAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, inputAccount: DeleteAccountInputDto):
        if inputAccount.idAccount is None:
            raise EmptyFieldsException("Campos vacíos")
        
        try:
            result = self.repository.delete(inputAccount.idAccount)
            return result
        except DataBaseException:
            raise DataBaseException("Error al eliminar la cuenta")
        