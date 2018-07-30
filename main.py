import webapp2
import json
from google.appengine.api import users



class MainPage(webapp2.RequestHandler):
    def get(self):



app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
