from PyQt4 import *
import Models.TableModel as c

class MainController():
	def __init__(self):		
		import Views.MainWindow as mainWindow
		data = None
		self.main = mainWindow.MainWindow(data)
		#self.main.btn1.clicked.connect(self.doit)
		self.main.addClient.triggered.connect(self.addClient)
		self.main.addEmployee.triggered.connect(self.addEmployee)
		self.main.show()
		
		
		headers = ["ID","Nome","Idade"]
		
		clients = [[1,"Guilherme",20], [2,"Marcelo",21], [3,"Cliente",20]] 
		clientModel = c.TableModel(clients,headers)
		self.main.clientTableView.setModel(clientModel)
		
		employee = [[10,"Vadia",23], [20,"Puta",24], [24,"Paulista",24],["12+12","Victor",24]] 
		employeeModel = c.TableModel(employee,headers)
		self.main.employeeTableView.setModel(employeeModel)
		
		
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
