from database import db
import os

class Editor():
    def __init__(self):
        super(Editor, self).__init__()

    def delPhotoItem(self, *args):
        sql = ""
        if len(args) == 0:
            sql = f"select path from photo"
            results = db.selectAll(sql)
            for item in results:
                os.remove(item[0])
            sql = "delete from photo"
        elif len(args) == 1:
            sql = f"select path from photo where PId = {args[0]}"
            result = db.selectOne(sql)
            os.remove(result[0])
            sql = f"delete from photo where PId={args[0]}"
        if sql != "":
            db.prepare(sql)
            db.update()

    def delMovieItem(self, *args):
        sql = ""
        if len(args) == 0:
            sql = f"select path from video"
            results = db.selectAll(sql)
            for item in results:
                os.remove(item[0])
            sql = "delete from table video"
        elif len(args) == 1:
            sql = f"select path from video where VId = {args[0]}"
            result = db.selectOne(sql)
            os.remove(result[0])
            sql = f"delete from video where VId={args[0]}"
        if sql != "":
            db.prepare(sql)
            db.update()

    def delUserData(self, *args):
        sql = ""
        if len(args) == 0:
            sql = "delete from viewer"
        elif len(args) == 1:
            sql = f"delete from viewer where UId={args[0]}"
        db.prepare(sql)
        db.update()

    def getUserData(self):
        sql = "select UId, Uname, phone, email from viewer"
        results = db.selectAll(sql)
        return results

    def getPhotoData(self, *args):
        sql = ""
        if len(args) == 0:
            sql = "select * from photo"
        elif len(args) == 1:
            sql = f"select * from photo where user = {args[0]}"
        if sql != "":
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

editor = Editor()