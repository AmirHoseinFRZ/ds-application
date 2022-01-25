from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        with open("./stylesheet.qss") as file:
            stylesheet = file.read()
            MainWindow.setObjectName("MainWindow")
            MainWindow.setWindowIcon(QtGui.QIcon('ico.png'))
            MainWindow.resize(485, 520)
            MainWindow.setStyleSheet(stylesheet)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.BubbleSort = QtWidgets.QPushButton(self.centralwidget)
            self.BubbleSort.setGeometry(QtCore.QRect(10, 10, 161, 61))
            self.BubbleSort.setObjectName("BubbleSort")
            self.InsertionSort = QtWidgets.QPushButton(self.centralwidget)
            self.InsertionSort.setGeometry(QtCore.QRect(10, 80, 161, 61))
            self.InsertionSort.setObjectName("InsertionSort")
            self.SelectionSort = QtWidgets.QPushButton(self.centralwidget)
            self.SelectionSort.setGeometry(QtCore.QRect(10, 150, 161, 61))
            self.SelectionSort.setObjectName("SelectionSort")
            self.MergeSort = QtWidgets.QPushButton(self.centralwidget)
            self.MergeSort.setGeometry(QtCore.QRect(10, 220, 161, 61))
            self.MergeSort.setObjectName("MergeSort")
            self.QuickSort = QtWidgets.QPushButton(self.centralwidget)
            self.QuickSort.setGeometry(QtCore.QRect(10, 290, 161, 61))
            self.QuickSort.setObjectName("QuickSort")
            self.CountingSort = QtWidgets.QPushButton(self.centralwidget)
            self.CountingSort.setGeometry(QtCore.QRect(10, 360, 161, 61))
            self.CountingSort.setObjectName("CountingSort")
            self.BucketSort = QtWidgets.QPushButton(self.centralwidget)
            self.BucketSort.setGeometry(QtCore.QRect(10, 430, 161, 61))
            self.BucketSort.setObjectName("BucketSort")
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
            self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 21))
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
        self.BubbleSort.setText(_translate("MainWindow", "Bubble Sort"))
        self.InsertionSort.setText(_translate("MainWindow", "Insertion Sort"))
        self.SelectionSort.setText(_translate("MainWindow", "Selection Sort"))
        self.MergeSort.setText(_translate("MainWindow", "Merge Sort"))
        self.QuickSort.setText(_translate("MainWindow", "Quick Sort"))
        self.CountingSort.setText(_translate("MainWindow", "Couting Sort"))
        self.BucketSort.setText(_translate("MainWindow", "Bucket Sort"))
        self.label.setText(_translate("MainWindow", "input"))
        self.label_2.setText(_translate("MainWindow", "output"))

        # -------------------------- connect buttons to functions -------------------
        self.BubbleSort.clicked.connect(self.bubbleSort)
        self.InsertionSort.clicked.connect(self.insertionSort)
        self.SelectionSort.clicked.connect(self.selectionSort)
        self.QuickSort.clicked.connect(self.quick_sort)
        self.CountingSort.clicked.connect(self.counting_sort)
        self.MergeSort.clicked.connect(self.merge_sort)
        self.BucketSort.clicked.connect(self.bucket_sort)

    def bubbleSort(self):
        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        sorted = []
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                string = " ".join(map(str, arr))
                if len(sorted) > 0:
                    if sorted[-1] != string:
                        sorted.append(string)
                else:
                    sorted.append(string)
        self.output.setText("\n".join(sorted))

    def insertionSort(self):
        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        sorted = []
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            string = " ".join(map(str, arr))
            if len(sorted) > 0:
                if sorted[-1] != string:
                    sorted.append(string)
            else:
                sorted.append(string)
        self.output.setText("\n".join(sorted))

    def selectionSort(self):
        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        sorted = []
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            string = " ".join(map(str, arr))
            if len(sorted) > 0:
                if sorted[-1] != string:
                    sorted.append(string)
            else:
                sorted.append(string)
        self.output.setText("\n".join(sorted))

    def quick_sort(self):
        sorted = []
        def qsort(arr):
            from random import randint
            if len(arr) < 2:
                return arr
            low, same, high = [], [], []
            pivot = arr[randint(0, len(arr) - 1)]
            sorted.append("pivot : " + str(pivot))
            for i in arr:
                if i < pivot:
                    low.append(i)
                elif i == pivot:
                    same.append(i)
                elif i > pivot:
                    high.append(i)
            sorted.append("smaller : " + " ".join(map(str, low)))
            sorted.append("bigger  : " + " ".join(map(str, high)))
            return qsort(low) + same + qsort(high)

        ar = self.Input.text().split()
        ar = list(map(cast, ar))
        sorted.append("sorted : " + " ".join(map(str, qsort(ar))))
        self.output.setText("\n".join(sorted))

    def counting_sort(self):
        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        sorted = []
        c = []
        size = len(arr)
        output = [0] * size
        count = [0] * 10
        for i in range(0, size):
            count[arr[i]] += 1
        c = count.copy()
        sorted.append("output : " + " ".join(map(str, output)))
        sorted.append("count  : " + " ".join(map(str, count)))
        for j in range(1, 10):
            count[j] += count[j-1]
        a = size - 1
        while a >= 0:
            output[count[arr[a]] - 1] = arr[a]
            sorted.append("output : " + " ".join(map(str, output)))
            count[arr[a]] -= 1
            c[arr[a]] -= 1
            sorted.append("count  : " + " ".join(map(str, c)))
            a -= 1
        for k in range(0, size):
            arr[k] = output[k]
        self.output.setText("\n".join(sorted))

    def merge_sort(self):
        sorted = []

        def merge(left, right):
            if len(left) == 0:
                return right
            if len(right) == 0:
                return left
            result = []
            l_ind = r_ind = 0
            while len(result) < len(left) + len(right):
                if left[l_ind] <= right[r_ind]:
                    result.append(left[l_ind])
                    l_ind += 1
                else:
                    result.append(right[r_ind])
                    r_ind += 1

                if r_ind == len(right):
                    result += left[l_ind:]
                    break
                if l_ind == len(left):
                    result += right[r_ind:]
                    break
            return result

        def msort(arr):
            if len(arr) < 2:
                return arr
            mp = len(arr) // 2
            sorted.append(" ".join(map(str, arr[:mp])) + " , " + " ".join(map(str, arr[mp:])))
            return merge(left=msort(arr[:mp]), right=msort(arr[mp:]))

        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        sorted.append("sorted : " + " ".join(map(str, msort(arr))))
        self.output.setText("\n".join(sorted))


    def bucket_sort(self):
        sorted = []

        def bsort(arr, noOfBuckets):
            max_ele = max(arr)
            min_ele = min(arr)
            rnge = (max_ele - min_ele) / noOfBuckets
            temp = []
            for i in range(noOfBuckets):
                temp.append([])
            for i in range(len(arr)):
                diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
                if diff == 0 and arr[i] != min_ele:
                    temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
                else:
                    temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
            for i in range(len(temp)):
                sorted.append("bucket " + str(i + 1) + ": " + " ".join(map(str, temp[i])))
            for i in range(len(temp)):
                if len(temp[i]) != 0:
                    bubbleSort(temp[i])
            for i in range(len(temp)):
                sorted.append("sorted bucket " + str(i + 1) + ": " + " ".join(map(str, temp[i])))
            k = 0
            for lst in temp:
                if lst:
                    for i in lst:
                        arr[k] = i
                        k = k + 1

        def bubbleSort(arr):
            n = len(arr)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        arr = self.Input.text().split()
        arr = list(map(cast, arr))
        noOfBuckets = 5
        bsort(arr, noOfBuckets)
        sorted.append("sorted : " + " ".join(map(str, arr)))
        self.output.setText("\n".join(sorted))

def cast(x):
    if "." in x:
        return float(x)
    return int(x)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
