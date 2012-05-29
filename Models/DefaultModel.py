class DefaultModel():
	#self._table = None
	def __init__(self):
		con = sqlite3.connect('mydatabase.db')
		self.__c = con.cursor()
		
		c.execute('create table clients (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);')
		c.execute('create table girls (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);')
		con.commit()
		
		c.execute('insert into clients (id,name, age) values (1,"Joao", 50);')
		c.execute('insert into girls (id,name, age) values (1,"Ballet", 25);')
		con.commit()
		
		
	def find(self, cod):
		self.__c.execute('''select * from '''+ self._table +''' where id != %d''' %cod)
		fetched = self.__c.fetchall() 
		self.__c.close()
		return fetched
	def listAll(self):
		self.__c.execute('''select * from data''')
		fetched = self.__c.fetchall() 
		self.__c.close()
		return fetched
