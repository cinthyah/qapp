from google.appengine.ext import ndb

user.user_id()

class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringPRoperty(required=True)



class Restaurant(ndb.model):
    name = ndb.StringProperty(required = True)
    phone = ndb.StringProperty(required = True)
    street_address= ndb.StringProperty(required = True)
    city = ndb.StringProperty(required = True)
    state = ndb.StringProperty(required = True)
    zip_code = ndb.StringProperty(required = True)
