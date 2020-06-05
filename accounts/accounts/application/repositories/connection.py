import pyodbc

class ConnectionSQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.server = 'localhost,1500'
        self.database = 'LisMusicDB'
        self.username = 'usrLisMusicDB'
        self.password = 'usrLisMusicDB_2020'
        self.connectionString = "DRIVER={ODBC Driver 17 for SQL Server}" + ";SERVER={0};DATABASE={1};UID={2};PWD={3}".format(
        self.server, self.database,self.username,self.password)
        

    def open(self):
        self.connection = pyodbc.connect(self.connectionString)
        self.cursor = self.connection.cursor()


    def close(self):
        self.cursor.close()
        self.connection.close()


# Ejemplo de implementación 
# conx = ConnectionSQL()
# conx.open()
# conx.cursor.execute("Select * from MusicGenders ")
# #connection.commit()
# rows = conx.cursor.fetchall() 
# for row in rows:
#     print(row, end='\n')
    

# conx.close()