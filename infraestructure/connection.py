import pyodbc
from accounts.accounts.domain.exceptions import DataBaseException

class ConnectionSQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.server = '25.111.36.180'
        self.database = 'LisMusicDB'
        self.username = 'sa'
        self.password = '12345'
        self.connectionString = "DRIVER={ODBC Driver 17 for SQL Server}" + ";SERVER={0};DATABASE={1};UID={2};PWD={3}".format(
        self.server, self.database,self.username,self.password)
        

    def open(self):
        try:
            self.connection = pyodbc.connect(self.connectionString)
            self.cursor = self.connection.cursor()
        except Exception as ex:
            raise DataBaseException(ex)
        


    def close(self):
        self.cursor.close()
        self.connection.close()

    def save(self):
        self.connection.commit()