import sys
from PyQt4 import QtGui, QtCore
import qdarkstyle
import pipeline.tools.playA as example_ui
def main():
    # create the application and the main window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    # setup ui
    self = example_ui.Ui_MainWindow()
    self.setupUi(window)
    item = QtGui.QTableWidgetItem("Test")
    item.setCheckState(QtCore.Qt.Checked)
    # ui.tableWidget.setItem(0, 0, item)
    window.setWindowTitle("QDarkStyle example")
    window.setWindowTitle("QDarkStyle example")
    # tabify dock widgets to show bug #6
    self.okButton.clicked.connect(lambda: test(self))
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    # run
    window.show()
    app.exec_()
def test(self):
    self.cancelButton.setText('asdf')
    print 'atsd'
if __name__ == "__main__":
    main()