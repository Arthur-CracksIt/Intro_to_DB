import mysql.connector
import check

try:
    connection = mysql.connector.connect(host= check.user_credentials['host'], 
                                         user = check.user_credentials['username'], 
                                         passwd= check.user_credentials['password'])
    myCursor = connection.cursor()
    dbName = 'alx_book_store'
    query = f"CREATE DATABASE IF NOT EXISTS {dbName} "
    myCursor.execute(query) 
    connection.commit()
    print(f"Database {dbName} created successfully!")
except mysql.connector.Error as error:
    print(f"Error: {error}")