# Events Around You
This project is part of the STIT Backend Programming Challenge. Notice that 
the entire project is written in Python 3, and the database backend uses 
sqlite3, which is part of the Standard Python Library.

### Getting Started
As the implementation uses Python requests library to interact with remote API 
endpoint, we install it first:
```
$ pip install requests
```

Clone the repository to your local machine and `cd` into it:
```
$ git clone https://github.com/tianrunw/events_around_you.git
$ cd events_around_you
```

### Registration
The user only needs to interact with one file: `main.py`, where the main 
functions of the API take place, within the interactive Python prompt:
```
$ python -i main.py
```

To register as a new user, we call the `register` function with a userid, (for 
example your NYU NetID), a password, and a list of your interests:
```
>>> register('tw969', '199397', [('Music', 'Classical'), ('Film', 'Comedy'), ('Parking', )])
```

Notice that each interest tuple in the list takes the form of `(classificationName, genreName)`, 
where the `genreName` is not `genreID`, but the genre name. The translation is 
done behind the user. Each tuple must have at least `classificationName` at the 
first position, while `genreName` is optional, see `('Parking', )`.

### Login
The `Login` object is the only way for the user to view/change his/her preferences 
and get event information:
```
>>> L = Login('tw969', '199397')
>>> L.get_interests()
[('Music', 'Classical'), ('Film', 'Comedy'), ('Parking', )]
```

### Changing Interests
Changing interests is intuitive:
```
>>> L.set_interests([('Music', 'Classical')])
```

### Getting Events Information
```
>>> L.get_events()
[[{'name': 'Summer Symphony feat. Dennis DeYoung & the Memphis Symphony Orchestra', 'type': 'event', 'dates': {'start': {'localDate': '2019-05-24', 'localTime': '19:30:00', 'dateTime': '2019-05-25T00:30:00Z', 'dateTBD': False, 'dateTBA': False, 'timeTBA': False, 'noSpecificTime': False}, 'timezone': 'America/Chicago', 'status': {'code': 'onsale'}, 'spanMultipleDays': False}, 'info': 'Gossett Audi presents Dennis DeYoung and the music of Styx with the Memphis Symphony Orchestra Friday night, May 24th Gates open at 5:30 pm / concert at 7:30 pm. Tickets on sale Friday, April 5th at 10am through Ticketmaster.com For more information, go to www.liveatthegarden.com/summersymphony Sponsored by Gossett Audi, Radians, Sedgwick, Mednikow Jewelers, Sullivan Branding', 'classifications': [{'primary': True, 'segment': {'id': 'KZFzniwnSyZfZ7v7na', 'name': 'Arts & Theatre'}, 'genre': {'id': 'KnvZfZ7v7nJ', 'name': 'Classical'}, 'subGenre': {'id': 'KZazBEonSMnZfZ7v7nI', 'name': 'Symphonic'}, 'type': {'id': 'KZAyXgnZfZ7v7nI', 'name': 'Undefined'}, 'subType': {'id': 'KZFzBErXgnZfZ7v7lJ', 'name': 'Undefined'}, 'family': False}]}, {}]]
```
The `get_events` method returns a list of `requests.json()` objects, of which the 
ordering corresponds to the interests list. In the above example, as we changed 
our preference to just one (Classical Music), the length of the list is expected 
to be one.

### Logout
```
>>> L.logout()
```
The `logout` method closes the connection to the database. All operations on `L` 
thereafter will throw an unhandled exception.

### Database Details
1. Everything is stored on disk in `events.sqlite` in the same directory, and thus 
information is persisted across runs.
2. The non-salted, SHA-256 hashed password is stored in the database and in no 
circumstance is the plain-text equivalent recorded.
3. The interests list is parsed into a `,` and `|` delimited string and stored 
in the database as `TEXT` type.
