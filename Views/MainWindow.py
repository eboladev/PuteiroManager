import sys
from PyQt4 import *
class MainWindow(Qt.QMainWindow):
	def __init__(self, *args):
		Qt.QMainWindow.__init__(self, *args)
		self.cw = Qt.QWidget(self)
		self.setCentralWidget(self.cw)
		self.setGeometry(100,100,400,400)
		self.sigFoo = QtCore.pyqtSignal()
		self.btn1 = Qt.QPushButton("Click me", self.cw)
		self.btn1.setGeometry(Qt.QRect(0, 0, 100, 30))