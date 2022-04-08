from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_Photo(object):
    def setupUi(self, Photo):
        Photo.setObjectName("Photo")
        Photo.resize(1280, 720)

        self.frame = QtWidgets.QFrame(Photo)
        self.frame.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.ShowLb = QtWidgets.QLabel(self.frame)
        self.ShowLb.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.ShowLb.setText("")
        self.ShowLb.setPixmap(QtGui.QPixmap("../Image/tips.png"))
        self.ShowLb.setObjectName("ShowLb")

        self.layoutWidget = QtWidgets.QWidget(Photo)
        self.layoutWidget.setGeometry(QtCore.QRect(980, 0, 300, 720))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.PhotoBt = QtWidgets.QPushButton(self.layoutWidget)
        self.PhotoBt.setObjectName("PhotoBt")
        self.PhotoBt.setFixedSize(300,180)
        self.PhotoBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.PhotoBt)

        self.FileBt = QtWidgets.QPushButton(self.layoutWidget)
        self.FileBt.setObjectName("FileBt")
        self.FileBt.setFixedSize(300,180)
        self.FileBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.FileBt)

        self.StartBt = QtWidgets.QPushButton(self.layoutWidget)
        self.StartBt.setObjectName("StartBt")
        self.StartBt.setFixedSize(300,180)
        self.StartBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.StartBt)

        self.ReturnBt = QtWidgets.QPushButton(self.layoutWidget)
        self.ReturnBt.setObjectName("ReturnBt")
        self.ReturnBt.setFixedSize(300,180)
        self.ReturnBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.ReturnBt)

        self.retranslateUi(Photo)
        QtCore.QMetaObject.connectSlotsByName(Photo)

    def retranslateUi(self, Photo):
        _translate = QtCore.QCoreApplication.translate
        Photo.setWindowTitle(_translate("Photo", "照片检测"))
        self.FileBt.setText(_translate("Photo", "上传"))
        self.PhotoBt.setText(_translate("Photo", "拍照"))
        self.StartBt.setText(_translate("Photo", "开始"))
        self.ReturnBt.setText(_translate("Photo", "返回"))
