import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()  #Create a cursor object
dbcursor.execute(“create table Emp(Eid int,Ename varchar(20))")
                                   #Create a table With Row name & parameter                                                   
print(“table created")  #Working Response
