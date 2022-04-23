import pymysql

class Database(object):
    def __init__(self):
        #self.db = pymysql.connect(host="localhost", user="root", passwd="daq233622", database="huoti", charset="utf8")
        self.db = pymysql.connect(host="localhost", user="root", passwd="Poison0809.", database="huoti", charset="utf8")
        self.cursor = self.db.cursor()
    def prepare(self, sql):
        return self.cursor.execute(sql)
    def selectOne(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except:
            print("Error: unable to fetch data")
    def selectAll(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")

    def update(self):
        self.db.commit()
    def close(self):
        self.db.close()

db = Database()