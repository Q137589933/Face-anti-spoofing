from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(800, 600)

        self.frame = QtWidgets.QFrame(SignUp)
        self.frame.setGeometry(QtCore.QRect(150, 50, 500, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frame1 = QtWidgets.QFrame(SignUp)
        self.frame1.setGeometry(QtCore.QRect(150, 50, 200, 400))
        #self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setObjectName("frame1")

        self.frame2 = QtWidgets.QFrame(SignUp)
        self.frame2.setGeometry(QtCore.QRect(350, 50, 300, 400))
        #self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setObjectName("frame2")

        self.frame3 = QtWidgets.QFrame(SignUp)
        self.frame3.setGeometry(QtCore.QRect(200, 450, 400, 50))
        #self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setObjectName("frame3")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout1.setContentsMargins(0,0,0,0)
        self.verticalLayout1.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label1 = QtWidgets.QLabel(self.frame1)
        self.label1.setFont(font)
        self.label1.setText("账号：")
        self.label1.setFixedHeight(40)
        self.verticalLayout.addWidget(self.label1, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.label2 = QtWidgets.QLabel(self.frame1)
        self.label2.setFont(font)
        self.label2.setText("密码：")
        self.label2.setFixedHeight(40)
        self.verticalLayout.addWidget(self.label2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setFont(font)
        self.label3.setText("确认密码：")
        self.label3.setFixedHeight(40)
        self.verticalLayout.addWidget(self.label3, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.label4 = QtWidgets.QLabel(self.frame1)
        self.label4.setFont(font)
        self.label4.setText("邮箱：")
        self.label4.setFixedHeight(40)
        self.verticalLayout.addWidget(self.label4, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.label5 = QtWidgets.QLabel(self.frame1)
        self.label5.setFont(font)
        self.label5.setText("手机号：")
        self.label5.setFixedHeight(40)
        self.verticalLayout.addWidget(self.label5, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.uid = QtWidgets.QLineEdit(self.frame2)
        self.uid.setFont(font)
        self.uid.setObjectName("uid")
        self.uid.setFixedSize(200, 40)
        self.verticalLayout1.addWidget(self.uid, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.password = QtWidgets.QLineEdit(self.frame2)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.setFixedSize(200, 40)
        self.verticalLayout1.addWidget(self.password, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.repassWd = QtWidgets.QLineEdit(self.frame2)
        self.repassWd.setFont(font)
        self.repassWd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassWd.setObjectName("repassWd")
        self.repassWd.setFixedSize(200, 40)
        self.verticalLayout1.addWidget(self.repassWd, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.email = QtWidgets.QLineEdit(self.frame2)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.email.setFixedSize(200, 40)
        self.verticalLayout1.addWidget(self.email, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.tel = QtWidgets.QLineEdit(self.frame2)
        self.tel.setFont(font)
        self.tel.setObjectName("tel")
        self.tel.setFixedSize(200, 40)
        self.verticalLayout1.addWidget(self.tel, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.signUpBt = QtWidgets.QPushButton(self.frame3)
        self.signUpBt.setFont(QFont("Microsoft YaHei", 14))
        self.signUpBt.setFixedSize(100, 40)
        self.signUpBt.setObjectName("signupBt")
        self.horizontalLayout.addWidget(self.signUpBt)

        self.backBt = QtWidgets.QPushButton(self.frame3)
        self.backBt.setFont(QFont("Microsoft YaHei", 14))
        self.backBt.setObjectName("backBt")
        self.backBt.setFixedSize(100, 40)
        self.horizontalLayout.addWidget(self.backBt)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "注册"))
        self.backBt.setText(_translate("SignUp", "返回"))
        self.signUpBt.setText(_translate("SignUp", "注册"))
