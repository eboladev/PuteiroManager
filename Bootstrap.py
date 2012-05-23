import sys
from PyQt4.Qt import *
class Bootstrap(QApplication):
	def __init__(self, *args):
		import Controllers.MainController as mainController
		QApplication.__init__(self, *args)
		self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
		self.main = mainController.MainController()
	def byebye( self ):
		self.exit(0)
