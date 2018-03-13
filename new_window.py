from PyQt4 import QtGui


class NewWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent=parent)
        self._new_window = None
        self._label = QtGui.QLabel('Hello, is it me you\'re looking for?')

        self.setCentralWidget(self._label)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
