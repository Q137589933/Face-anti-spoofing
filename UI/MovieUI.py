from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

class Ui_Movie(object):
    def setupUi(self, Movie):
        Movie.setObjectName("Movie")
        Movie.resize(1280, 720)

        self.frame = QtWidgets.QFrame(Movie)
        self.frame.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.ShowLb = QtWidgets.QLabel(self.frame)
        self.ShowLb.setGeometry(QtCore.QRect(0, 0, 980, 720))
        self.ShowLb.setText("")
        self.ShowLb.setPixmap(QtGui.QPixmap("../Image/tips.png"))
        self.ShowLb.setObjectName("ShowLb")

        self.rePlayBt = QtWidgets.QPushButton(self.frame)
        self.rePlayBt.setGeometry(QtCore.QRect(50,620,100,50))
        self.rePlayBt.setObjectName("replayBt")

        self.processBar = QtWidgets.QProgressBar(self.frame)
        self.processBar.setGeometry(QtCore.QRect(200, 650, 700, 30))
        self.processBar.setValue(0)
        self.processBar.setRange(0,140)
        self.processBar.setObjectName("processBar")

        self.layoutWidget = QtWidgets.QWidget(Movie)
        self.layoutWidget.setGeometry(QtCore.QRect(980, 0, 300, 720))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.ShowBt = QtWidgets.QPushButton(self.layoutWidget)
        self.ShowBt.setObjectName("PhotoBt")
        self.ShowBt.setFixedSize(300, 180)
        self.ShowBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.ShowBt)

        self.FileBt = QtWidgets.QPushButton(self.layoutWidget)
        self.FileBt.setObjectName("FileBt")
        self.FileBt.setFixedSize(300, 180)
        self.FileBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.FileBt)

        self.StartBt = QtWidgets.QPushButton(self.layoutWidget)
        self.StartBt.setObjectName("StartBt")
        self.StartBt.setFixedSize(300, 180)
        self.StartBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.StartBt)

        self.ReturnBt = QtWidgets.QPushButton(self.layoutWidget)
        self.ReturnBt.setObjectName("ReturnBt")
        self.ReturnBt.setFixedSize(300, 180)
        self.ReturnBt.setFont(QFont("Microsoft YaHei", 14))
        self.verticalLayout.addWidget(self.ReturnBt)

        self.retranslateUi(Movie)
        QtCore.QMetaObject.connectSlotsByName(Movie)

    def retranslateUi(self, Movie):
        _translate = QtCore.QCoreApplication.translate
        Movie.setWindowTitle(_translate("Movie", "视频检测"))
        self.ShowBt.setText(_translate("Movie", "录制"))
        self.FileBt.setText(_translate("Movie", "上传"))
        self.StartBt.setText(_translate("Movie", "开始"))
        self.ReturnBt.setText(_translate("Movie", "返回"))
        self.rePlayBt.setText(_translate("Movie", "重播"))
        self.rePlayBt.setEnabled(False)
