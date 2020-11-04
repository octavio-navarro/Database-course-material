import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='0412M4sql.', host='127.0.0.1', database='iot')

    cursor = cnx.cursor()

    query = (f"SELECT id_light FROM lights;")
    cursor.execute(query)

    # # List comprehension
    # last_id = [result[0] for result in cursor][-1]

    # # 18--> 19-29
    # for id_light in range(last_id+1, last_id+12):
    #   query_data = (id_light, False, 0)
    #   query = f"INSERT INTO lights(id_light, turned_on, intensity) values(%s, %s, %s);"
    
    #   cursor.execute(query, query_data)

    # update lights id_light > 18 turned_on true
    # query = f"UPDATE lights SET turned_on = false, intensity = 0;"

    # delte lights id_light > 5
    #query = f"DELETE FROM lights WHERE id_light > 7;"
    # cursor.execute(query)

    cnx.commit()

except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  if 'cnx' in locals() or 'cnx' in globals():
    cnx.close()