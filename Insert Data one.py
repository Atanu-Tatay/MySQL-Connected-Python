import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()  #Create a cursor object
dbcursor.execute(“insert into Emp(Eid,Ename)values(%s,%s)“,
                                (10,”Tatay”)) #insert data
mydb.commit()    #Sava database or table
print(“insert data")  #Working Response

