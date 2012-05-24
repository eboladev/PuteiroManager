# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'puteiroManager.ui'
#
# Created: Thu May 24 02:38:41 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(424, 550)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setText(QtGui.QApplication.translate("MainWindow", "PuteiroManager", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.clientTab = QtGui.QWidget()
        self.clientTab.setObjectName(_fromUtf8("clientTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.clientTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.clientTableView = QtGui.QTableView(self.clientTab)
        self.clientTableView.setObjectName(_fromUtf8("clientTableView"))
        self.gridLayout_2.addWidget(self.clientTableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.clientTab, _fromUtf8(""))
        self.employeeTab = QtGui.QWidget()
        self.employeeTab.setObjectName(_fromUtf8("employeeTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.employeeTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.employeeTableView = QtGui.QTableView(self.employeeTab)
        self.employeeTableView.setObjectName(_fromUtf8("employeeTableView"))
        self.gridLayout_3.addWidget(self.employeeTableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.employeeTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setTitle(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.addClient = QtGui.QAction(MainWindow)
        self.addClient.setText(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.addClient.setObjectName(_fromUtf8("addClient"))
        self.addEmployee = QtGui.QAction(MainWindow)
        self.addEmployee.setText(QtGui.QApplication.translate("MainWindow", "Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.addEmployee.setObjectName(_fromUtf8("addEmployee"))
        self.viewClient = QtGui.QAction(MainWindow)
        self.viewClient.setText(QtGui.QApplication.translate("MainWindow", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.viewClient.setObjectName(_fromUtf8("viewClient"))
        self.viewEmployee = QtGui.QAction(MainWindow)
        self.viewEmployee.setText(QtGui.QApplication.translate("MainWindow", "Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.viewEmployee.setObjectName(_fromUtf8("viewEmployee"))
        self.actionNo_Help = QtGui.QAction(MainWindow)
        self.actionNo_Help.setText(QtGui.QApplication.translate("MainWindow", "No Help!", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNo_Help.setObjectName(_fromUtf8("actionNo_Help"))
        self.menuAdd.addAction(self.addClient)
        self.menuAdd.addAction(self.addEmployee)
        self.menuHelp.addAction(self.actionNo_Help)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addClient, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clientTab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.employeeTab), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

