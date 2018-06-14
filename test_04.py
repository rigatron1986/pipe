from qtswitch import QtGui
import sys
from untitled import Ui_Dialog


class SilhouetteWindowA(QtGui.QDialog, Ui_Dialog):
    """UI to Silhouetteviewer by given information."""

    def __init__(self, checkname, parents=None):
        """
        Initialise.

        """
        # cmds.select(clear=True)
        super(SilhouetteWindowA, self).__init__(parents)
        self.setupUi(self)
        self.setWindowTitle('Silhouette Viewer')
        self.okbtn = False
        # self.add_selected_btn.clicked.connect(lambda: self.runner())
        self.pushButton.clicked.connect(lambda: self.button_press())
        self.pushButton_2.clicked.connect(lambda: self.button_press())
        self.checkBox.setText(checkname)

    def pushA(self):
        self.okbtn = True
        print self.okbtn

    def button_press(self):
        if self.sender() == self.pushButton:
            self.okbtn = True
        self.close()

    @classmethod
    def isOkay(cls, chk_nam, parent=None):
        dialog = cls(chk_nam, parent)
        dialog.exec_()
        result = [dialog.okbtn, dialog.checkBox.isChecked()]
        return result

"""
app = QtGui.QApplication([])
print(SilhouetteWindowA.isOkay('asdf'))
sys.exit(app.exec_())

"""
