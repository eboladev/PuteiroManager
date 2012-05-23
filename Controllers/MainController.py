class MainController():
	def __init__(self):		
		import Views.MainWindow as mainWindow
		self.main = mainWindow.MainWindow()
		self.main.btn1.clicked.connect(self.doit)
		self.main.show()
	def doit(self):
		print "Opening a new popup window..."
		import Views.PopUp as popUp
		self.w = popUp.PopUp()
		self.w.setGeometry(150, 150, 400, 200)
		self.w.show()
