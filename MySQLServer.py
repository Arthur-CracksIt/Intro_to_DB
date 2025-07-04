import mysql.connector
import check

connection = mysql.connector.connect(host= check.user_credentials['host'], user = check.user_credentials['username'], passwd= check.user_credentials['password'])

myCursor = connection.cursor()
query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

myCursor.execute(query)
connection.commit()