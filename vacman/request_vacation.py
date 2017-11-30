import time
import sqlite3

import os


class VacMan():
    def __init__(self, user, date):

        self.user=user
        self.date = date

        dbfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../vacations.sqlite"
        self.conn = sqlite3.connect(dbfile_path)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS vacations (user STRING, data STRING, status STRING)")

    def request(self):
        self.c.execute("INSERT INTO vacations (user,data,status) VALUES (?,?,?)", (self.user, self.date, "pending"))
        self.closeDB()

    def approve(self):
        self.c.execute("UPDATE vacations SET status = 'approved' WHERE user=? AND date=?", (self.user, self.date))
        self.closeDB()

    def closeDB(self):
        self.conn.commit()
        self.conn.close()
        return "ok"
