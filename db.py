import sqlite3
def createDataBase():
  con = sqlite3.connect('''mydatabase.db''')
  c = con.cursor()
  c.execute('''drop table data;''')
  con.commit()
  c.execute('''create table clients (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);''')
  c.execute('''create table girls (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);''')
  con.commit()
  c.execute('''insert into clients (id,name, age) values (1,"Joao", 50);''')
  c.execute('''insert into girls (id,name, age) values (1,"Ballet", 25);''')
  con.commit()

  print c.lastrowid
  
  c.close()

#sqlite select example
def select():
  con = sqlite3.connect('''mydatabase.db''')
  c = con.cursor()
  
  c.execute('''select * from data''')
  print c.fetchall() 
  
  c.close()

#sqlite select example 2
def selectByID(id):
  con = sqlite3.connect('''mydatabase.db''')
  c = con.cursor()
  
  results = c.execute('''select name from data where id = %d''' %id)
  
  for row in results:
      name = row[0]
      print "id:", id, "name:", name
  
  c.close()
  
createDataBase()
#select()
#selectByID(2)
