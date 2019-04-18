from user_database import Database
from events_api import get_events



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
        self.D.set_interests(self.userid, self.password, newint)


    def get_events (self):
        """
        RETURNS
        -------
        a list of requests.json() objects
        """
        interests = self.get_interests()
        events = [get_events(*args) for args in interests]
        return events


    def logout (self):
        self.userid = ''
        self.password = ''
        self.D.close()





if __name__ == '__main__':
    L = Login('tw969', '199397')
