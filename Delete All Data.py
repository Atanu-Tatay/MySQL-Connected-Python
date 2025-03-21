import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
dbdeleteall=“truncate table Emp” 
dbcursor.execute(dbdeleteall)
mydb.commit()
Print(dbcursor.rowcount,“All Record Delete”)

