import webapp2
import json
from google.appengine.api import users
from twilio.rest import Client


account_sid = "ACfe3c09107ca923f7c8425fc58cbf0fc4"
auth_token = "e32ae179c853e667d8f5fc135d89c0aa"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Your table will be ready in five minutes',
                              from_='17472325261',
                              to='13107176463'#have to add variable here
                          )

print(message.sid)


class MainPage(webapp2.RequestHandler):
    def get(self):

class LoginPage(webapp2.RequestHandler):
    def post(self):
        user = user.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = user.nickname()
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)'
              % (nickname, logout_url))
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="%s">Sign in</a>' % (login_url,)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage)
], debug=True)
