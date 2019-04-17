import os
import sqlite3
import hashlib



class Database (object):

    def __init__ (self):
        sql_file = "events.sqlite"

        if os.path.exists(sql_file):
            self.con = sqlite3.connect(sql_file)
        else:
            self.con = self._init_database(sql_file)


    def _init_database (self, sql_file):
        sql = """
            CREATE TABLE events (
                userid TEXT PRIMARY KEY, 
                password TEXT,
                interests TEXT
            )
        """
        con = sqlite3.connect(sql_file)
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        return con


    def close (self):
        self.con.close()


    def authenticate (self, userid, password):
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        sql = """
            SELECT (password) FROM events WHERE userid='{}'
        """
        cur = self.con.cursor()
        cur.execute(sql.format(userid))
        result = cur.fetchall()
        
        if (len(result) > 0) and (result[0][0] == hashed):
            return
        else:
            raise ValueError("Authentication failed")


    def register (self, userid, password, interests):
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        assert(type(interests) is list)
        interests = ','.join(interests)
        sql = """
            INSERT INTO events VALUES ('{}', '{}', '{}')
        """
        sql = sql.format(userid, hashed, interests)
        cur = self.con.cursor()
        try:
            cur.execute(sql)
            self.con.commit()
        except sqlite3.IntegrityError:
            raise ValueError("User ID already exists")


    def get_interests (self, userid, password):
        self.authenticate(userid, password)
        sql = """
            SELECT (interests) FROM events WHERE userid='{}'
        """
        cur = self.con.cursor()
        cur.execute(sql.format(userid))
        result = cur.fetchall()
        assert(len(result) > 0)
        return result[0][0].split(',')


    def set_interests (self, userid, password, newint):
        self.authenticate(userid, password)
        assert(type(newint) is list)
        newint = ','.join(newint)
        sql = """
            UPDATE events SET interests=('{}') WHERE userid='{}'
        """
        cur = self.con.cursor()
        cur.execute(sql.format(newint, userid))
        self.con.commit()





if __name__ == '__main__':
    D = Database()
