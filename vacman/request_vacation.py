import sqlite3

import os


class VacMan():
    def __init__(self, user, date):

        self.user=user
        self.date = date

        dbfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../vacations.sqlite"
        self.conn = sqlite3.connect(dbfile_path)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS vacations (user STRING, date STRING, status STRING)")

    def request(self):
        self.c.execute("INSERT INTO vacations (user,date,status) VALUES (?,?,?)", (self.user, self.date, "pending"))
        self.closeDB()

    def closeDB(self):
        self.conn.commit()
        self.conn.close()
        return "ok"
