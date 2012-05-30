from PyQt4 import *
import Models.TableModel as c
import Models.DefaultModel as db

class MainController():
	def __init__(self):		
		import Views.MainWindow as mainWindow
		data = None
		self.main = mainWindow.MainWindow(data)
		self.main.addClient.triggered.connect(self.addClient)
		self.main.addEmployee.triggered.connect(self.addEmployee)
		self.main.show()
		
		headers = ["ID","Nome","Idade"]
		
		self.database = db.DefaultModel()
		
		clients = self.database.selectAll("clients") 
		clientModel = c.TableModel(clients,headers)
		self.main.clientTableView.setModel(clientModel)
		
		employee = self.database.selectAll("girls") 
		employeeModel = c.TableModel(employee,headers)
		self.main.employeeTableView.setModel(employeeModel)
		
	def addClient(self):
		import Views.addClient as popUp
		self.w = popUp.AddClient()
		self.w.show()
		if self.w.exec_():
			pass
		print "C: " + self.w.getName() + " - " + self.w.getAge()
		self.database.insertClient(self.w.getName(),self.w.getAge())
			
			

	def addEmployee(self):
		import Views.addEmployee as popUp
		self.w = popUp.AddEmployee()
		self.w.show()
		if self.w.exec_():
			pass
		print "E: " + self.w.getName() + " - " + self.w.getAge()
