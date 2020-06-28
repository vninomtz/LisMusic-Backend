from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from accounts.accounts.domain.exceptions import AccountNotExistException, DataBaseException, EmailNotExistsException, EmptyFieldsException, LoginFailedException, UserNotExistsException
from accounts.accounts.domain.account import Account
from dataclasses import dataclass
import json
from flask.json import jsonify


@dataclass
class LoginAccountInputDto:
    user: str = None  
    password: str = None

class LoginAccount:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def execute(self, inputLoginAccount:LoginAccountInputDto):

        if not inputLoginAccount.user and not inputLoginAccount.password:
            raise EmptyFieldsException("Empty fields.")

        account = Account(None,None,None,inputLoginAccount.user,inputLoginAccount.password,inputLoginAccount.user,None,None,None,
                None,None,None,None)

        try:
            username_exists = self.repository.exist_userName(account.userName) 
            email_exists = self.repository.exist_email(account.email)
       
            if not username_exists and not email_exists :
                raise UserNotExistsException("Username or email not exists.")

            if username_exists:
                account = self.repository.login_with_username(account.userName, account.encode(account.password))
            else:
                account = self.repository.login_with_email(account.email, account.encode(account.password))

            if not account:
                    raise LoginFailedException("Incorrect credentials.")
            
            return account        
            
        except DataBaseException as ex:
            raise DataBaseException(ex)
        