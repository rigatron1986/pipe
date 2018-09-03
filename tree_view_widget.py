from PyQt4 import QtGui


class NewWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent=parent)
        self._new_window = None
        # self._label = QtGui.QLabel('Hello, is it me you\'re looking for?')
        self.treeView = QtGui.QTreeView(self)
        self.treeView.setObjectName("treeView")

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
        self.treeView.setModel(model)
        self.treeView.setUniformRowHeights(True)

        col1 = QtGui.QStandardItem('col entry1')
        col2 = QtGui.QStandardItem('col entry2')
        col3 = QtGui.QStandardItem('col entry3')

        row1 = QtGui.QStandardItem('row1')
        row2 = QtGui.QStandardItem('row2')
        row3 = QtGui.QStandardItem('row3')
        col1.appendRow([row1, row2, row3])

        model.appendRow([col1, col2, col3])

        col4 = QtGui.QStandardItem('col entry1')
        col5 = QtGui.QStandardItem('col entry2')
        col6 = QtGui.QStandardItem('col entry3')
        model.appendRow([col4, col5, col6])

        row4 = QtGui.QStandardItem('row1')
        row5 = QtGui.QStandardItem('row2')
        row6 = QtGui.QStandardItem('row3')
        col4.appendRow([row4, row5, row6])

        self.setCentralWidget(self.treeView)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
