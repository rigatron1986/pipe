from PyQt4 import QtGui, QtCore
import sys
import pipeline.core.utilities as utilities


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        edit = QtGui.QLineEdit()
        completer = QtGui.QCompleter()
        edit.setCompleter(completer)
        model = QtGui.QStringListModel()
        completer.setModel(model)
        self.get_data(model)
        self.setCentralWidget(edit)

    @staticmethod
    def get_data(model):
        expr = "@GET(sthpw/login['license_type','user'].code)"
        # users = utilities.Tactic().databaseQuery(expr)
        model.setStringList(["completion", "data", "goes", "here"])
        # model.setStringList(users)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
