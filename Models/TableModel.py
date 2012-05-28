import sqlite3
import sys
import Models.DefaultModel as m
from PyQt4 import *
"""
class Clients(m.DefaultModel):
	self._table = 'clients'
"""
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self,datas = [[]],headers = [], parent = None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__datas = datas
        self.__headers = headers

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section<len(self.__headers):
                    return self.__headers[section]
                else:
                    return "TEMP"
        
    def rowCount(self, parent):
        return len(self.__datas)
    
    def columnCount(self, parent):
        return len(self.__datas[0])
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    
    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__datas[row][column]
        
        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return self.__datas[row][column]
        
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__datas[row][column]
            return value
    
    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            color = value
            if color.isValid():
                self.__datas[row][column] = color
                self.dataChanged.emit(index, index)
                return True
        return False
    
    """
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows -1)
        for i in range(rows):
            defaultValues = [QtGui.QColor("#000000") for i in range(self.columnCount(None))]
            self.__datas.insert(position, defaultValues)
        self.endInsertRows()
        return True
    
    def insertColumns(self, position, columns, parent = QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns -1)
        rowCount = len(self.__datas)
        for i in range(columns):
            for j in range(rowCount):
                self.__datas[j].insert(position, QtGui.QColor("#000000"))
        self.endInsertColumns()
        return True
    """
    
