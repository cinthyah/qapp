from google.appengine.ext import ndb


class Event(ndb.Model):
    organizer = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)


class Restaurant(ndb.Model):
    name = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    street_address= ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    zip_code = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)

class Table(ndb.Model):
    max= ndb.StringProperty(required=True)
    table_name=ndb.StringProperty(required=False)
    restaurant_id = ndb.KeyProperty(Restaurant)
    full = ndb.BooleanProperty(required=True)
    time_filled = ndb.DateTimeProperty(required=False)

class Wait(ndb.Model):
    customer = ndb.StringProperty(required=True)
    phone = ndb.StringProperty(required=True)
    party_size = ndb.StringProperty(required=True)
    restaurant_key = ndb.KeyProperty(Restaurant, required=True)
    table_type = ndb.KeyProperty(Table)
    time = ndb.DateTimeProperty(required=True, auto_now_add=True)
