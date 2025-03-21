import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",   #your MySQL server address
    user="root",        #your MySQL username
    password="aaaaaa"   #your MySQL password
)
dbcursor=mydb.cursor()  #Create a cursor object
dbcursor.execute(“drop database lee")  #Delete a database
print("database deleted")  #Working Response
