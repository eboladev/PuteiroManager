from PyQt4.Qt import *

class Table_Helper(QTableWidget):
    def __init__(self, parent, thestruct, labels):
        QTableWidget.__init__(self, parent)
        self.setColumnCount(len(thestruct[0]))
        self.setRowCount(len(thestruct))
        self.setHorizontalHeaderLabels(labels)	
        self.data = thestruct
        self.setmydata()
    def setmydata(self):
        n = 0
        for person in self.data:
            m = 0
            for item in person:
                newitem = QTableWidgetItem(str(item))
                self.setItem(n, m, newitem)
                m += 1
            n += 1