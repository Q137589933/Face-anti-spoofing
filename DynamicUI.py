from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class Ui_Dynamic(object):
    def setupUi(self, Dynamic):
        Dynamic.setFixedSize(1280, 720)
        Dynamic.setWindowFlags(Qt.WindowCloseButtonHint)
        Dynamic.setObjectName("dynamic")

        self.frame = QtWidgets.QFrame(Dynamic)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.centralLayout = QtWidgets.QWidget(self.frame)
        self.centralLayout.setGeometry(QtCore.QRect(240,0,800,600))
        self.centralLayout.setObjectName("centralLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralLayout)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.MsgLb = QtWidgets.QLabel(self.centralLayout)
        self.MsgLb.setText("")
        self.MsgLb.setFixedSize(800, 100)
        self.MsgLb.setFont(QFont("Microsoft YaHei", 16))
        self.verticalLayout.addWidget(self.MsgLb)

        self.ShowLb = QtWidgets.QLabel(self.centralLayout)
        self.ShowLb.setFixedSize(800, 500)
        self.ShowLb.setText("")
        self.ShowLb.setPixmap(QtGui.QPixmap("Image/tips.jpg"))
        self.ShowLb.setObjectName("ShowLb")
        self.verticalLayout.addWidget(self.ShowLb)

        self.layoutWidget = QtWidgets.QWidget(Dynamic)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 600, 1280, 120))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.StartBt = QtWidgets.QPushButton(self.layoutWidget)
        self.StartBt.setObjectName("StartBt")
        self.StartBt.setFixedSize(300,80)
        self.StartBt.setFont(QFont("Microsoft YaHei", 14))
        self.horizontalLayout.addWidget(self.StartBt)

        self.ReturnBt = QtWidgets.QPushButton(self.layoutWidget)
        self.ReturnBt.setObjectName("ReturnBt")
        self.ReturnBt.setFixedSize(300,80)
        self.ReturnBt.setFont(QFont("Microsoft YaHei", 14))
        self.horizontalLayout.addWidget(self.ReturnBt)

        self.retranslateUi(Dynamic)
        QtCore.QMetaObject.connectSlotsByName(Dynamic)

    def retranslateUi(self, Dynamic):
        _translate = QtCore.QCoreApplication.translate
        Dynamic.setWindowTitle(_translate("dynamic", "动态检测"))
        self.StartBt.setText(_translate("dynamic", "开始"))
        self.ReturnBt.setText(_translate("dynamic", "返回"))
