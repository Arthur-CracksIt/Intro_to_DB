import mysql.connector
import check

try:
    connection = mysql.connector.connect(host= check.user_credentials['host'], 
                                         user = check.user_credentials['username'], 
                                         passwd= check.user_credentials['password'])
    myCursor = connection.cursor()
    dbName = 'alx_book_store'
    # query = f"CREATE DATABASE IF NOT EXISTS {dbName} "
    query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    myCursor.execute(query) 
    connection.commit()
    print(f"Database {dbName} created successfully!")

    listAll = myCursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'alx_book_store'")
    # result = myCursor.fetchall()
    # for i in result:
    #     print(i)
except mysql.connector.Error as error:
    print(f"Error: {error}")