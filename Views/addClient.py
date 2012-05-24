# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addClient.ui'
#
# Created: Thu May 24 02:02:14 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class AddClient(QtGui.QDialog):
    def __init__(self, *args):
		QtGui.QDialog.__init__(self, *args)
		self.setObjectName(_fromUtf8("Dialog"))
		self.resize(320, 139)
		self.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.gridLayout_2 = QtGui.QGridLayout(self)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.buttonBox = QtGui.QDialogButtonBox(self)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label = QtGui.QLabel(self)
		font = QtGui.QFont()
		font.setPointSize(22)
		self.label.setFont(font)
		self.label.setText(QtGui.QApplication.translate("Dialog", "Add Client", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout.addWidget(self.label)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.label_2 = QtGui.QLabel(self)
		self.label_2.setText(QtGui.QApplication.translate("Dialog", "Nome", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout_2.addWidget(self.label_2)
		self.lineEdit = QtGui.QLineEdit(self)
		self.lineEdit.setText(_fromUtf8(""))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.horizontalLayout_2.addWidget(self.lineEdit)
		self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
		QtCore.QMetaObject.connectSlotsByName(self)
