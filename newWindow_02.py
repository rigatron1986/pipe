import sys
from PyQt4 import QtGui
import qdarkstyle


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.statusBar().showMessage('Ready')
        username_label = QtGui.QLabel("Username :")
        password_label = QtGui.QLabel("Password :")
        _username = QtGui.QLineEdit()
        _password = QtGui.QLineEdit()
        Main_grid_layout = QtGui.QGridLayout()
        # Set the stretch
        Main_grid_layout.setColumnStretch(0, 1)
        Main_grid_layout.setColumnStretch(3, 1)
        Main_grid_layout.setRowStretch(0, 1)
        Main_grid_layout.setRowStretch(3, 1)
        # Add widgets
        Main_grid_layout.addWidget(username_label, 1, 1)
        Main_grid_layout.addWidget(password_label, 2, 1)
        Main_grid_layout.addWidget(_username, 1, 2)
        Main_grid_layout.addWidget(_password, 2, 2)

        """
        test
        """

        username_label1 = QtGui.QLabel("Username :")
        password_label1 = QtGui.QLabel("Password :")
        _username1 = QtGui.QLineEdit()
        _password1 = QtGui.QLineEdit()
        Main_grid_layout1 = QtGui.QGridLayout()
        # Set the stretch
        Main_grid_layout1.setColumnStretch(0, 1)
        Main_grid_layout1.setColumnStretch(3, 1)
        Main_grid_layout1.setRowStretch(0, 1)
        Main_grid_layout1.setRowStretch(3, 1)
        # Add widgets
        Main_grid_layout1.addWidget(username_label1, 1, 1)
        Main_grid_layout1.addWidget(password_label1, 2, 1)
        Main_grid_layout1.addWidget(_username1, 1, 2)
        Main_grid_layout1.addWidget(_password1, 2, 2)
        widgetA = QtGui.QWidget()
        widgetA.setLayout(Main_grid_layout)
        widgetB = QtGui.QWidget()
        widgetB.setLayout(Main_grid_layout1)
        combined = QtGui.QGridLayout()
        combined.addWidget(widgetA, 0, 0, 1, 1)
        combined.addWidget(widgetB, 0, 1, 1, 1)

        main_widget = QtGui.QWidget()
        # main_widget.setLayout(Main_grid_layout)
        main_widget.setLayout(combined)

        self.setCentralWidget(main_widget)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Project Estimate')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
