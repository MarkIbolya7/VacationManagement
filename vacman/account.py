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
        self.c.execute("SELECT user FROM accounts WHERE user = ?", (self.user,))
        row = self.c.fetchone()
        if row is None:
            self.c.execute("INSERT INTO accounts (user, usergroup) VALUES (?,?)", (self.user, "pending"))

        self.closeDB()

    def closeDB(self):
        self.conn.commit()
        self.conn.close()
        return "ok"