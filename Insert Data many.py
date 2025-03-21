import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()  #Create a cursor object
dbinsert=(“insert into Emp(Eid,Ename)values(%s,%s)“)
dblist=[(30,”Anish”),(40,”Aftab”),(32,”Rohit”),(22,”Virat”)]
dbcursor.executemany(dbinsert,dblist)
mydb.commit()    #Sava database or table
print(dbcursor.rowcount,“insert data")  #Number of data count   

