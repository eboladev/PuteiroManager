# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEmployeeForm.ui'
#
# Created: Wed May 16 14:32:55 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_addEmployerForm(object):
    def setupUi(self, addEmployerForm):
        addEmployerForm.setObjectName(_fromUtf8("addEmployerForm"))
        addEmployerForm.resize(360, 143)
        addEmployerForm.setWindowTitle(QtGui.QApplication.translate("addEmployerForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(addEmployerForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clientHeader = QtGui.QLabel(addEmployerForm)
        self.clientHeader.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Waree"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clientHeader.setFont(font)
        self.clientHeader.setText(QtGui.QApplication.translate("addEmployerForm", "Add Employer", None, QtGui.QApplication.UnicodeUTF8))
        self.clientHeader.setObjectName(_fromUtf8("clientHeader"))
        self.verticalLayout.addWidget(self.clientHeader)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.addClientName = QtGui.QHBoxLayout()
        self.addClientName.setObjectName(_fromUtf8("addClientName"))
        self.nameLabel = QtGui.QLabel(addEmployerForm)
        self.nameLabel.setText(QtGui.QApplication.translate("addEmployerForm", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.addClientName.addWidget(self.nameLabel)
        self.nameLineEdit = QtGui.QLineEdit(addEmployerForm)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.addClientName.addWidget(self.nameLineEdit)
        self.gridLayout.addLayout(self.addClientName, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.clearButton = QtGui.QPushButton(addEmployerForm)
        self.clearButton.setText(QtGui.QApplication.translate("addEmployerForm", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.addClientButton = QtGui.QPushButton(addEmployerForm)
        self.addClientButton.setText(QtGui.QApplication.translate("addEmployerForm", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.addClientButton.setObjectName(_fromUtf8("addClientButton"))
        self.horizontalLayout.addWidget(self.addClientButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(addEmployerForm)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nameLineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(addEmployerForm)

    def retranslateUi(self, addEmployerForm):
        pass

