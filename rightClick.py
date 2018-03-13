from PyQt4 import QtCore, QtGui

self.AssetsListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
self.AssetsListWidget.connect(self.AssetsListWidget,
                              QtCore.SIGNAL("customContextMenuRequested(QPoint)"),
                              self.listItemRightClicked)


def listItemRightClicked(self, QPos):
    self.listMenu = QtGui.QMenu()
    menu_item = self.listMenu.addAction("Update Shaders")
    menu_itemA = self.listMenu.addAction("Shaders")
    self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
    self.connect(menu_itemA, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
    parentPosition = self.AssetsListWidget.mapToGlobal(QtCore.QPoint(0, 0))
    self.listMenu.move(parentPosition + QPos)
    self.listMenu.show()


def menuItemClicked(self):
    currentItemName = str(self.AssetsListWidget.currentItem().text())
    print currentItemName
