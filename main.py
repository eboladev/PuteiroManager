#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import puteiroManager, addClientForm
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = puteiroManager.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #sys.exit(app.exec_())
    addClient = QtGui.QWidget()
    ui = addClientForm.Ui_addClientForm()
    ui.setupUi(addClient)
    addClient.show()
    sys.exit(app.exec_())
