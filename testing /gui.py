# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Nov 22 08:59:07 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.Pages = QtGui.QListView(self.dockWidgetContents)
        self.Pages.setGeometry(QtCore.QRect(0, 0, 111, 271))
        self.Pages.setObjectName(_fromUtf8("Pages"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(307, 0, 91, 27))
        self.pushButton.setObjectName(_fromUtf8("Exit"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 30, 91, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def on_click_1():
        self.pushButton.clicked.conect(exit)
    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget", None))
        self.pushButton.setText(_translate("DockWidget", "Exit", None))
        self.pushButton_2.setText(_translate("DockWidget", "PushButton", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DockWidget = QtGui.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

