# PyQt4.QtGui imports
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QCursor

# PyQt4.QtGui imports
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QTextCodec

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

# sys import
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Custom Menu")

        # self.text_edit = QTextEdit()

        self.text_edit = QtGui.QTableWidget()
        QtGui.QShortcut(QtGui.QKeySequence('Ctrl+q'), self, self.test)

        rowf = 3
        self.text_edit.setColumnCount(3)
        self.text_edit.setRowCount(rowf)
        self.text_edit.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("col1"))
        self.text_edit.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("col2"))
        self.text_edit.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("col3"))

        self.text_edit.setContextMenuPolicy(Qt.CustomContextMenu)

        self.setCentralWidget(self.text_edit)
        self.text_edit.connect(self.text_edit,
                               QtCore.SIGNAL("customContextMenuRequested(QPoint)"),
                               self.context_menu)
        # self.connect(self.text_edit, SIGNAL('customContextMenuRequested(const QPoint &)'), self.context_menu)

    def context_menu(self, QPos):
        self.listMenu = QtGui.QMenu()
        menu_list = ["Update Shaders", "Shaders"]
        menu_item = self.listMenu.addAction("Update Shaders", self.test)
        menu_itemA = self.listMenu.addAction("Shaders")
        # menu_item.triggered.connect(self.menuItemClicked(menu_item))
        # self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
        self.connect(menu_itemA, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
        parentPosition = self.text_edit.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show()

    def test(self):
        print("test")

    def menuItemClicked(self):
        # print(value.text())
        action = self.sender()
        print(action.text())
        column_count = self.text_edit.rowCount()
        print(column_count)
        val = self.text_edit.currentRow()
        result = {}
        s_name = self.text_edit.item(val, 1)
        if s_name:
            result[str(s_name.text())] = {}
            for x in range(column_count):
                item = self.text_edit.item(val, x)
                if item:
                    print(self.text_edit.horizontalHeaderItem(x).text())
                    column_name = str(self.text_edit.horizontalHeaderItem(x).text())
                    result[str(s_name.text())][column_name] = item.text()
        print(result)


if __name__ == "__main__":
    # Init Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
