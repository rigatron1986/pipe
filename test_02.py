from mmSilhouetteviewerUI import Ui_MainWindow
from qtswitch import QtGui
import sys
# importing the dialog ui
from test_04 import SilhouetteWindowA


class SilhouetteWindow(QtGui.QMainWindow, Ui_MainWindow):
    """UI to Silhouetteviewer by given information."""

    def __init__(self, parents=None):
        """
        Initialise.

        """
        # cmds.select(clear=True)
        super(SilhouetteWindow, self).__init__(parents)
        self.setupUi(self)
        self.setWindowTitle('Silhouette Viewer')
        self.add_selected_btn.clicked.connect(lambda: self.runner())

    def runner(self):
        print(SilhouetteWindowA.isOkay('asdf', self))


app = QtGui.QApplication([])
MM_SVE = SilhouetteWindow()
MM_SVE.show()
sys.exit(app.exec_())
