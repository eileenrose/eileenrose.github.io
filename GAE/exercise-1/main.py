import jinja2
import os
import webapp2 # webapp2 is a module that you import

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))# this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py


class CountHandler(webapp2.RequestHandler):
  def get(self):
    for i in range(1, 101):
      self.response.write(i)

cats = ["Ike","Chip","Dog", "Shadow", "Cheese"]

class CatHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/cats.html')

        cat_owner = {
            cats[0]: {"owner":"Bryce", "college":"Cornell"},
            cats[1]: {"owner":"Andrea", "college":"MIT"},
            cats[2]: {"owner":"Jesus", "college": "Stanford"},
            cats[3]: {"owner":"Rosy", "college": "UC Irvine"},
            cats[4]: {"owner":"Eileen"},
            "Yellow": {"owner":"Eileen"},
            "Fluff": {"owner":"Andrea", "college":"MIT"},}
        self.response.out.write(template.render(cat_owner))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/hello.html')
        template_dictionary = {
        "people": {
        "<em>Eileen</em>": {"favorite_cat": cats[4]},
        "Andrea": {"college": "MIT", "favorite_cat": cats[1]},
        "Rosy": {"college": "UC Irvine", "favorite_cat": cats[3]},
        "Bryce": {"college": "Cornell", "favorite_cat": cats[0]},
        "Jesus": {"college": "Stanford", "favorite_cat": cats[2]},
        },

        }
        self.response.out.write(template.render(template_dictionary))
"""
class MainHandler(webapp2.RequestHandler): # This is the handler class
  def get(self):
    self.response.write('Hello webapp2 world!') # replacing your print statements
"""


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/count', CountHandler),
  ('/cat', CatHandler),
], debug=True) # creates a WSGIApplication and assigns it to the variable app.
