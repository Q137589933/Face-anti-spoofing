import datetime
import sys
import time
import cv2
import dlib
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from Editor import editor
from numpy import iterable
from  PyQt5 import QtWidgets, QtCore

from dynamic.pose_liveness_video import load_model, face_direction_detect
from UI.mainUI import Ui_MainWindow
from UI.MovieUI import Ui_Movie
from UI.PhotoUI import Ui_Photo
from UI.DynamicUI import Ui_Dynamic
from UI.SignUpUI import Ui_SignUp
from UI.EditorUI import Ui_Editor, Ui_PreView, Editor_Type
from PyQt5.Qt import QFileDialog
from PyQt5.QtGui import QImage

# 视频检测
from video_detect.main import recognition_liveness

# 主窗口
from dynamic.detector import detector
import dynamic.inter_config as inter_cfg

from database import db

image_path = "Image/"
movie_path = "Movie/"

class parentWindow(QMainWindow, Ui_MainWindow):
    def __del__(self):
        try:
            self.camera.release()  # 释放资源
        except:
            return

    def __init__(self, parent=None):
        super(parentWindow, self).__init__(parent)
        self.setupUi(self)
        self.CallBackFunctions()

    def show(self):
        super(parentWindow, self).show()
        if _user == -1:
            self.userLabel.setText("欢迎使用")
            self.signInBt.setVisible(True)
            self.signUpBt.setVisible(True)
            self.signOutBt.setVisible(False)
        else:
            self.userLabel.setText(f"用户：{_userName}")
            self.signInBt.setVisible(False)
            self.signUpBt.setVisible(False)
            self.signOutBt.setVisible(True)
        self.back()

    # 回调函数
    def CallBackFunctions(self):
        self.About.clicked.connect(self.about)
        self.signInBt.clicked.connect(self.signIn)
        self.signOutBt.clicked.connect(self.signOut)
        self.backBt.clicked.connect(self.back)
        self.loginBt.clicked.connect(self.loginIn)

    # 帮助
    def about(self):
        reply = QMessageBox.information(self,
                                        "关于",
                                        "1.点击【视频检测】按钮上传或录制视频,点击【开始】检测\n"
                                        "2.点击【照片检测】按钮上传或拍摄照片，点击【开始】检测\n"
                                        "3.点击【动态监测】按钮根据指令做出动作，显示检测结果\n"
                                        "4.点击【帮助】按钮可查看帮助",
                                        QMessageBox.Close)

    def signIn(self):
        self.leftFrame.setVisible(False)
        self.passWd.setText("")
        self.frame.setVisible(True)

    def loginIn(self):
        global _user, _userName
        userName = self.uId.text()
        passWd = self.passWd.text()
        if userName != "" and passWd != "":
            sql = f"select * from editor where Ename = '{userName}'"
            if db.prepare(sql) != 0:
                sql = f"select EId from editor where Ename = '{userName}' and password = '{passWd}'"
                if db.prepare(sql) != 0:
                    result = db.selectOne(sql)
                    _user = result[0]
                    _userName = userName
                    self.close()
                    ui_child_editor.show()
                else:
                    QMessageBox.warning(self, "warning", "密码不正确", QMessageBox.Close)
            else:
                sql = f"select * from viewer where Uname = '{userName}'"
                if db.prepare(sql) == 0:
                    QMessageBox.warning(self, "warning", "用户名不存在", QMessageBox.Close)
                else:
                    sql = f"select UId from viewer where Uname = '{userName}' and password = '{passWd}'"
                    if db.prepare(sql) == 0:
                        QMessageBox.warning(self, "warning", "密码不正确", QMessageBox.Close)
                    else:
                        result = db.selectOne(sql)
                        _user = result[0]
                        _userName = userName
                        self.userLabel.setText(f"用户：{userName}")
                        self.back()
                        self.signInBt.setVisible(False)
                        self.signUpBt.setVisible(False)
                        self.signOutBt.setVisible(True)
        else:
            QMessageBox.warning(self, "warning", "用户名/密码不能为空", QMessageBox.Close)

    def back(self):
        self.leftFrame.setVisible(True)
        self.frame.setVisible(False)

    def signOut(self):
        global _user, _userName
        _user = -1
        _userName = ""
        self.signInBt.setVisible(True)
        self.signUpBt.setVisible(True)
        self.signOutBt.setVisible(False)

# 照片窗口
class childWindow_photo(QDialog, Ui_Photo):
    def __init__(self, parent=None):
        super(childWindow_photo, self).__init__(parent)
        self.setupUi(self)
        self.frame = []
        self.frame_name = ""
        self.start_time = ""
        self.fPhoto = False
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.TimerOutFunc)
        self.CallBackFunctions()

    def _initData(self):
        self.frame = []
        self.frame_name = ""
        self.start_time = ""
        self.ShowLb.setPixmap(QPixmap("Icon/tips.png"))
        self.fPhoto = False
        self.StartCamera()

    # 回调函数
    def CallBackFunctions(self):
        self.PhotoBt.clicked.connect(self.PhotoCamera)
        self.StartBt.clicked.connect(self.Start)
        self.FileBt.clicked.connect(self.UploadPhoto)
        self.ReturnBt.clicked.connect(self.Back)

    def Back(self):
        ui.show()
        self.Timer.stop()
        self.camera.release()
        self.close()

    # 初始化摄像头并打开
    def PrepCamera(self):
        self.camera = cv2.VideoCapture(0)

    # 开始按钮函数
    def StartCamera(self):
        self.PrepCamera()
        self.Timer.start(1)  # 每隔1ms刷新一次
        self.timelb = time.perf_counter()
        #这里的数据库还没加

    def TimerOutFunc(self):
        success, img = self.camera.read()
        if self.fPhoto:
            self.frame = img
            self.Timer.stop()
        if success:
            self.openFrame(img)

    # 拍照按钮函数
    def PhotoCamera(self):
        self.start_time = datetime.datetime.now()
        self.frame_name = image_path + self.start_time.strftime("%Y_%m_%d_%H_%M_%S") + '.jpg'
        if self.fPhoto:
            self.Timer.start(1)
        self.fPhoto = not self.fPhoto

    def UploadPhoto(self):
        self.fPhoto = True
        self.Timer.stop()
        pictureName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.jpg;*.png;;All Files(*)")
        if pictureName != "":
            self.frame = cv2.imread(pictureName)
            self.frame_name = pictureName
            self.openFrame(self.frame)

    def openFrame(self, img):
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.ShowLb.width(),
                                                                                               self.ShowLb.height())
        self.ShowLb.setPixmap(QPixmap.fromImage(q_image))

    # 开始检测,图片信息存储在self.frame中
    def Start(self):
        if self.frame_name == "":
            QMessageBox.information(self, "提示", "还未上传/拍摄图片", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            print("开始分析")
            label = 0
            if self.start_time == "":
                self.start_time = datetime.datetime.now()
                self.frame_name = image_path + self.start_time.strftime("%Y_%m_%d_%H_%M_%S") + '.jpg'
            cv2.imwrite(self.frame_name, self.frame)
            create_time = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            print(create_time)
            sql = f"insert into photo(path, upTime, label, user) values ('{self.frame_name}','{create_time}', {label}, {_user})"
            db.prepare(sql)
            db.update()
            print("分析完成")

# 视频窗口
class childWindow_movie(QDialog, Ui_Movie):
    def __init__(self, parent=None):
        super(childWindow_movie, self).__init__(parent)
        self.setupUi(self)
        self.mvName = ""
        self.start_time = ""
        self.frame = []
        self.viewTimer = QTimer()
        self.saveTimer = QTimer()
        self.fCamera = False
        self.viewTimer.timeout.connect(self.viewCam)
        self.saveTimer.timeout.connect(self.saveCam)
        self.CallBackFunctions()

    def _initData(self):
        self.mvName = ""
        self.start_time = ""
        self.frame = []
        self.ShowLb.setPixmap(QPixmap("Icon/tips.png"))
        self.processBar.setValue(0)
        self.rePlayBt.setEnabled(False)
        self.PrepCamera()

    # 初始化摄像头
    def PrepCamera(self):
        try:
            self.cap = cv2.VideoCapture(0)
        except Exception as e:
            print("摄像头调用失败")

    def StartCamera(self):
        self.viewTimer.start(1)  # 每隔1ms刷新一次
        self.timelb = time.perf_counter()

    # 回调函数
    def CallBackFunctions(self):
        self.FileBt.clicked.connect(self.UploadVideo)
        self.ShowBt.clicked.connect(self.RecordVideo)
        self.StartBt.clicked.connect(self.Start)
        self.ReturnBt.clicked.connect(self.Back)
        self.rePlayBt.clicked.connect(self.rePlay)

    # 上传视频
    def UploadVideo(self):
        self.rePlayBt.setEnabled(True)
        self.fCamera = False
        self.cap.release()
        self.viewTimer.stop()
        self.saveTimer.stop()
        self.start_time = datetime.datetime.now()
        mvName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.mp4;*.avi;*mpeg;;All Files(*)")
        if mvName != "":
            self.cap = cv2.VideoCapture(mvName)
            self.mvName = movie_path + self.start_time.strftime("%Y_%m_%d_%H_%M_%S") + '.mp4'
            w = int(self.cap.get(3))
            h = int(self.cap.get(4))
            self.out = cv2.VideoWriter(self.mvName, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 20, (w, h))
            self.viewTimer.start(40)

    # 录制视频
    def RecordVideo(self):
        if not self.fCamera:
            self.viewTimer.stop()
            self.PrepCamera()
        w = int(self.cap.get(3))
        h = int(self.cap.get(4))
        self.start_time = datetime.datetime.now()
        self.mvName = movie_path + self.start_time.strftime("%Y_%m_%d_%H_%M_%S") + '.mp4'
        self.out = cv2.VideoWriter(self.mvName, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 20, (w, h))
        self.fCamera = True
        self.mvTime = 0
        self.StartCamera()
        self.saveTimer.start(5000)

    # 开始分析，视频信息可以通过self.mvName
    def Start(self):
        if self.mvName == "":
            QMessageBox.information(self, "提示", "还未上传/录制视频", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            print(self.mvName)
            print(self.cap)

            print("开始分析")
            label_name = recognition_liveness(self.mvName, './video_detect/liveness.model',
                                                   './video_detect/label_encoder.pickle',
                                                   './video_detect/face_detector', confidence=0.7)
            if label_name == 'fake':
                label = 0
            else:
                label = 1

            create_time = self.start_time.strftime("%Y-%m-%d %H:%M:%S")
            sql = f"insert into video (path, upTime, label, user) values ('{self.mvName}','{create_time}', {label}, {_user})"
            db.prepare(sql)
            db.update()
            print("分析完成")

    def Back(self):
        ui.show()
        self.cap.release()
        self.viewTimer.stop()
        self.saveTimer.stop()
        self.close()

        # 从摄像头读取图像

    def viewCam(self):
        success, frame = self.cap.read()
        self.out.write(frame)
        if success:
            if self.fCamera:
                self.mvTime = self.mvTime + 1
                self.processBar.setValue(self.mvTime)
            self.OpenFrame(frame)
        else:
            self.viewTimer.stop()
            self.cap.release()
            if not self.fCamera:
                self.out.release()

    def saveCam(self):
        self.fCamera = False
        self.saveTimer.stop()
        self.viewTimer.stop()
        self.rePlayBt.setEnabled(True)
        self.cap.release()
        self.out.release()

    def OpenFrame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(self.ShowLb.width(),
                                                                                               self.ShowLb.height())
        self.ShowLb.setPixmap(QPixmap.fromImage(q_image))

    def rePlay(self):
        if self.mvName != "":
            self.cap = cv2.VideoCapture(self.mvName)
            self.viewTimer.start(40)

# 注册窗口
class childWindow_signUp(QDialog, Ui_SignUp):
    def __init__(self, parent=None):
        super(childWindow_signUp, self).__init__(parent)
        self.setupUi(self)
        self.CallBackFunctions()

    def show(self):
        super(childWindow_signUp, self).show()
        self.uid.setText("")
        self.password.setText("")
        self.repassWd.setText("")
        self.email.setText("")
        self.tel.setText("")

    # 回调函数
    def CallBackFunctions(self):
        self.signUpBt.clicked.connect(self.signUp)
        self.backBt.clicked.connect(self.back)

    def back(self):
        self.close()

    def signUp(self):
        userName = self.uid.text()
        passWord = self.password.text()
        if passWord != self.repassWd.text():
            QMessageBox.warning(self, "warning", "两次密码输入不一致", QMessageBox.Close)
            return
        email = self.email.text()
        tel = self.email.text()
        sql = f"select * from viewer where Uname = '{userName}'"
        if db.prepare(sql) != 0:
            QMessageBox.warning(self, "warning", "账号已存在", QMessageBox.Close)
            return
        sql = f"insert into viewer (Uname, password, phone, email) values ('{userName}', '{passWord}', '{email}', '{tel}')"
        db.prepare(sql)
        db.update()
        QMessageBox.information(self, "tips", "注册成功！", QMessageBox.Close)
        self.close()

# 动态检测窗口
class childWindow_dynamic(QDialog, Ui_Dynamic):
    """
        EYE_BLINK = 0
        OPEN_MOUSE = 1
        RIGHT_HEAD = 2
        LEFT_HEAD = 3
    """

    def __init__(self, parent=None):
        super(childWindow_dynamic, self).__init__(parent)
        self.setupUi(self)
        self.frame = []
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.TimerOutFunc)
        self.CallBackFunctions()

    def stats_init(self):  # 初始化需要用到的统计参数
        self.blink_frame = 0  # 记录一次眨眼所花帧数
        self.blink_times = 0  # 记录眨眼次数
        self.open_frame = 0  # 记录张嘴帧数
        self.open_times = 0  # 记录张嘴几次
        self.keep_status = 0  # 当前状态持续帧数

    def _initData(self):
        self.frame = []  # 用于存储测试帧
        self.StartCamera()  # 启动摄像头
        self.action_list = range(4)  # 测试动作列表
        self.ACTION_NUM = 4  # 动作数量
        self.keep_status = 0  # 当前状态持续了多久
        self.status = -2  # 当前状态 记录当前正在做哪个动作 -2表示没有开始检测 -1表示检测不到正面 0123对应action序号
        self.model_init()  # 初始化模型
        print(1)
        self.stats_init()  # 初始化统计参数

    def model_init(self):
        self.face_pos_detector = dlib.get_frontal_face_detector()
        self.detector = detector(detector=dlib.shape_predictor(inter_cfg.landmarks),
                                 face_pos_detector=self.face_pos_detector)
        self.face_dir_model = load_model(inter_cfg.path_hopenet, device=inter_cfg.device)

    # 回调函数
    def CallBackFunctions(self):
        self.StartBt.clicked.connect(self.Start)
        self.ReturnBt.clicked.connect(self.Back)

    def Back(self):
        self.camera.release()
        self.close()
        self.Timer.stop()
        ui.show()

    # 开始检测
    def Start(self):
        self.MsgLb.setText("请正视屏幕")
        self.chosen_action = [0, 1, 2, 3]  # 选择动作
        # self.chosen_action = random.sample(range(len(self.action_list)), self.ACTION_NUM)  # 随机挑选动作
        self.status = -1  # 更新status为未检测到正面
        self.cur_act = 0  # 当前进行第几个动作

    # 初始化摄像头并打开
    def PrepCamera(self):
        self.camera = cv2.VideoCapture(0)

    # 启动相机
    def StartCamera(self):
        self.PrepCamera()
        self.Timer.start(30)  # 每隔30ms刷新一次
        self.timelb = time.perf_counter()

    def TimerOutFunc(self):  # 定时器事件，每计数一次触发一次该函数
        success, img = self.camera.read()
        self.frame = img
        if success:
            self.openFrame()  # 检测、显示帧

    def openFrame(self):
        if self.frame != []:
            # 尚未开始检测
            if self.status == -2:
                # 直接显示摄像头读取的信息
                show = cv2.resize(self.frame, (self.ShowLb.width(), self.ShowLb.height()))
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
                showImage = QImage(show.data, show.shape[1], show.shape[0],
                                   QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
                self.ShowLb.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
            # 正在检测
            else:
                if self.keep_status > inter_cfg.FRAME_LIMIT:
                    self.detect_finish(0)  # 超过限定时间没有通过验证
                    self.status = -2
                    return
                # 修改帧尺寸为showLB尺寸
                show = cv2.resize(self.frame, (self.ShowLb.width(), self.ShowLb.height()))
                face_result = self.detect_face(show)
                if iterable(face_result):  # 检测到人脸
                    x1, y1, x2, y2, rect = face_result
                    show = cv2.rectangle(show, (x1, y1), (x2, y2), (0, 255, 0), 2)
                else:

                    if self.status == -1:
                        self.keep_status += 1
                    if self.status != 2 and self.status != 3:  # 转头动作会导致检测不到人脸
                        self.MsgLb.setText('请正对屏幕')
                        self.status = -1
                # cv2.rectangle(show, (60, 60), (260, 260), (0, 255, 0), 2)
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
                showImage = QImage(show.data, show.shape[1], show.shape[0],
                                   QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
                self.ShowLb.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
                if not iterable(face_result): return  # 没检测到人脸显示玩人像直接返回

                real_flag = False
                self.make_instruction()  # 对用户做出动作指示
                if self.action_list[self.chosen_action[self.cur_act]] == 0:
                    self.blink_frame, self.blink_times = self.detect_blink(show, rect, self.blink_frame,
                                                                           self.blink_times)
                    if self.blink_times > inter_cfg.EYE_AR_TOTAL_THRESH:
                        real_flag = True
                    if self.status == 0: self.keep_status += 1
                    self.status = 0
                elif self.action_list[self.chosen_action[self.cur_act]] == 1:
                    self.open_frame, self.open_times = self.detect_open_mouse(show, rect, self.open_frame,
                                                                              self.open_times)
                    if self.open_times >= inter_cfg.MOUTH_OPEN_TOTAL_THRESH:
                        real_flag = True
                    if self.status == 1: self.keep_status += 1
                    self.status = 1
                elif self.action_list[self.chosen_action[self.cur_act]] == 2:
                    if self.detect_turn_head(show, rect, right=0):
                        real_flag = True
                    if self.status == 2: self.keep_status += 1
                    self.status = 2
                elif self.action_list[self.chosen_action[self.cur_act]] == 3:
                    if self.detect_turn_head(show, rect, right=1):
                        real_flag = True
                    if self.status == 3: self.keep_status += 1
                    self.status = 3
                if real_flag:  # 通过检测
                    self.cur_act += 1
                    if self.cur_act >= len(self.chosen_action):
                        self.detect_finish()
                        self.status = -2
                    else:
                        self.stats_init()  # 重置统计量

    def make_instruction(self):
        if self.action_list[self.chosen_action[self.cur_act]] == 0:
            self.MsgLb.setText('请眨眼')
        elif self.action_list[self.chosen_action[self.cur_act]] == 1:
            self.MsgLb.setText('请张嘴')
        elif self.action_list[self.chosen_action[self.cur_act]] == 2:
            self.MsgLb.setText('请向左转头')
        elif self.action_list[self.chosen_action[self.cur_act]] == 3:
            self.MsgLb.setText('请向右转头')

    def detect_finish(self, success=1):  # 检测完成
        if success:
            self.MsgLb.setText('验证成功！')
        else:
            self.MsgLb.setText('验证失败')
        self.ShowLb.clear()
        self.camera.release()
        self.Timer.stop()

    def detect_face(self, img):  # 检测人脸位置
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = self.face_pos_detector(gray, 0)  # 框出人脸
        if len(rects) != 1: return len(rects)
        for rect in rects:
            y1 = rect.top() if rect.top() > 0 else 0
            y2 = rect.bottom() if rect.bottom() > 0 else 0
            x1 = rect.left() if rect.left() > 0 else 0
            x2 = rect.right() if rect.right() > 0 else 0
            return x1, y1, x2, y2, rect

    def detect_blink(self, img, rect, blink_frame, blink_times):  # 检测眨眼
        blink_frame, blink_times = self.detector.eye_blink(img, rect, blink_frame, blink_times)
        return blink_frame, blink_times

    def detect_open_mouse(self, img, rect, open_frame, open_times):  # 检测张嘴
        open_frame, open_times = self.detector.mouth_open(img, rect, open_frame, open_times)
        return open_frame, open_times

    def detect_turn_head(self, img, rect, right=0):  # right=0：左转头  #检测转头
        y1 = rect.top() if rect.top() > 0 else 0
        y2 = rect.bottom() if rect.bottom() > 0 else 0
        x1 = rect.left() if rect.left() > 0 else 0
        x2 = rect.right() if rect.right() > 0 else 0
        head = img[x1:x2, y1:y2, :]
        return face_direction_detect(head, self.face_dir_model, right, device=inter_cfg.device)

# 管理员窗口
class childWindow_editor(QDialog, Ui_Editor):
    def __init__(self, parent=None):
        super(childWindow_editor, self).__init__(parent)
        self.viewTimer = QTimer()
        self.viewTimer.timeout.connect(self.previewVideo)
        self.setupUi(self)
        self.CallBackFunctions()

    def previewVideo(self):
        success, frame = self.cap.read()
        if success:
            self.OpenFrame(frame)
        else:
            self.viewTimer.stop()
            self.cap.release()

    def show(self):
        super(childWindow_editor, self).show()
        self.showChildFrame(Editor_Type.User)
        if _user == -1:
            self.infoLabel.setText("欢迎使用")
        else:
            self.infoLabel.setText(f"管理员:{_userName}")
            self.ReFreshUserData()

    # 回调函数
    def CallBackFunctions(self):
        self.signOutBtn.clicked.connect(self.Back)
        self.photoSearchBtn.clicked.connect(self.searchPhotoData)
        self.videoSearchBtn.clicked.connect(self.searchVideoData)
        self.delUserBtn.clicked.connect(lambda :self.delUserData())
        self.delPhotoBtn.clicked.connect(lambda : self.delPhotoData())
        self.delVideoBtn.clicked.connect(lambda : self.delVideoData())
        self.userBtn.clicked.connect(lambda : self.showChildFrame(Editor_Type.User))
        self.photoBtn.clicked.connect(lambda : self.showChildFrame(Editor_Type.PHOTO))
        self.videoBtn.clicked.connect(lambda : self.showChildFrame(Editor_Type.MOVIE))

    def Back(self):
        global _user, _userName
        _user = -1
        _userName = ""
        ui.show()
        self.close()

    # 搜索
    def searchPhotoData(self):
        uid = self.photoLineEdit.text()
        if uid != "":
            self.ReFreshPhotoData(uid)

    # 查询视频数据
    def searchVideoData(self):
        uid = self.videoLineEdit.text()
        if uid != "":
            self.ReFreshVideoData(uid)

    # 更新用户数据
    def ReFreshUserData(self):
        data = editor.getUserData()
        self.userTableWidget.clearContents()
        self.userTableWidget.setRowCount(len(data))
        row = 0
        bindEvent = lambda button, row: button.clicked.connect(lambda: self.delUserData(data[row][0]))
        for tup in data:
            col = 0
            for item in tup:
                oneitem = QtWidgets.QTableWidgetItem(str(item))
                oneitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.userTableWidget.setItem(row, col, oneitem)
                col += 1
            btnDelete = QtWidgets.QPushButton()
            btnDelete.setText("删除")
            bindEvent(btnDelete, row)
            self.userTableWidget.setCellWidget(row, col, btnDelete)
            row += 1

    # 删除用户数据
    def delUserData(self, *args):
        editor.delUserData(*args)
        self.ReFreshUserData()

    # 删除相机数据
    def delPhotoData(self, *args):
        editor.delPhotoItem(*args)
        self.ReFreshPhotoData()

    # 删除视频数据
    def delVideoData(self, *args):
        editor.delMovieItem(*args)
        self.ReFreshVideoData()

    # 更新图片数据
    def ReFreshPhotoData(self, *args):
        data = editor.getPhotoData(*args)
        self.photoTableWidget.clearContents()
        self.photoTableWidget.setRowCount(len(data))
        bindDelEvent = lambda button, row: button.clicked.connect(lambda: self.delPhotoData(data[row][0]))
        bindShowEvent = lambda button, row: button.clicked.connect(lambda: self.showPhotoData(data[row][1]))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                if col == 2:
                    item = item.strftime("%Y-%m-%d %H:%M:%S")
                oneitem = QtWidgets.QTableWidgetItem(str(item))
                oneitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.photoTableWidget.setItem(row, col, oneitem)
                col += 1
            btnDelete = QtWidgets.QPushButton()
            btnDelete.setText("删除")
            bindDelEvent(btnDelete, row)
            self.photoTableWidget.setCellWidget(row, col, btnDelete)

            btnShow = QtWidgets.QPushButton()
            btnShow.setText("预览")
            bindShowEvent(btnShow, row)
            self.photoTableWidget.setCellWidget(row, col + 1, btnShow)
            row += 1

    # 预览照片
    def showPhotoData(self, path):
        ui_child_preview.show()
        frame = cv2.imread(path)
        self.OpenFrame(frame)

    # 预览视频
    def showVideoData(self, path):
        ui_child_preview.show()
        self.cap = cv2.VideoCapture(path)
        self.viewTimer.start(40)

    # 更新视频数据
    def ReFreshVideoData(self, *args):
        data = editor.getVideoData(*args)
        self.videoTableWidget.clearContents()
        self.videoTableWidget.setRowCount(len(data))
        bindDelEvent = lambda button, row: button.clicked.connect(lambda: self.delVideoData(data[row][0]))
        bindShowEvent = lambda button, row: button.clicked.connect(lambda: self.showVideoData(data[row][1]))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                if col == 2:
                    item = item.strftime("%Y-%m-%d %H:%M:%S")
                oneitem = QtWidgets.QTableWidgetItem(str(item))
                oneitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.videoTableWidget.setItem(row, col, oneitem)
                col += 1
            btnDelete = QtWidgets.QPushButton()
            btnDelete.setText("删除")
            bindDelEvent(btnDelete, row)
            self.videoTableWidget.setCellWidget(row, col, btnDelete)

            btnShow = QtWidgets.QPushButton()
            btnShow.setText("预览")
            bindShowEvent(btnShow, row)
            self.videoTableWidget.setCellWidget(row, col + 1, btnShow)
            row += 1

    def OpenFrame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(ui_child_preview.label.width(),
                                                                                               ui_child_preview.label.height())
        ui_child_preview.label.setPixmap(QPixmap.fromImage(q_image))

    def showChildFrame(self, editType):
        for item in self.rightFrames.values():
            item.setVisible(False)
        if editType == Editor_Type.User:
            self.ReFreshUserData()
        elif editType == Editor_Type.PHOTO:
            self.ReFreshPhotoData()
        else:
            self.ReFreshVideoData()
        self.rightFrames[editType].setVisible(True)


# 预览窗口
class childWindow_preview(QDialog, Ui_PreView):
    def __init__(self, parent=None):
        super(childWindow_preview, self).__init__(parent)
        self.setupUi(self)

def open_childWindow(child_window):
    if _user != -1:
        child_window.show()
        child_window._initData()
        ui.close()
    else:
        QMessageBox.warning(ui, "warning", "请先登录!", QMessageBox.Close)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    global _user, _userName
    _user = -1
    _userName = ""

    ui = parentWindow()
    ui_child_movie = childWindow_movie()
    ui_child_photo = childWindow_photo()
    ui_child_dynamic = childWindow_dynamic()
    ui_child_signUp = childWindow_signUp()
    ui_child_preview = childWindow_preview()
    ui_child_editor = childWindow_editor()
    ui_child_editor.preview = ui_child_preview

    movie_btn = ui.Moviebt
    photo_btn = ui.Photobt
    dynamic_btn = ui.Dynamicbt
    signUp_btn = ui.signUpBt

    movie_btn.clicked.connect(lambda: open_childWindow(ui_child_movie))
    photo_btn.clicked.connect(lambda: open_childWindow(ui_child_photo))
    dynamic_btn.clicked.connect(lambda: open_childWindow(ui_child_dynamic))

    signUp_btn.clicked.connect(ui_child_signUp.show)

    ui.show()
    sys.exit(app.exec_())
