import webapp2
import json
import jinja2
import os
from google.appengine.api import users
import models
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


jinja_current_directory= jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = Event.query().fetch()
            self.redirect('/new_rest')
        else:
            login_prompt_template = jinja_current_directory.get_template('templates/login2.html')
            self.response.write(login_prompt_template.render({'login_link': users.create_login_url('/')}))

class RestNewHandler(webapp2.RequestHandler):
    def get(self):
        new_r_template=jinja_current_directory.get_template("templates/restaurant_new.html")
        self.response.write(new_r_template.render({'templates': templates}))

    def post(self):
        Restaurant(name = self.request.get('name_r'),
            phone = self.request.get('phone_r'),
            street_address= self.request.get('street'),
            city = self.request.get('city'),
            state = self.request.get('state'),
            zip_code = self.request.get('zip'),
        ).put()


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/new_rest', RestNewHandler),
], debug=True)
