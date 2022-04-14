import flask 
from flask import jsonify
import pyodbc
conn = pyodbc.connect('Driver={SQL Server}; Server=172.26.54.46,1433;Database=Triple Take Solutions Project;UID=Triple;PWD=Triple12;Trusted_connection=no;')
print(conn)
cursor = conn.cursor()
# cursor.execute('SELECT * FROM dbo.[Test Table]')

# for i in cursor:
#     print(i)

def execute_query(connection, query):
    values = []
    cursor = connection.cursor()
    cursor.execute(query)

    for i in cursor:
        values.append(i)
        print(i)
    # print(jsonify(values))

query = 'SELECT * FROM dbo.[item]'
execute_query(conn, query)