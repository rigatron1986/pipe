from PyQt4 import QtGui
class NewWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__()
        self._new_window = None
        self._label = QtGui.QLabel('Hello, is it me you\'re looking for?')
        To_date_label = QtGui.QLabel('To Date')
        self.To_date = QtGui.QLineEdit()
        self.To_date.installEventFilter(self)
        self.setCentralWidget(self.To_date)
    def runner(self):
        print 'asdf'
    def eventFilter(self, obj, event):
        if event.type() == event.MouseButtonPress:
            if obj == self.To_date:
                self.runner()
        return super(NewWindow, self).eventFilter(obj, event)
if __name__ == '__main__':
    app = QtGui.QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()
