import time
import sqlite3

import os


class Account():
    def __init__(self, user):
        self.user = user

        dbfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../users.sqlite"
        self.conn = sqlite3.connect(dbfile_path)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS accounts (user STRING, usergroup STRING)")

    def isnewuser(self):


        #make the first user admin

        self.c.execute("SELECT user FROM accounts")
        row = self.c.fetchone()
        if row is None:
            self.c.execute("INSERT INTO accounts (user, usergroup) VALUES (?,?)", (self.user, "admin"))
        else:
            self.c.execute("SELECT user FROM accounts WHERE user = ?", (self.user,))
            row = self.c.fetchone()
            if row is None:
                self.c.execute("INSERT INTO accounts (user, usergroup) VALUES (?,?)", (self.user, "viewer"))

        self.closeDB()

    def getuserstatus(self):
        self.c.execute("SELECT usergroup FROM accounts WHERE user=?", (self.user,))
        usergroup = self.c.fetchone()
        return usergroup[0]

    def getuservacations(self):
        dbfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../vacations.sqlite"
        self.conn = sqlite3.connect(dbfile_path)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS vacations (user STRING, date STRING, status STRING)")
        self.c.execute("SELECT date, status FROM vacations WHERE user=?", (self.user,))
        vacations = self.c.fetchall()
        self.conn.commit()
        self.conn.close()
        return vacations

    def closeDB(self):
        self.conn.commit()
        self.conn.close()
        return "ok"
