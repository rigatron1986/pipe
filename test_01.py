def get_data(self):
    # print("test")
    all_data = self.titleEdit.currentIndex()
    print(all_data.data().toString())
    itms = self.titleEdit.selectedIndexes()[0]
    print(itms.data().toString())
    """
    for it in itms:
        print 'selected item index found at %s' % it.row()
        print 'selected item index found at %s with data: %s' % (it.row(), it.data().toString())
    """
