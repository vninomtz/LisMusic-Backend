from accounts.accounts.domain.account import Account
from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from infraestructure.connection import ConnectionSQL
from accounts.accounts.domain.exceptions import DataBaseException, AccountNotExistException

class SqlServerAccountRepository(AccountRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, account: Account):
        self.connection.open()
        self.connection.cursor.execute("""
        INSERT INTO Accounts
           (IdAccount,FirstName,LastName,Email,Password,UserName,Gender,Birthday,Cover,CreatedDate)
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, account.idAccount,account.firstName,account.lastName,account.email,account.password,
        account.userName,account.gender,account.birthday,account.cover,account.createdDate)

        print(self.connection.cursor.rowcount, " Accounts inserted")
        self.connection.save()
        self.connection.close()
        return account

    def update(self, account: Account):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPU_UpdateAccount]
                @idAccount = ?,
                @firstName = ?,
                @lastName = ?,
                @userName = ?,
                @birthday = ?,
                @cover = ?,
                @updated = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """
        params =(account.idAccount,account.firstName, account.lastName,account.userName, account.birthday, 
                account.cover,account.updatedDate)

        self.connection.cursor.execute(sql, params)
        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, " Accounts updated")
            self.connection.close()
            return True
        except DataBaseException as identifier:
            raise DataBaseException("Error en la conexión a la BD")


    def delete(self, accountId: str):
        if not self.exist_account(accountId):
            raise AccountNotExistException("Account not exist")

        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPD_DeleteAccount]
                    @idAccount = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT
        """
        params = (accountId)
        self.connection.cursor.execute(sql, params)
        row = self.connection.cursor.rowcount
        print(row)
        if row == -1:
            raise DataBaseException("Error deleting account")

        try:
            self.connection.save()
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Error al actualizar la Base de datos: ", ex)


    def exist_account(self, idAccount:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_AccountExist]
                    @idAccount = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idAccount)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
        
        self.connection.close()
        return result


        

    

