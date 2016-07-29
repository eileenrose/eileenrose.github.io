from google.appengine.ext import ndb

# Message {
# timestamp: Integer
# author: String
# text: String
# }

class Message(ndb.Model):
    timestamp = ndb.IntegerProperty(required=True)
    author = ndb.StringProperty(required=True)
    text = ndb.StringProperty(required=True)
