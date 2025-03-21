import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
dbupdate=“update Emp set Eid=%s where Ename=%s”
dbvalue=(50,”Rohit”)  #Change Rohit Id 
dbcursor.execute(dbupdate,dbvalue)
mydb.commit()

