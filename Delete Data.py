import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
dbdelete=“delete from Emp where Ename=%s” 
dbvalue=(“Rohit”,)
dbcursor.execute(dbdelete,dbvalue)
mydb.commit()
Print(dbcursor.rowcount,”Record Deleted”)

