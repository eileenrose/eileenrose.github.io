from google.appengine.ext import ndb
    # https://cloud.google.com/appengine/docs/python/ndb/

class Student(ndb.Model):
  name = ndb.StringProperty(required=True)
  university = ndb.StringProperty(required=True)
  birthday = ndb.StringProperty(required=False)
