import time
import sqlite3

import os


class Admin():

    def __init__(self):

        self.users_path = os.path.dirname(os.path.realpath(__file__)) + "/../users.sqlite"
        self.requests_path = os.path.dirname(os.path.realpath(__file__)) + "/../vacations.sqlite"
        pass

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def accounts_as_dict(self):
        con = sqlite3.connect(self.users_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT user,usergroup AS a")
        return cur.fetchone()["a"]

    def requests_as_dict(self):
        con = sqlite3.connect(self.requests_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT user,date,status AS a")
        return cur.fetchone()["a"]

    def approve(self):
        self.c.execute("UPDATE vacations SET status = 'approved' WHERE user=? AND date=?", (self.user, self.date))
        self.closeDB()