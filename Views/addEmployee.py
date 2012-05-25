# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEmployee.ui'
#
# Created: Thu May 24 02:05:13 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class AddEmployee(QtGui.QDialog):
    def __init__(self, *args):
		QtGui.QDialog.__init__(self, *args)
		self.setObjectName(_fromUtf8("Dialog"))
		self.resize(293, 176)
		self.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.gridLayout = QtGui.QGridLayout(self)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.title = QtGui.QLabel(self)
		font = QtGui.QFont()
		font.setPointSize(22)
		self.title.setFont(font)
		self.title.setText(QtGui.QApplication.translate("Dialog", "Add Employee", None, QtGui.QApplication.UnicodeUTF8))
		self.title.setObjectName(_fromUtf8("title"))
		self.horizontalLayout.addWidget(self.title)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.nameLabel = QtGui.QLabel(self)
		self.nameLabel.setText(QtGui.QApplication.translate("Dialog", "Nome", None, QtGui.QApplication.UnicodeUTF8))
		self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
		self.horizontalLayout_2.addWidget(self.nameLabel)
		self.nameLineEdit = QtGui.QLineEdit(self)
		self.nameLineEdit.setText(_fromUtf8(""))
		self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
		self.horizontalLayout_2.addWidget(self.nameLineEdit)
		self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.label_3 = QtGui.QLabel(self)
		self.label_3.setText(QtGui.QApplication.translate("Dialog", "Idade", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.horizontalLayout_3.addWidget(self.label_3)
		self.lineEdit_2 = QtGui.QLineEdit(self)
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.horizontalLayout_3.addWidget(self.lineEdit_2)
		self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
		self.buttonBox = QtGui.QDialogButtonBox(self)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
		QtCore.QMetaObject.connectSlotsByName(self)
