# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addClientForm.ui'
#
# Created: Wed May 16 14:19:43 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_addClientForm(object):
    def setupUi(self, addClientForm):
        addClientForm.setObjectName(_fromUtf8("addClientForm"))
        addClientForm.resize(358, 143)
        addClientForm.setWindowTitle(QtGui.QApplication.translate("addClientForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(addClientForm)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.addClientName = QtGui.QHBoxLayout()
        self.addClientName.setObjectName(_fromUtf8("addClientName"))
        self.nameLabel = QtGui.QLabel(addClientForm)
        self.nameLabel.setText(QtGui.QApplication.translate("addClientForm", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.addClientName.addWidget(self.nameLabel)
        self.nameLineEdit = QtGui.QLineEdit(addClientForm)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.addClientName.addWidget(self.nameLineEdit)
        self.gridLayout_2.addLayout(self.addClientName, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clientHeader = QtGui.QLabel(addClientForm)
        self.clientHeader.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Waree"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clientHeader.setFont(font)
        self.clientHeader.setText(QtGui.QApplication.translate("addClientForm", "Add Client", None, QtGui.QApplication.UnicodeUTF8))
        self.clientHeader.setObjectName(_fromUtf8("clientHeader"))
        self.verticalLayout.addWidget(self.clientHeader)
        spacerItem = QtGui.QSpacerItem(17, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.clearButton = QtGui.QPushButton(addClientForm)
        self.clearButton.setText(QtGui.QApplication.translate("addClientForm", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.addClientButton = QtGui.QPushButton(addClientForm)
        self.addClientButton.setText(QtGui.QApplication.translate("addClientForm", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.addClientButton.setObjectName(_fromUtf8("addClientButton"))
        self.horizontalLayout.addWidget(self.addClientButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(addClientForm)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.nameLineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(addClientForm)

    def retranslateUi(self, addClientForm):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    addClientForm = QtGui.QWidget()
    ui = Ui_addClientForm()
    ui.setupUi(addClientForm)
    addClientForm.show()
    sys.exit(app.exec_())

