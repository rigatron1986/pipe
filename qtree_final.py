from PyQt4 import QtGui


class NewWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent=parent)
        self._new_window = None
        # self._label = QtGui.QLabel('Hello, is it me you\'re looking for?')
        self.treeView = QtGui.QTreeView(self)
        self.treeView.setObjectName("treeView")

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['shot name', 'work hrs', 'wage'])
        self.treeView.setModel(model)
        self.treeView.setUniformRowHeights(True)
        self.data = {
            "shot_01": [{"user": "raj", "hrs": [5, 6], "wage": 100}, {"user": "rajA", "hrs": [15, 6], "wage": 1100}],
            "shot_02": [{"user": "vick", "hrs": [2, 8], "wage": 250}, {"user": "vickA", "hrs": [12, 8], "wage": 2250}]}
        # self.data = {"shot_01": [["a", "b"], {"user": "raj"}], "shot_02": [["c", "d"], {"user": "vick"}]}
        # for key, value in self.data.iteritems():
        for key, value in self.data.iteritems():
            # print key
            col1 = QtGui.QStandardItem(key)
            total_hrs = []
            for one in value:
                row1 = QtGui.QStandardItem(one["user"])
                total_hrs.append(sum(one["hrs"]))
                row2 = QtGui.QStandardItem(str(sum(one["hrs"])))
                row3 = QtGui.QStandardItem(one["wage"])
                col1.appendRow([row1, row2, row3])
            col2 = QtGui.QStandardItem(str(sum(total_hrs)))
            model.appendRow([col1, col2])

        self.setCentralWidget(self.treeView)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
