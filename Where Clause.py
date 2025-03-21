import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
dbcur=("select * from Student where City=%s")  
dbvalue=(“Delhi",)
dbcursor.execute(dbcur,dbvalue)
for dbshow in dbcursor.fetchall():
      print(dbshow)

