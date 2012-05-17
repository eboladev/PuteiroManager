import sys
from PyQt4.Qt import *
from app.Models.Clients import *
#from app.Views.listAll_View import *
from ..Views.listAll_View import *
from ..Views.addClient_View import *

class Clients_Controller():
	def __init__(self):
		self.__m = Clients_Model()
	def listAll(self):
		app = QApplication(sys.argv)
		v = listAll_View(self, self.__m.listAll())
		sys.exit(app.exec_())
	def listOne(self, cod):
		app = QApplication(sys.argv)
		v = listAll_View(self.__m.find(cod))
		sys.exit(app.exec_())
	@staticmethod
	def addClient():
		v = addClient_View()
