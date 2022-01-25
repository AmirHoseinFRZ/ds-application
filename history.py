from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        with open("./stylesheet.qss") as file:
            stylesheet = file.read()
            MainWindow.setObjectName("MainWindow")
            MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
            MainWindow.resize(360, 502)
            MainWindow.setStyleSheet(stylesheet)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.HistoryOutput = QtWidgets.QTextEdit(self.centralwidget)
            self.HistoryOutput.setGeometry(QtCore.QRect(20, 60, 321, 411))
            self.HistoryOutput.setObjectName("HistoryOutput")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(130, 0, 91, 41))
            self.label.setObjectName("label")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dijkstra"))
        self.label.setText(_translate("MainWindow", "HISTORY"))

    def set_history(self, text):
        self.HistoryOutput.setText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
