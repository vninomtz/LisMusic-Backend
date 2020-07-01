from accounts.accounts.domain.account import Account
from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from infraestructure.connection import ConnectionSQL
from accounts.accounts.domain.exceptions import DataBaseException, AccountNotExistException, EmailAlreadyExistException, UserNameAlreadyExistException

class SqlServerAccountRepository(AccountRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, account: Account):
        self.connection.open()
        sql = """
                DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPI_CreateAccount]
                @IdAccount = ?,
                @firstName = ?,
                @lastName = ?,
                @email = ?,
                @password = ?,
                @userName = ?,
                @gender = ?,
                @birthday = ?,
                @cover = ?,
                @created = ?,
                @updated = ?,
                @contentCreator = ?,
                @typeRegister = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT

        SELECT	@salida as N'@salida',
                @estado as N'@estado'
        """
        params = (account.idAccount,account.firstName,account.lastName,account.email,account.password,
                    account.userName,account.gender,account.birthday,account.cover,account.createdDate,
                    None,account.contentCreator, account.typeRegister)

        self.connection.cursor.execute(sql,params)

        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, " Account created")
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Error en la conexión a la BD")


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
        self.connection.open()
        sql = """
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

    
    def exist_email(self, email: str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_EmailExist]
                    @email = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, email)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
        
        self.connection.close()
        return result


    def exist_userName(self, userName: str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_UserNameExist]
                    @userName = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, userName)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
        
        self.connection.close()
        return result

    def exist_userName(self, userName: str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_UserNameExist]
                    @userName = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, userName)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
        
        self.connection.close()
        return result

    def login_with_username(self, username, password):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_LoginWithUsername]
                    @username = ?,
                    @password = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, username, password)
        rows = self.connection.cursor.fetchall()
        account = None
        if rows:
            for row in rows:
                account = Account(row.IdAccount,row.FirstName,row.LastName,row.Email,None,row.UserName, row.Gender,row.Birthday.strftime('%Y-%m-%d'),row.Cover,
                row.CreatedDate.strftime('%Y-%m-%d'),None,row.ContentCreator,None)
                if row.UpdatedDate:
                    account.updatedDate = row.UpdatedDate.strftime('%Y-%m-%d')
        
        self.connection.close()
        return account


    def login_with_email(self, email,password):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_LoginWithEmail]
                    @email = ?,
                    @password = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, email, password)
        rows = self.connection.cursor.fetchall()
        account = None
        if rows:
            for row in rows:
                account = Account(row.IdAccount,row.FirstName,row.LastName,row.Email,None,row.UserName, row.Gender,row.Birthday.strftime('%Y-%m-%d'),row.Cover,
                row.CreatedDate.strftime('%Y-%m-%d'),None,row.ContentCreator,None)
                if row.UpdatedDate:
                    account.updatedDate = row.UpdatedDate.strftime('%Y-%m-%d')

        
        self.connection.close()
        return account




        

    

