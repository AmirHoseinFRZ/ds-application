from PyQt5 import QtCore, QtGui, QtWidgets
from expression import Expression
from expression import infix_to_postfix, infix_to_prefix
from expression import postfix_to_infix, postfix_to_prefix
from expression import prefix_to_infix, prefix_to_postfix
from expression import isvalid, split_checker
from history import Ui_MainWindow4


class Ui_MainWindow(object):
    dic = [["infix to postfix", 0],
           ["infix to prefix", 0],
           ["postfix to infix", 0],
           ["postfix to prefix", 0],
           ["prefix to infix", 0],
           ["prefix to postfix", 0]]
    def open_history(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self.window)
        self.ui.HistoryOutput.setText("\n".join(Ui_MainWindow.get_dic()))
        self.window.show()

    def setupUi(self, MainWindow):
        with open("./stylesheet.qss") as file:
            stylesheet = file.read()
            MainWindow.setObjectName("MainWindow")
            MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
            MainWindow.resize(485, 520)
            MainWindow.setStyleSheet(stylesheet)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.in2post = QtWidgets.QPushButton(self.centralwidget)
            self.in2post.setGeometry(QtCore.QRect(10, 10, 161, 61))
            self.in2post.setObjectName("in2post")
            self.in2pre = QtWidgets.QPushButton(self.centralwidget)
            self.in2pre.setGeometry(QtCore.QRect(10, 80, 161, 61))
            self.in2pre.setObjectName("in2pre")
            self.post2in = QtWidgets.QPushButton(self.centralwidget)
            self.post2in.setGeometry(QtCore.QRect(10, 150, 161, 61))
            self.post2in.setObjectName("post2in")
            self.post2pre = QtWidgets.QPushButton(self.centralwidget)
            self.post2pre.setGeometry(QtCore.QRect(10, 220, 161, 61))
            self.post2pre.setObjectName("post2pre")
            self.pre2in = QtWidgets.QPushButton(self.centralwidget)
            self.pre2in.setGeometry(QtCore.QRect(10, 290, 161, 61))
            self.pre2in.setObjectName("pre2in")
            self.pre2post = QtWidgets.QPushButton(self.centralwidget)
            self.pre2post.setGeometry(QtCore.QRect(10, 360, 161, 61))
            self.pre2post.setObjectName("pre2post")
            self.history = QtWidgets.QPushButton(self.centralwidget)
            self.history.setGeometry(QtCore.QRect(10, 430, 161, 61))
            self.history.setObjectName("history")
            self.Input = QtWidgets.QLineEdit(self.centralwidget)
            self.Input.setGeometry(QtCore.QRect(200, 30, 265, 40))
            self.Input.setObjectName("Input")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(200, -5, 70, 35))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(200, 70, 70, 35))
            self.label_2.setObjectName("label_2")
            self.output = QtWidgets.QTextEdit(self.centralwidget)
            self.output.setGeometry(QtCore.QRect(200, 105, 265, 380))
            self.output.setObjectName("output")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
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
        self.in2post.setText(_translate("MainWindow", "Infix to Postfix"))
        self.in2pre.setText(_translate("MainWindow", "Infix to Prefix"))
        self.post2in.setText(_translate("MainWindow", "Postfix to Infix"))
        self.post2pre.setText(_translate("MainWindow", "Postfix to Prefix"))
        self.pre2in.setText(_translate("MainWindow", "Prefix to Infix"))
        self.pre2post.setText(_translate("MainWindow", "Prefix to Postfix"))
        self.history.setText(_translate("MainWindow", "History"))
        self.label.setText(_translate("MainWindow", "Input"))
        self.label_2.setText(_translate("MainWindow", "Output"))

        # -------------- connect buttons to functions -------------------
        self.in2post.clicked.connect(self.i2po)
        self.in2pre.clicked.connect(self.i2pr)
        self.post2in.clicked.connect(self.po2i)
        self.post2pre.clicked.connect(self.po2pr)
        self.pre2in.clicked.connect(self.pr2i)
        self.pre2post.clicked.connect(self.pr2po)
        self.history.clicked.connect(self.open_history)

    def i2po(self):
        exp = Expression(self.Input.text(), "infix")
        x = infix_to_postfix(exp.phrase)
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(x))
                i = get_index(self.dic, "infix to postfix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    def i2pr(self):
        exp = Expression(self.Input.text(), "infix")
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(infix_to_prefix(exp.phrase)))
                i = get_index(self.dic, "infix to prefix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    def po2i(self):
        exp = Expression(self.Input.text(), "postfix")
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(postfix_to_infix(exp.phrase)))
                i = get_index(self.dic, "postfix to infix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    def po2pr(self):
        exp = Expression(self.Input.text(), "postfix")
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(postfix_to_prefix(exp.phrase)))
                i = get_index(self.dic, "postfix to prefix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    def pr2i(self):
        exp = Expression(self.Input.text(), "prefix")
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(prefix_to_infix(exp.phrase)))
                i = get_index(self.dic, "prefix to infix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    def pr2po(self):
        exp = Expression(self.Input.text(), "prefix")
        if split_checker(exp.phrase):
            if isvalid(exp):
                self.output.setText("\n".join(prefix_to_postfix(exp.phrase)))
                i = get_index(self.dic, "prefix to postfix")
                self.dic[i][1] += 1
                sorting(i, self.dic)
            else:
                self.output.setText("Invalid type of input!")
        else:
            self.output.setText("please separate tokens with one space!")

    @staticmethod
    def get_dic():
        arr = Ui_MainWindow.dic.copy()
        final = []
        for i in range(6):
            if arr[i][1] != 0:
                final.append(arr[i][0] + " : " + str(arr[i][1]))
        return final


def get_index(l, string):
    for i in range(len(l)):
        if string == l[i][0]:
            return i


def sorting(j, arr):
    while j > 0:
        if arr[j][1] >= arr[j - 1][1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
