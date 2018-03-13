from PyQt4 import QtGui, QtCore
from random import randint

list1 = ['vr2', 'rub']


class PaintPicture(QtGui.QDialog):
    def __init__(self, parent=None):
        super(PaintPicture, self).__init__()
        self.user_choice = None
        self.gridLayout = QtGui.QGridLayout()
        self.img_btn = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok,
                                              QtCore.Qt.Horizontal, self)
        self.img_btn.accepted.connect(self.accept)
        # self.img_btn.rejected.connect(self.reject)
        self.img_btn.clicked.connect(self.close)
        image_no = randint(0, 2)
        filenameA = "D:/toexe/tacticCheckin/dist/memes/{0}/{1}.png".format('idiotic', image_no)
        filenameA = filenameA.replace('/', '\\')
        # image = QtGui.QPixmap(filenameA)
        self.Label = QtGui.QLabel()
        self.Label.setText('test')
        self.comboBox = QtGui.QComboBox()
        # self.imageLabel.setPixmap(image)
        for li in list1:
            self.comboBox.addItem(li)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.Label, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.img_btn, 1, 2, 1, 2)
        self.setLayout(self.gridLayout)
        self.show()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent=None):
        dialog = PaintPicture(parent)
        result = dialog.exec_()
        # date = dialog.dateTime()
        # return result == QtGui.QDialog.Accepted
        return result == QtGui.QComboBox.currentText()


app = QtGui.QApplication([])
ok = PaintPicture.getDateTime()
print("{}".format(ok))
app.exec_()
