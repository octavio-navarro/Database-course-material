import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='0412M4sql.', host='127.0.0.1', database='iot')
    cursor = cnx.cursor()

    query_data = (3,)
    query = (f"SELECT * FROM rooms WHERE id_room > %s;")
    
    cursor.execute(query, query_data)

    for result in cursor:
        print(result)

except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  cnx.close()