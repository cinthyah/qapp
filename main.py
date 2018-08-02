import webapp2
import json
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import time
from models import Restaurant,Table,Wait
import datetime
import seed_q
import json
import logging
#from twilio.rest import Client

#
#account_sid="ACfe3c09107ca923f7c8425fc58cbf0fc4"
#auth_token="e32ae179c853e667d8f5fc135d89c0aa"
#client=Client(account_sid, auth_token)


#message=client.messages.create(
                              #body='Your table will be ready in five minutes',
                              #from_='17472325261',
                              #to='13107176463'#have to add variable here
                          #)




#class MainPage(webapp2.RequestHandler):
    #def get(self):


jinja_current_directory= jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

secrets_file = open('app-secrets.json')
SECRETS = json.load(secrets_file)
secrets_file.close()

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        #if statement that checks if user is logged in via google
        if user:
            log_url=users.create_logout_url('/')
            #check if user is in Restaurant Datastore already/is a returning user
            user_email=user.email()
            rest_query =Restaurant.query(Restaurant.user == user_email).fetch(1)

            #if user email is in Restaurant Datastore go to home page/ else send to new restaurant handler
            if rest_query != [] :
                self.redirect('/tables')
            else:
                self.redirect('/new_rest')
        #if user not logged into google, generates login
        else:
            log_url=users.create_login_url('/')
        #renders login2 html page with link to login url for unlogged in users
        login_template=jinja_current_directory.get_template("templates/login2.html")
        self.response.write(login_template.render({'log_url': log_url}))

class RestNewHandler(webapp2.RequestHandler):
    def get(self):
        #render's html page for new restaurant handler
        log_url = users.create_logout_url('/')
        template_vars ={
        "log_url":log_url
        }
        new_r_template=jinja_current_directory.get_template("templates/restaurant_new.html")
        self.response.write(new_r_template.render(template_vars))

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

        Table(description = self.request.get('table_description'),
            max = self.request.get('table_size_max'),
            min = self.request.get('table_size_min'),
            #restaurant_id = self.request.get(),
            full = False,
            time_filled = datetime.datetime.now(),
        ).put()


class CustNewHandler(webapp2.RequestHandler):
    def get(self):
        new_r_template=jinja_current_directory.get_template("templates/add_customer.html")
        self.response.write(new_r_template.render())

    def post(self):
        Wait(customer = self.request.get('c_name'),
            phone = self.request.get('c_number'),
            party_size = self.request.get('c_party'),
            #restaurant_key = self.request.get('INSERT'),
            #table_type = self.request.get('INSERT'),
            time = datetime.datetime.now(),
        ).put()

class TablesHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        restaurant = Restaurant.query(Restaurant.user == user.email()).fetch()
        if restaurant:
            log_url = users.create_logout_url('/')
            restaurant = restaurant[0]
            tables = Table.query(Table.restaurant_id == restaurant.key).order(Table.time_filled).fetch()
            template_vars = {
            "tables" : tables,
            "restaurant":restaurant,
            "log_url":log_url,
            }
            tables_template=jinja_current_directory.get_template("templates/tables.html")
            self.response.write(tables_template.render(template_vars))

        else:
            self.response.write(users.create_logout_url('/'))

    def post(self):
        pass

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_q.seed_data()

class ActiveQHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        restaurant = Restaurant.query(Restaurant.user == user.email()).fetch()
        if restaurant:
            restaurant = restaurant[0]
            waits = Wait.query(Wait.restaurant_key == restaurant.key).order().fetch()
            template_vars = {
            "waits" : waits,
            "restaurant":restaurant,
            "twilio_account_sid":SECRETS["twilio_account_sid"],
            "twilio_auth_token":SECRETS["twilio_auth_token"],
             }

            activeq_template = jinja_current_directory.get_template("templates/active_q.html")
            self.response.write(activeq_template.render(template_vars))
        else:
            self.response.write(users.create_logout_url('/'))


class DeleteWaitHandler(webapp2.RequestHandler):
    def get(self):
        wait_key = ndb.Key(urlsafe=self.request.get('wait_id'))
        wait_key.delete()
        time.sleep(0.5)
        self.redirect("/a_queue")


class NotifyHandler(webapp2.RequestHandler):
    def get(self):
        pass

class UpTabUseHandler(webapp2.RequestHandler):
    def get (self):
        used = self.request.get('used')
        table_key = ndb.Key(urlsafe = self.request.get('table_id'))
        logging.info(table_key)
        #uses value to be not value that was
        table = table_key.get()
        if used == 'False':
            #table = Table.get_by_id(table_id)
            table.full= True
            table.time_filled=datetime.datetime.now()
        else:
            #table = Table.get_by_id(table_id)
            table.full= False
            table.time_filled= None
        table.put()
        time.sleep(0.5)
        self.redirect("/tables")

app=webapp2.WSGIApplication([
    ('/',LoginHandler),
    ('/new_rest', RestNewHandler),
    ('/new_cust', CustNewHandler),
    ('/tables', TablesHandler),
    ('/seed-data', LoadDataHandler),
    ('/a_queue', ActiveQHandler),
    ('/delete', DeleteWaitHandler),
    ('/update_table_use',UpTabUseHandler)
], debug=True)
