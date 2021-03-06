from PyQt5 import QtCore, QtGui, QtWidgets
from convertor_page import Ui_MainWindow
from sort_page import Ui_MainWindow3


class Ui_MainWindow0(object):
    def open_convertor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_sort(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):

        with open("./stylesheet.qss") as file:
            stylesheet = file.read()
            MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(280, 268)
            MainWindow.setStyleSheet(stylesheet)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.Convertor = QtWidgets.QPushButton(self.centralwidget)
            self.Convertor.setGeometry(QtCore.QRect(70, 65, 141, 61))
            self.Convertor.setObjectName("Convertor")
            self.Sort = QtWidgets.QPushButton(self.centralwidget)
            self.Sort.setGeometry(QtCore.QRect(70, 140, 141, 61))
            self.Sort.setObjectName("Sort")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(74, 15, 150, 30))
            self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";")
            self.label.setObjectName("label")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
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
        self.Convertor.setText(_translate("MainWindow", "Convertor"))
        self.Sort.setText(_translate("MainWindow", "Sorter"))
        self.label.setText(_translate("MainWindow", "  Select a button"))

        self.Convertor.clicked.connect(self.open_convertor)
        self.Sort.clicked.connect(self.open_sort)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow0()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
