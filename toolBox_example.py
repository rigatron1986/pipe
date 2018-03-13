from PyQt4 import QtCore, QtGui
import qdarkstyle


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # all_list = ['tes', 'ted', 'cb', 'gh', 'hf']
        all_list = {'test': 'this is a test', 'value': 'this is a value'}
        self.toolbox = QtGui.QToolBox(self)
        for key, value in all_list.items():
            subTool = QtGui.QWidget()
            self.toolbox.addItem(subTool, key)
            self.gridLayout = QtGui.QGridLayout(subTool)
            self.listWidget = QtGui.QListWidget(subTool)
            self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
            self.listWidget.addItem(value)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.toolbox)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    window = Window()
    window.setGeometry(500, 300, 300, 300)
    window.show()
    sys.exit(app.exec_())
