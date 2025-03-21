import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
dbcur=("select City,count(*) from Student group by City")
dbcursor.execute(dbcur)
for dbshow, City in dbcursor.fetchall():
    print(f"{dbshow}: {City}")

