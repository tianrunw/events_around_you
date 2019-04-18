import os
import sqlite3
import hashlib



# parse user interests list to string
def list_to_string (l):
    l = ['|'.join(t) for t in l]
    return ','.join(l)


# parse user interests string to list
def string_to_list (s):
    l = s.split(',')
    l = [tuple(t.split('|')) for t in l]
    return l



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
        interests = list_to_string(interests)
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
        return string_to_list(result[0][0])


    def set_interests (self, userid, password, newint):
        self.authenticate(userid, password)
        assert(type(newint) is list)
        newint = list_to_string(newint)
        sql = """
            UPDATE events SET interests=('{}') WHERE userid='{}'
        """
        cur = self.con.cursor()
        cur.execute(sql.format(newint, userid))
        self.con.commit()





if __name__ == '__main__':
    l1 = [('Music', 'Classical'), ('Music', 'R&B'), ('Film', )]
    D = Database()
