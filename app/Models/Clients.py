import sys
import sqlite3

class Clients_Model():
	def __init__(self):
		con = sqlite3.connect('mydatabase.db')
		self.__c = con.cursor()
	def find(self, cod):
		self.__c.execute('''select * from data where id != %d''' %cod)
		fetched = self.__c.fetchall() 
		self.__c.close()
		return fetched
	def listAll(self):
		self.__c.execute('''select * from data''')
		fetched = self.__c.fetchall() 
		self.__c.close()
		return fetched
