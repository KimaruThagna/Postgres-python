import psycopg2 as pg #python connection library to postgres db
# connect to postgres databse
con=pg.connect("dbname='pythontrials' user='postgres' host='localhost'password='postgres'")
# create a cursor to hold sql statements
cursor=con.cursor()
# store command in the cursor
cursor.execute("select * from contacts")
data=cursor.fetchall()
for r in data:
     print(r)
 #importing data as a dictionary rather than a list so as to use column names
import psycopg2.extras as ex
cur=con.cursor(cursor_factory=ex.DictCursor)
cur.execute("select * from contacts")
d_data=cur.fetchall()
print(d_data)

#=======================================
# one can select a table in postgres and output the sql result in json format
#=======================================

#SELECT row_to_json(contacts) from contacts;
#========================================================
#Write data from table to file
#========================================================

fhandle=open('data','w')

cur.execute('select * from contacts')
cur.fetchall()
cur.copy_to(fhandle,'contacts',sep="|") # sep is seperator


#=========================================
#from file to db
#=========================================


fhandle=open('data','r')
cur.execute('select * from contacts')
cur.fetchall()
cur.copy_from(fhandle,'contacts',sep="|")
con.commit() #since youre saving to database

