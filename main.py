import psycopg2


#--------------------------------------------!--------------------------------------------

#connect to the db 
con = psycopg2.connect(
            # don't forget write your data !!
            host = "localhost-name",
            database="db-name",
            user = "server-yser",
            password = "your-password")
#--------------------------------------------!--------------------------------------------

#cursor 
cur = con.cursor()
#--------------------------------------------!--------------------------------------------

#add a new employee 
#cur.execute("insert into employees (name,age,departement) values ('jhony',34,'IT') ;")
#--------------------------------------------!--------------------------------------------
#update employee
#cur.execute("update employees set name='linda' , age=27 , departement='HR' where id =2 ;")
#--------------------------------------------!--------------------------------------------

#delete employee 
cur.execute("delete from employees where id=4 ;")
#--------------------------------------------!--------------------------------------------

#execute query
cur.execute("select * from employees")
#--------------------------------------------!--------------------------------------------

#show data
rows = cur.fetchall()

for r in rows:
    print (f"id : {r[0]} , name : {r[1]}, age : {r[2]}, departement : {r[3]}")
#--------------------------------------------!--------------------------------------------

#commit the transcation 
con.commit()
#--------------------------------------------!--------------------------------------------

#close the cursor
cur.close()
#--------------------------------------------!--------------------------------------------

#close the connection
con.close()
#--------------------------------------------!--------------------------------------------