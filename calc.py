'''
1. qt控件基本编排
2. 槽函数连接通过 partial 传参数
3. pyinstaller 转为 exe 文件，注意 exe 文件较大
4. 获取到的 text 都是字符串，要转换过（跟 C# 一样）
5. 设计时 业务代码 分离
'''

# 要复制
from sys import exit
from PyQt5 import QtCore, QtWidgets
from functools import partial
from math import sqrt

class Ui_mainWindow(QtWidgets.QMainWindow):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(451, 342)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 74, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 200, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 220, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 220, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        mainWindow.setCentralWidget(self.centralwidget)
        mainWindow.setWindowTitle("MasterCable")
        self.label.setText("a")
        self.label_2.setText("b")
        self.label_3.setText("c")
        self.pushButton.setText("求解")
        self.label_4.setText("x1")
        self.label_5.setText("x2")

        # 要复制
        self.my_own_link()

    # 要复制，业务代码，接受各信号的槽函数。要传参数怎么办？ 答：用 partial
    def calc(self, str, str2):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        c = int(self.lineEdit_3.text())
        delta = b*b - 4*a*c
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        self.lineEdit_4.setText("%.4f"%x1)
        self.lineEdit_5.setText("%.4f"%x2)
        self.pushButton.setText(str)
        self.label.setText(str2)

    # 要复制，所有槽函数都在这里进行连接，注意 partial
    def my_own_link(self):
        self.pushButton.clicked.connect(  partial(self.calc, "hello", "world")  )

# 要复制
if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 传一个空字符串数组
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    exit(app.exec_())
