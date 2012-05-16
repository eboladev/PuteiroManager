from PyQt4.Qt import *
from PyQt4 import *
from app.Helpers.Table_Helper import *

class listAll_View(QMainWindow):
    
    def __init__(self, data):
        super(listAll_View, self).__init__()
        self.initUI(data)
        
    def initUI(self, data):

        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 29))
        self.menubar.setObjectName(("menubar"))
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setTitle(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdd.setObjectName(("menuAdd"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setObjectName(("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(("menuHelp"))
        self.setMenuBar(self.menubar)

        self.addClient = QtGui.QAction(self)
        self.addClient.setText(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.addClient.setObjectName(("addClient"))
        self.addClient.triggered.connect(self.doit)
        self.addEmployee = QtGui.QAction(self)
        self.addEmployee.setText(QtGui.QApplication.translate("MainWindow", "Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.addEmployee.setObjectName(("addEmployee"))
        self.viewClient = QtGui.QAction(self)
        self.viewClient.setText(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.viewClient.setObjectName(("viewClient"))
        self.viewEmployee = QtGui.QAction(self)
        self.viewEmployee.setText(QtGui.QApplication.translate("MainWindow", "Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.viewEmployee.setObjectName(("viewEmployee"))
        self.actionNo_Help = QtGui.QAction(self)
        self.actionNo_Help.setText(QtGui.QApplication.translate("MainWindow", "No Help!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNo_Help.setObjectName(("actionNo_Help"))
        self.menuAdd.addAction(self.addClient)
        self.menuAdd.addAction(self.addEmployee)
        self.menuView.addAction(self.viewClient)
        self.menuView.addAction(self.viewEmployee)
        self.menuHelp.addAction(self.actionNo_Help)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
       
        labelTitle = QLabel("<h1>Clientes do puteiro</h1>", self)
        labelTitle.move(10,20)
        table = Table_Helper(self, data, ['ID', 'Nome', 'Idade'])
        table.setGeometry(10,70,340,100)
        labelFooter = QLabel("COPYLEFT - All Wrongs Reserved", self)
        labelFooter.move(60,280)
        self.setGeometry(300, 300, 360, 300)
        self.setWindowTitle('Puteiro manager')    
        self.show()
    def doit(self):
        print "Opening a new popup window..."
        self.w = popup_View()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()
