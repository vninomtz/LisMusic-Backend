from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.account import Account
from accounts.accounts.domain.exceptions import EmailAlreadyExistException, UserNameAlreadyExistException, DataBaseException
from dataclasses import dataclass

@dataclass
class CreateAccountInputDto:
    idAccount: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    userName: str = None
    gender: str = None
    birthday: str = None
    cover: str = None
    typeRegister: str = None

class CreateAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, inputAccount: CreateAccountInputDto):
        newAccount = Account.create(inputAccount.firstName, inputAccount.lastName, inputAccount.email,
                        inputAccount.password, inputAccount.userName,inputAccount.gender, 
                        inputAccount.birthday, inputAccount.cover, inputAccount.typeRegister)
        
        if self.repository.exist_email(newAccount.email):
           raise EmailAlreadyExistException("Email already exist")

        if self.repository.exist_userName(newAccount.userName):
            raise UserNameAlreadyExistException("User name already exist")

        try:
            account = self.repository.save(newAccount)
            return newAccount
        except DataBaseException:
            raise DataBaseException("Error en la base de datos")
