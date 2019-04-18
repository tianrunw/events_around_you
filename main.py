from user_database import Database
from events_api import get_events



def register (userid, password, interests):
    """
    PARAMETERS
    ----------
    userid: str
    password: str
    interests: list of tuples of strings
        e.g. [(classificationName, genreName), ...]

    RETURNS
    -------
    None

    ATTENTION
    ---------
    1. genreName is the name of the genre, not genreID
    2. each tuple must contain at least classificationName, genreName is 
       optional, e.g. [('Film', 'Comedy'), ('Parking', )]
    """
    D = Database()
    try:
        D.register(userid, password, interests)
    except:
        raise
    finally:
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
        """
        RETURNS
        -------
        list of tuples of strings, same format given by user
        """
        return self.D.get_interests(self.userid, self.password)


    def set_interests (self, newint):
        """
        PARAMETERS
        ----------
        newint: list of tuples of strings
            e.g. [(classificationName, genreName), ...]

        RETURNS
        -------
        None

        ATTENTION
        ---------
        1. genreName is the name of the genre, not genreID
        2. each tuple must contain at least classificationName, genreName is 
           optional, e.g. [('Film', 'Comedy'), ('Parking', )]
        """
        self.D.set_interests(self.userid, self.password, newint)


    def get_events (self):
        """
        RETURNS
        -------
        a list of requests.json() objects each containing event info, the 
        ordering corresponds to interests list exactly
        """
        interests = self.get_interests()
        events = [get_events(*args) for args in interests]
        return events


    # client's responsibility to reqlinquish database resources
    def logout (self):
        self.D.close()





if __name__ == '__main__':
    l1 = [('Music', 'Classical'), ('Film', 'Comedy'), ('Parking', )]
