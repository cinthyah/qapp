import webapp2
import json
from google.appengine.api import users
from twilio.rest import Client

account_sid = "ACfe3c09107ca923f7c8425fc58cbf0fc4"
auth_token = "e32ae179c853e667d8f5fc135d89c0aa"
client = Client(account_sid, auth_token)



class MainPage(webapp2.RequestHandler):
    def get(self):



app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
