from user_database import Database



def register (userid, password, interests):
    D = Database()
    D.register(userid, password, interests)
    D.close()



class Login (object):

    def __init__ (self, userid, password):
        self.D = Database()
        try:
            self.D.authenticate(userid, password)
        except:
            self.D.close()
            raise

        self.userid = userid
        self.password = password


    def get_interests (self):
        return self.D.get_interests(self.userid, self.password)


    def set_interests (self, newint):
        return self.D.set_interests(self.userid, self.password, newint)