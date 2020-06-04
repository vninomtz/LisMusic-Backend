from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.account import Account
from dataclasses import dataclass

@dataclass
class CreateAccountInputDto:
    idAccount: str
    firstName: str
    lastName: str
    email: str
    password: str
    userName: str
    gender: str
    birthday: str
    cover: str

class CreateAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, inputAccount: CreateAccountInputDto):
        newAccount = Account.create(inputAccount.firstName, inputAccount.lastName, inputAccount.email,
                        inputAccount.password, inputAccount.userName,inputAccount.birthday, inputAccount.cover)

        return self.repository.save(newAccount)
         
