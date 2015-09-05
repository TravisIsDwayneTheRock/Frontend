import webapp2
import json
from google.appengine.ext import ndb

class User(ndb.Model):
    """Models an individual Guestbook entry with content and date."""
    username = ndb.StringProperty()
  	password = ndb.StringProperty()
  	conversations = ndb.StringProperty(repeated=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.date)

class Conversation(ndb.Model):
	conversationID = ndb.StringProperty
	messages = ndb.StructuredProperty(Message,repeated=True)

class Message(ndb.Model):
	user1 = ndb.StringProperty()
	user2 = ndb.StringProperty()
	time = ndb.DateTimeProperty()
	message = ndb.StringProperty()




class conversation(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'application/json'
		self.response.write(self.request.params)

app = webapp2.WSGIApplication([
	('/conversation', conversation)
], debug=True)
