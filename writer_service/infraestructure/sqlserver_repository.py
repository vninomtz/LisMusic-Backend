from accounts.accounts.domain.account import Account
from accounts.accounts.application.repositories.repositorie_account import AccountRepository
from infraestructure.connection import ConnectionSQL
from accounts.accounts.domain.exceptions import DataBaseException

class SqlServerAccountRepository(AccountRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, account: Account):
        self.connection.open()
        self.connection.cursor.execute("""
        INSERT INTO Accounts
           (IdAccount,FirstName,LastName,Email,Password,UserName,Gender,Birthday,Cover)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, account.idAccount,account.firstName,account.lastName,account.email,account.password,
        account.userName,account.gender,account.birthday,account.cover)

        print(self.connection.cursor.rowcount, " Accounts inserted")
        self.connection.save()
        self.connection.close()
        return account

    def update(self, account: Account):
        self.connection.open()
        self.connection.cursor.execute("""
        UPDATE Accounts
            SET FirstName = ?
                ,LastName = ?
                ,UserName = ?
                ,Birthday = ?
                ,Cover = ?
            WHERE IdAccount = ?
        """, account.firstName, account.lastName,account.userName, account.birthday, account.cover, account.idAccount)
        
        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, " Accounts updated")
            return True
        except DataBaseException as identifier:
            raise DataBaseException("Error en la conexión a la BD")

    def delete(self, accountId: str):
        self.connection.open()
        self.connection.cursor.execute("""
        DELETE FROM Accounts WHERE IdAccount = ?""", accountId)
        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, " Accounts deleted")
            return True
        except DataBaseException as ex:
            raise DataBaseException("Error al actualizar la Base de datos: ", ex)
        

    

