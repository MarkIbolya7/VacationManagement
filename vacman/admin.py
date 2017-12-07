import sqlite3
import os


class Admin:
    def __init__(self):
        self.users_path = os.path.dirname(os.path.realpath(__file__)) + "/../users.sqlite"
        self.requests_path = os.path.dirname(os.path.realpath(__file__)) + "/../vacations.sqlite"

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def accounts_as_dict(self):
        con = sqlite3.connect(self.users_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT user, usergroup FROM accounts")
        return_data = cur.fetchall()
        con.close()
        return return_data

    def requests_as_dict(self):
        con = sqlite3.connect(self.requests_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("SELECT user, date, status FROM vacations")
        return_data = cur.fetchall()
        con.close()
        return return_data

    def change_request(self, user, date, status):
        con = sqlite3.connect(self.requests_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("UPDATE vacations SET status = ? WHERE user = ? AND date = ?", (status, user, date))
        con.commit()
        con.close()

    def change_user_info(self, user, usergroup):
        con = sqlite3.connect(self.users_path)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute("UPDATE accounts SET usergroup = ? WHERE user = ?", (usergroup, user))
        con.commit()
        con.close()
