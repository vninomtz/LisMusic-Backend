import pyodbc

server = 'localhost,1500'
database = 'LisMusicDB'
username = 'usrLisMusicDB'
password = 'usrLisMusicDB_2020'
connectionString = "DRIVER={ODBC Driver 17 for SQL Server}" + ";SERVER={0};DATABASE={1};UID={2};PWD={3}".format(
server, database,username,password)
connection = pyodbc.connect(connectionString)
query = """INSERT INTO MusicGenders (GenderName, Cover) VALUES (?,?)""", 'Pop', 'url' 

cursor = connection.cursor()
#cursor.execute("""INSERT INTO MusicGenders (GenderName, Cover) VALUES (?,?)""",'Rock', 'url') 
cursor.execute("Select * from MusicGenders where GenderName = 'Pop'")
#connection.commit()
rows = cursor.fetchone() 
if rows:
    print(rows.GenderName, end='\n')
    