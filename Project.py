import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",         #your MySQL server address
    user="root",                 #your MySQL username
    password="aaaaaa“,   #your MySQL password
    database=“Lee”          #your MySQL database
)
dbcursor=mydb.cursor()
isrun=True
while isrun:
   r=int(input("Enter your Roll:\n"))
   n=input("Enter your Name:\n")
   c=input("Enter your City name:\n")
   print("NEXT INPUT YOUR Roll,Name & City ")
   insert_data="insert into Student (Roll,Name,City)values(%s,%s,%s)"
   t=(r,n,c)
   dbcursor.execute(insert_data,t)
   mydb.commit()

