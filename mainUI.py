from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)

        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(0,0,980,720))
        self.frame.setObjectName("frame")

        self.startBg = QtWidgets.QLabel(self.frame)
        self.startBg.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.startBg.setText("")
        self.startBg.setPixmap(QtGui.QPixmap("Image/Start.png"))
        self.startBg.setObjectName("startBg")

        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(980, 0, 300, 720))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Moviebt = QtWidgets.QPushButton(self.layoutWidget)
        self.Moviebt.setObjectName("Moviebt")
        self.Moviebt.setFixedSize(300, 180)
        self.Moviebt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.Moviebt)

        self.Photobt = QtWidgets.QPushButton(self.layoutWidget)
        self.Photobt.setObjectName("Photobt")
        self.Photobt.setFixedSize(300, 180)
        self.Photobt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.Photobt)

        self.Dynamicbt = QtWidgets.QPushButton(self.layoutWidget)
        self.Dynamicbt.setObjectName("Dynamicbt")
        self.Dynamicbt.setFixedSize(300, 180)
        self.Dynamicbt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.Dynamicbt)

        self.About = QtWidgets.QPushButton(self.layoutWidget)
        self.About.setObjectName("About")
        self.About.setFixedSize(300, 180)
        self.About.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.About)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "活体检测"))
        self.Moviebt.setText(_translate("MainWindow", "视频检测"))
        self.Photobt.setText(_translate("MainWindow", "拍照检测"))
        self.Dynamicbt.setText(_translate("MainWindow", "配合检测"))
        self.About.setText(_translate("MainWindow", "帮助"))
