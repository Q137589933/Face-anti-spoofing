from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)

        self.setUpSignInUI(MainWindow)

        self.leftFrame = QtWidgets.QFrame(MainWindow)
        self.leftFrame.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.leftFrame.setObjectName("leftFrame")

        self.startBg = QtWidgets.QLabel(self.leftFrame)
        self.startBg.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.startBg.setText("")
        self.startBg.setPixmap(QtGui.QPixmap("Icon/Start.png"))
        self.startBg.setObjectName("startBg")

        self.leftLayoutWidget = QtWidgets.QWidget(self.leftFrame)
        self.leftLayoutWidget.setGeometry(QtCore.QRect(10, 650, 300, 70))
        self.leftLayoutWidget.setObjectName("leftLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.leftLayoutWidget)
        self.horizontalLayout.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.signInBt = QtWidgets.QPushButton(self.leftLayoutWidget)
        self.signInBt.setObjectName("signInBt")
        self.signInBt.setFixedSize(100,50)
        self.signInBt.setFont(QFont("Microsoft YaHei", 14))
        self.horizontalLayout.addWidget(self.signInBt)

        self.signUpBt = QtWidgets.QPushButton(self.leftLayoutWidget)
        self.signUpBt.setObjectName("signUpBt")
        self.signUpBt.setFixedSize(100, 50)
        self.signUpBt.setFont(QFont("Microsoft YaHei", 14))
        self.horizontalLayout.addWidget(self.signUpBt)

        self.signOutBt = QtWidgets.QPushButton(self.leftLayoutWidget)
        self.signOutBt.setObjectName("signOutBt")
        self.signOutBt.setFixedSize(100, 50)
        self.signOutBt.setFont(QFont("Microsoft YaHei", 14))
        self.signOutBt.setVisible(False)
        self.horizontalLayout.addWidget(self.signOutBt)

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

        self.userLabel = QtWidgets.QLabel(self.leftFrame)
        self.userLabel.setText("????????????")
        self.userLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.userLabel.setGeometry(QtCore.QRect(700, 10, 200, 40))
        self.userLabel.setObjectName("userLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.leftFrame.setVisible(True)
        self.frame.setVisible(False)

    def setUpSignInUI(self, MainWindow):
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(340,260,300,200))
        self.frame.setObjectName("frame")

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout1.setContentsMargins(0,0,0,0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout1.setContentsMargins(0,0,0,0)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.verticalLayout1.addLayout(self.horizontalLayout1)

        self.label1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.horizontalLayout1.addWidget(self.label1)

        self.uId = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStrikeOut(False)
        self.uId.setFont(font)
        self.uId.setFixedSize(200,30)
        self.uId.setObjectName("uId")
        self.horizontalLayout1.addWidget(self.uId)

        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.verticalLayout1.addLayout(self.horizontalLayout2)

        self.label2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.horizontalLayout2.addWidget(self.label2)

        self.passWd = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setStrikeOut(False)
        self.passWd.setFont(font)
        self.passWd.setFixedSize(200, 30)
        self.passWd.setEchoMode(QLineEdit.Password)
        self.passWd.setObjectName("passWd")
        self.horizontalLayout2.addWidget(self.passWd)

        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.verticalLayout1.addLayout(self.horizontalLayout3)

        self.loginBt = QtWidgets.QPushButton(self.frame)
        self.loginBt.setFixedSize(100, 30)
        self.loginBt.setObjectName("loginBt")
        self.horizontalLayout3.addWidget(self.loginBt)

        self.backBt = QtWidgets.QPushButton(self.frame)
        self.backBt.setFixedSize(100, 30)
        self.backBt.setObjectName("backBt")
        self.horizontalLayout3.addWidget(self.backBt)

        self.label1.setText("?????????")
        self.label2.setText("?????????")
        self.loginBt.setText("??????")
        self.backBt.setText("??????")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.Moviebt.setText(_translate("MainWindow", "????????????"))
        self.Photobt.setText(_translate("MainWindow", "????????????"))
        self.Dynamicbt.setText(_translate("MainWindow", "????????????"))
        self.About.setText(_translate("MainWindow", "??????"))
        self.signUpBt.setText(_translate("MainWindow", "??????"))
        self.signInBt.setText(_translate("MainWindow", "??????"))
        self.signOutBt.setText(_translate("MainWindow", "??????"))