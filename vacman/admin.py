import time
import sqlite3

import os


class Admin():

    def __init__(self):

        self.dbfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../users.sqlite"
        pass

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def users_as_dict(self):
        con = sqlite3.connect(self.dbfile_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT 1 AS a")
        return cur.fetchone()["a"]

    def accounts_as_dict(self):
        con = sqlite3.connect(self.dbfile_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT 1 AS a")
        return cur.fetchone()["a"]

    def approve(self):
        self.c.execute("UPDATE vacations SET status = 'approved' WHERE user=? AND date=?", (self.user, self.date))
        self.closeDB()