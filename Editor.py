from database import db
from PyQt5.QtGui import QImage, QPixmap
import cv2

class Editor():
    def __init__(self):
        super(Editor, self).__init__()

    def delPhotoItem(self, *args):
        if len(args) == 0:
            sql = "delete from photo"
            db.prepare(sql)
            db.update()
        elif len(args) == 1:
            sql = f"delete from photo where PId={args[0]}"
            db.prepare(sql)
            db.update()

    def delMovieItem(self, *args):
        if len(args) == 0:
            sql = "delete from table video"
            db.prepare(sql)
            db.update()
        elif len(args) == 1:
            sql = f"delete from video where VId={args[0]}"
            db.prepare(sql)
            db.update()

    def delUserData(self, *args):
        if len(args) == 0:
            sql = "delete from viewer"
            db.prepare(sql)
            db.update()
        elif len(args) == 1:
            sql = f"delete from viewer where UId={args[0]}"
            db.prepare(sql)
            db.update()

    def getUserData(self):
        sql = "select UId, Uname, phone, email from viewer"
        results = db.selectAll(sql)
        return results

    def getPhotoData(self, *args):
        if len(args) == 0:
            sql = "select * from photo"
            results = db.selectAll(sql)
            return results
        elif len(args) == 1:
            sql = f"select * from photo where user = {args[0]}"
            results = db.selectAll(sql)
            return results

    def getVideoData(self, *args):
        if len(args) == 0:
            sql = "select * from video"
            results = db.selectAll(sql)
            return results
        elif len(args) == 1:
            sql = f"select * from video where user = {args[0]}"
            results = db.selectAll(sql)
            return results

    def showPhotoData(self, path, ui):
        ui.show()
        frame = cv2.imread(path)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        q_image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).scaled(ui.label.width(),ui.label.height())
        ui.label.setPixmap(QPixmap.fromImage(q_image))

editor = Editor()