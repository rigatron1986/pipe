from PyQt4 import QtGui, QtCore, uic
import sys
import time


class CalWidget(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(CalWidget, self).__init__(parent)
        self.calButton = QtGui.QToolButton(self)
        self.calButton.setIcon(QtGui.QIcon('balloontip.ico'))
        self.calButton.setStyleSheet('border: 0px; padding: 0px;')
        self.calButton.setCursor(QtCore.Qt.ArrowCursor)
        self.calButton.clicked.connect(self.showCalWid)

    def resizeEvent(self, event):
        buttonSize = self.calButton.sizeHint()
        frameWidth = self.style().pixelMetric(QtGui.QStyle.PM_DefaultFrameWidth)
        self.calButton.move(self.rect().right() - frameWidth - buttonSize.width(),
                            (self.rect().bottom() - buttonSize.height() + 1) / 2)
        super(CalWidget, self).resizeEvent(event)

    def showCalWid(self):
        self.calendar = QtGui.QCalendarWidget()
        self.calendar.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QtCore.QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate)
        self.calendar.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.calendar.setStyleSheet('background: white; color: black')
        self.calendar.setGridVisible(True)
        pos = QtGui.QCursor.pos()
        self.calendar.setGeometry(pos.x(), pos.y(), 300, 200)
        self.calendar.show()

    def updateDate(self, *args):
        getDate = self.calendar.selectedDate().toString()
        print time.strptime(self.calendar.selectedDate(),"%d/%m/%Y")
        self.setText(getDate)
        self.calendar.deleteLater()


class MainDialog(QtGui.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        centralwidget = QtGui.QWidget(self)
        centralwidget.setStyleSheet('background: grey; color: blue')
        self.layout = QtGui.QHBoxLayout(centralwidget)
        self.calButton = CalWidget()
        self.layout.addWidget(self.calButton)
        self.setCentralWidget(centralwidget)


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
