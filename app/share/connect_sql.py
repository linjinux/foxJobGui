import sqlite3
import os
class Sqlconn(object):
    def __init__(self):
        pass
    def insertdb(self,sql):
        conn = sqlite3.connect(dbdir)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    def deletedb(self,sql):
        conn = sqlite3.connect(dbdir)
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    def updatedb(self,sql):
        conn = sqlite3.connect(dbdir)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    def selectdb(self,sql,dbdir):
        conn = sqlite3.connect(dbdir)
        cur = conn.cursor()
        date=cur.execute(sql)
        #conn.close()
        return date