from accounts.accounts.application.use_cases import create_account, update_account
from infraestructure.sqlserver_repository import SqlServerAccountRepository
import datetime
from accounts.accounts.domain.account import Account
from accounts.accounts.domain.exceptions import AccountInvalidException, DataBaseException

#usecase = create_account.CreateAccount(SqlServerAccountRepository())
usecase = update_account.UpdateAccount(SqlServerAccountRepository())
dtoclass = update_account.UpdateAccountInputDto()
dtoclass.idAccount = "4b608c10-a341-472a-ad5d-ebe1fde68d24"
dtoclass.firstName = "Victor Manuel"
dtoclass.lastName = "Niño Martínez"
#dtoclass.email = "vic@gmail.com"
#dtoclass.password = "12345"
dtoclass.userName = "victor_nino"
dtoclass.gender = "Male"
dtoclass.birthday = datetime.date(1999,9,23)
dtoclass.cover = "url"

try:
    result = usecase.execute(dtoclass)
    if result:
        print("Exito en la actualización")
except (AccountInvalidException, DataBaseException) as ex:
    print(ex)


