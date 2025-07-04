import mysql.connector
import check

try:
    connection = mysql.connector.connect(host= check.user_credentials['host'], 
                                         user = check.user_credentials['username'], 
                                         passwd= check.user_credentials['password'])
    myCursor = connection.cursor()
    query = "CREATE DATABASE IF NOT EXISTS %s"
    dbName = 'alx_book_store'
    myCursor.execute(query, dbName,)
    connection.commit()
    print(f"Database {dbName} created successfully!")
except mysql.connector.Error as error:
    print(f"Error: {error}")