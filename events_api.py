import requests

API = 'https://yv1x0ke9cl.execute-api.us-east-1.amazonaws.com/prod/events'
USER = 'stitapplicant'
TOKEN = 'zvaaDsZHLNLFdUVZ_3cQKns'

FIELDS = ["Arts & Theatre", "Film", "Miscellaneous", "Music", "Sports", 
          "Undefined", "Donation", "Event Style", "Group", "Individual", 
          "Merchandise", "Nonticket", "Parking", "Transportation", "Upsell", 
          "Venue Based"]

GENRES = {'R&B':'KnvZfZ7vAee',
          'Hip­Hop/Rap':'KnvZfZ7vAv1',
          'Comedy':'KnvZfZ7vAe1',
          'Classical': 'KnvZfZ7v7nJ',
          'Jazz':'KnvZfZ7vAvE',
          'Foreign':'KnvZfZ7vAk1',
          'Dance/Electronic':'KnvZfZ7vAvF',
          'Comedy':'KnvZfZ7vAkA',
          'Animation':'KnvZfZ7vAkd',
          'Music':'KnvZfZ7vAkJ',
          'Miscellaneous':'KnvZfZ7vAka',
          'Family':'KnvZfZ7vAkF',
          'Miscellaneous Theatre':'KnvZfZ7v7ld',
          'Theatre':'KnvZfZ7v7l1'}



def get_events (field, genre=None):
    if genre in GENRES:
        payload = {'classificationName':field, 'genreId':GENRES[genre]}
    else:
        payload = {'classificationName':field}

    r = requests.get(API, auth=(USER, TOKEN), params=payload)
    return r.json()





if __name__ == '__main__':
    E = get_events('Music', 'Classical')
