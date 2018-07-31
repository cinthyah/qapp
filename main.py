import webapp2
import json
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
#from twilio.rest import Client


#account_sid = "ACfe3c09107ca923f7c8425fc58cbf0fc4"
#auth_token = "e32ae179c853e667d8f5fc135d89c0aa"
#client = Client(account_sid, auth_token)

#message = client.messages.create(
                              #body='Your table will be ready in five minutes',
                              #from_='17472325261',
                              #to='13107176463'#have to add variable here
                          #)

#print(message.sid)


#class MainPage(webapp2.RequestHandler):
    #def get(self):
user =users.get_current_user()

if user:
    logout_url = users.create_logout_url('/')
    greeting = ('Welcome! (<a href = "%s"> sign out</a>)'% logout_url)
else:
    login_url = users.create_login_url('/')
    greeting = '<a href ="%s">Sign in</a>'%(login_url,)

jinja_current_directory= jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template('templates/restaurant_new.html')
        self.response.write(welcome_template.render())
user.user_id()

class Event(ndb.Model):
    organizer = ndb.StringProperty(required = True)
    title = ndb.StringProperty(required = True)

Event(organizer = user.user_id(), title = "CSSI Presentations")


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler)
], debug=True)
