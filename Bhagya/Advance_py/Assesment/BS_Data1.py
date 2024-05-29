# Import the pymysql module to enable communication with MySQL
import pymysql

# Establish a connection to the MySQL server without specifying a database
mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()  # Create a cursor object using the connection

# Execute SQL command to create a new database named 'Biling_Database' if it doesn't exist
mycursor.execute("create database if not exists Biling_Database")
mydb.commit()  # Commit the transaction to the database

# Re-establish connection, this time specifying the newly created database
mydb = pymysql.connect(host="localhost", user="root", password="", database="Biling_Database")
mycursor = mydb.cursor()  # Create a new cursor object using the new connection

# Execute SQL command to create a new table named 'software' if it doesn't exist
# The table includes columns for id, customer name, phone number, and bill number
# 'id' is set as the primary key and will auto-increment with each new entry
mycursor.execute("create table if not exists software(id int primary key auto_increment ,Customer_name varchar(30),Phone_no Bigint(12),Bill_no int(12))")
mydb.commit()   # Commit the transaction to ensure the table is created

  