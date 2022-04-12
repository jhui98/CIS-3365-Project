import pyodbc
conn = pyodbc.connect('Driver={SQL Server}; Server=172.26.54.46,1433;Database=Triple Take Solutions Project;UID=Triple;PWD=Triple12;Trusted_connection=no;')
print(conn)
cursor = conn.cursor()
# cursor.execute('SELECT * FROM dbo.[Test Table]')

# for i in cursor:
#     print(i)

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)

    for i in cursor:
        print(i)

query = 'SELECT * FROM dbo.[Test Table]'
execute_query(conn, query)