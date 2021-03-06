from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from Editor import editor
from PyQt5.QtGui import QImage, QPixmap
import cv2

class Editor_Type():
    User = 0
    PHOTO = 1
    MOVIE = 2

class Ui_PreView(object):
    def setupUi(self, Preview):
        Preview.setObjectName("Preview")
        Preview.resize(640, 480)

        self.label = QtWidgets.QLabel(Preview)
        self.label.setGeometry(QtCore.QRect(0,0,640,480))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)
    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Preview", "预览"))

class Ui_Editor(object):
    def setupUi(self, Editor):
        self.data = []
        Editor.setObjectName("Editor")
        Editor.resize(1280, 720)

        self.leftFrame = QtWidgets.QFrame(Editor)
        self.leftFrame.setGeometry(QtCore.QRect(0,0,250, 720))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.leftFrame.setPalette(QtGui.QPalette(QtGui.QColor(220, 220, 220)))

        self.rightFrames = {}

        self.rightFrame = QtWidgets.QFrame(Editor)
        self.rightFrame.setGeometry(QtCore.QRect(250, 0, 1030, 720))
        self.rightFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.rightFrame.setObjectName("rightFrame")

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout1.setContentsMargins(0,0,0,0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.infoLabel = QtWidgets.QLabel(self.leftFrame)
        self.infoLabel.setFixedSize(250,150)
        self.infoLabel.setFont(QFont("Microsoft YaHei", 16))
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout1.addWidget(self.infoLabel, QtCore.Qt.AlignmentFlag.AlignTop)

        self.userBtn = QtWidgets.QPushButton(self.leftFrame)
        self.userBtn.setFixedHeight(40)
        self.userBtn.setFont(QFont("Microsoft YaHei", 14))
        self.userBtn.setObjectName("userBtn")
        self.verticalLayout1.addWidget(self.userBtn, QtCore.Qt.AlignmentFlag.AlignTop)

        self.photoBtn = QtWidgets.QPushButton(self.leftFrame)
        self.photoBtn.setFixedHeight(40)
        self.photoBtn.setFont(QFont("Microsoft YaHei", 14))
        self.photoBtn.setObjectName("photoBtn")
        self.verticalLayout1.addWidget(self.photoBtn, QtCore.Qt.AlignmentFlag.AlignTop)

        self.videoBtn = QtWidgets.QPushButton(self.leftFrame)
        self.videoBtn.setFixedHeight(40)
        self.videoBtn.setFont(QFont("Microsoft YaHei", 14))
        self.videoBtn.setObjectName("videoBtn")
        self.verticalLayout1.addWidget(self.videoBtn, QtCore.Qt.AlignmentFlag.AlignTop)

        self.signOutBtn = QtWidgets.QPushButton(self.leftFrame)
        self.signOutBtn.setFixedHeight(40)
        self.signOutBtn.setFont(QFont("Microsoft YaHei", 14))
        self.signOutBtn.setObjectName("signOutBtn")
        self.verticalLayout1.addWidget(self.signOutBtn, QtCore.Qt.AlignmentFlag.AlignBottom)

        self.setUpUserFrame()
        self.setUpPhotoFrame()
        self.setUpVideoFrame()

        self.rightFrames[Editor_Type.User] = self.userFrame
        self.rightFrames[Editor_Type.PHOTO] = self.photoFrame
        self.rightFrames[Editor_Type.MOVIE] = self.videoFrame

        self.showChildFrame(Editor_Type.User)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    # 用户管理界面
    def setUpUserFrame(self):
        self.userFrame = QtWidgets.QFrame(self.rightFrame)
        self.userFrame.setObjectName("userFrame")

        self.userTableWidget = QtWidgets.QTableWidget(self.userFrame)
        self.userTableWidget.setGeometry(QtCore.QRect(20, 60, 980, 540))
        self.userTableWidget.setColumnCount(5)
        self.userTableWidget.setRowCount(1)
        self.userTableWidget.setHorizontalHeaderLabels(['Uid', '账号', '手机', '邮箱'])
        self.userTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.delUserBtn = QtWidgets.QPushButton(self.userFrame)
        self.delUserBtn.setGeometry(QtCore.QRect(850, 620, 150, 40))
        self.delUserBtn.setObjectName("delUserBtn")
        self.delUserBtn.setFont(QFont("Microsoft YaHei", 14))
        self.delUserBtn.setText("删除全部")

    # 相机管理界面
    def setUpPhotoFrame(self):
        #self.data = editor.getPhotoData()
        self.photoFrame = QtWidgets.QFrame(self.rightFrame)
        self.photoFrame.setObjectName("photoFrame")

        self.photoSearchFrame = QtWidgets.QFrame(self.photoFrame)
        self.photoSearchFrame.setGeometry(QtCore.QRect(20, 30, 500, 60))
        self.photoSearchFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.photoSearchFrame.setObjectName("photoSearchFrame")

        horizontalLayout = QtWidgets.QHBoxLayout(self.photoSearchFrame)
        horizontalLayout.setContentsMargins(10,0,10,0)

        label = QtWidgets.QLabel(self.photoSearchFrame)
        label.setFont(QFont("Microsoft YaHei", 14))
        label.setText("按用户ID查询:")
        label.setFixedSize(160, 40)
        horizontalLayout.addWidget(label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.photoLineEdit = QtWidgets.QLineEdit(self.photoSearchFrame)
        self.photoLineEdit.setFont(QFont("Microsoft YaHei", 14))
        self.photoLineEdit.setFixedSize(200, 40)
        self.photoLineEdit.setObjectName("photoLineEdit")
        horizontalLayout.addWidget(self.photoLineEdit, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.photoSearchBtn = QtWidgets.QPushButton(self.photoSearchFrame)
        self.photoSearchBtn.setObjectName("photoSearchBtn")
        self.photoSearchBtn.setFont(QFont("Microsoft YaHei", 14))
        self.photoSearchBtn.setFixedSize(80, 40)
        self.photoSearchBtn.setText("查询")
        horizontalLayout.addWidget(self.photoSearchBtn, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.photoTableWidget = QtWidgets.QTableWidget(self.photoFrame)
        self.photoTableWidget.setGeometry(QtCore.QRect(20, 110, 980, 540))
        self.photoTableWidget.setColumnCount(7)
        self.photoTableWidget.setRowCount(1)
        self.photoTableWidget.setHorizontalHeaderLabels(['ID', '路径', '上传时间', '标签', '使用者'])
        self.photoTableWidget.horizontalHeader().resizeSection(0, 50)
        self.photoTableWidget.horizontalHeader().resizeSection(1, 300)
        self.photoTableWidget.horizontalHeader().resizeSection(2, 200)
        self.photoTableWidget.horizontalHeader().resizeSection(3, 50)
        self.photoTableWidget.horizontalHeader().resizeSection(4, 80)
        self.photoTableWidget.setObjectName("photoTableWidget")
        self.photoTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.delPhotoBtn = QtWidgets.QPushButton(self.photoFrame)
        self.delPhotoBtn.setGeometry(QtCore.QRect(850, 670, 150, 40))
        self.delPhotoBtn.setObjectName("delPhotoBtn")
        self.delPhotoBtn.setFont(QFont("Microsoft YaHei", 14))
        self.delPhotoBtn.setText("删除全部")

    # 视频管理界面
    def setUpVideoFrame(self):
        #self.data = editor.getVideoData()
        self.videoFrame = QtWidgets.QFrame(self.rightFrame)
        self.videoFrame.setObjectName("videoFrame")

        self.videoSearchFrame = QtWidgets.QFrame(self.videoFrame)
        self.videoSearchFrame.setGeometry(QtCore.QRect(20, 30, 500, 60))
        self.videoSearchFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.videoSearchFrame.setObjectName("videoSearchFrame")

        horizontalLayout = QtWidgets.QHBoxLayout(self.videoSearchFrame)
        horizontalLayout.setContentsMargins(10, 0, 10, 0)

        label = QtWidgets.QLabel(self.videoSearchFrame)
        label.setFont(QFont("Microsoft YaHei", 14))
        label.setText("按用户ID查询:")
        label.setFixedSize(160, 40)
        horizontalLayout.addWidget(label, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.videoLineEdit = QtWidgets.QLineEdit(self.photoSearchFrame)
        self.videoLineEdit.setFont(QFont("Microsoft YaHei", 14))
        self.videoLineEdit.setFixedSize(200, 40)
        self.videoLineEdit.setObjectName("videoLineEdit")
        horizontalLayout.addWidget(self.videoLineEdit, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.videoSearchBtn = QtWidgets.QPushButton(self.photoSearchFrame)
        self.videoSearchBtn.setObjectName("videoSearchBtn")
        self.videoSearchBtn.setFont(QFont("Microsoft YaHei", 14))
        self.videoSearchBtn.setFixedSize(80, 40)
        self.videoSearchBtn.setText("查询")

        horizontalLayout.addWidget(self.videoSearchBtn, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.videoTableWidget = QtWidgets.QTableWidget(self.videoFrame)
        self.videoTableWidget.setGeometry(QtCore.QRect(20, 110, 980, 540))
        self.videoTableWidget.setColumnCount(7)
        self.videoTableWidget.setRowCount(1)
        self.videoTableWidget.setHorizontalHeaderLabels(['ID', '路径', '上传时间', '标签', '使用者'])
        self.videoTableWidget.horizontalHeader().resizeSection(0, 50)
        self.videoTableWidget.horizontalHeader().resizeSection(1, 300)
        self.videoTableWidget.horizontalHeader().resizeSection(2, 200)
        self.videoTableWidget.horizontalHeader().resizeSection(3, 50)
        self.videoTableWidget.horizontalHeader().resizeSection(4, 80)
        self.videoTableWidget.setObjectName("videoTableWidget")
        self.videoTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.delVideoBtn = QtWidgets.QPushButton(self.videoFrame)
        self.delVideoBtn.setGeometry(QtCore.QRect(850, 670, 150, 40))
        self.delVideoBtn.setObjectName("delVideoBtn")
        self.delVideoBtn.setFont(QFont("Microsoft YaHei", 14))
        self.delVideoBtn.setText("删除全部")

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "管理员"))
        self.userBtn.setText(_translate("Editor", "用户(User)"))
        self.photoBtn.setText(_translate("Editor", "图片(Photo)"))
        self.videoBtn.setText(_translate("Editor", "视频(Video)"))
        self.signOutBtn.setText(_translate("Editor", "注销"))
