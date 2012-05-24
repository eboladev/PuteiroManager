from PyQt4 import *
class MainController():
	def __init__(self):		
		import Views.MainWindow as mainWindow
		self.main = mainWindow.MainWindow()
		#self.main.btn1.clicked.connect(self.doit)
		self.main.addClient.triggered.connect(self.addClient)
		self.main.addEmployee.triggered.connect(self.addEmployee)
		self.main.show()
	def doit(self):
		print "Opening a new popup window..."
		import Views.PopUp as popUp
		self.w = popUp.PopUp()
		self.w.setGeometry(150, 150, 400, 200)
		self.w.show()
	def addClient(self):
		import Views.addClient as popUp
		self.w = popUp.AddClient()
		self.w.show()
		print "Opening a new popup window..."
	def addEmployee(self):
		import Views.addEmployee as popUp
		self.w = popUp.AddEmployee()
		self.w.show()
		print "Opening a new popup window..."
