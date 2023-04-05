import mysql.connector

# Connect to the MySQL server
database = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
)

# Perform database operations
cursorObject = database.cursor()
cursorObject.execute('CREATE DATABASE crm')

# print('All Done')

# Close the database connection
cursorObject.close()
