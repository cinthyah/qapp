import webapp2
import json
import jinja2
import os
from google.appengine.api import users
import models
import seed_q
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




class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        #if statement that checks if user is logged in via google
        if user:
            log_url = users.create_logout_url('/')
            #check if user is in Restaurant Datastore already/is a returning user
            user_email = user.user_email()
            rest_query =Restaurant.query(Restaurant.user == user_email).fetch()
            #if user email is in Restaurant Datastore go to home page/ else send to new restaurant handler
            if rest_query[0].user != None :
                self.redirect('/r_home')
            else:
                self.redirect('/new_rest')

        else:
            log_url = users.create_login_url('/')
        new_r_template=jinja_current_directory.get_template("templates/login2.html")
        self.response.write(new_r_template.render({'log_url': log_url}))

class HomeHandler(webapp2.RequestHandler):
    def get(self):



class RestNewHandler(webapp2.RequestHandler):
    def get(self):
        new_r_template=jinja_current_directory.get_template("templates/restaurant_new.html")
        self.response.write(new_r_template.render())

    def post(self):
        user = users.get_current_user()
        Restaurant(name = self.request.get('name_r'),
            phone = self.request.get('phone_r'),
            street_address = self.request.get('street'),
            city = self.request.get('city'),
            state = self.request.get('state'),
            zip_code = self.request.get('zip'),
            user = user.email(),
            ).put()

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_q.seed_data()


app = webapp2.WSGIApplication([
    ('/',LoginHandler),
    ('/r_home', HomeHandler),
    ('/new_rest', RestNewHandler),
    ('/seed-data', LoadDataHandler),
], debug=True)
