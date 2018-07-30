from google.appengine.ext import ndb

class Restaurant(ndb.model):
    name = ndb.StringProperty(required = True)
    phone = ndb.StringProperty(required = True)
    street_address= ndb.StringProperty(required = True)
    city = ndb.StringProperty(required = True)
    state = ndb.StringProperty(required = True)
    zip_code = ndb.StringProperty(required = True)
