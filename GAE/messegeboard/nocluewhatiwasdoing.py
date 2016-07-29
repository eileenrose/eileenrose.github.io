import webapp2
import jinja2
from google.appengine.api import users
from user import User

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class forumHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('results.html')
        template_variables = {
            'message':self.request.get("message"),
            'name':self.request.get("name"),
            'email':self.request.get("email")
            }
        u = User(name=template_variables['name'], email=template_variables['email'])
        u.put()
        self.response.out.write(results_template.render(template_variables))

class ForumHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        email = self.request.get('post')
        user = User(name=name, email=email)
        user.put()
        message = '<ul><li>%s, %s</li></ul>' % (name, email)
        self.response.write(message)

class MessageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('messages.html')
        self.response.write(template.render())
    def post(self):
        results_template = jinja_env.get_template('messages.html')
        template_variables = {
            'user':self.request.get("name"),
            'timestamp':self.request.get('timestamp'),
            'text':self.request.get("text"),
            }
        m = Message(author=template_variables['user'], timestamp=template_variables['timestamp'], text=template_variables['text'])
        m.put()
        self.response.out.write(results_template.render(template_variables))


class listStudentsHandler(webapp2.RequestHandler):
    def get(self):
        query = Student.query().filter(Student.name == "Adina Wallis")
        student_list = query.fetch()
        for s in student_list:
            self.response.write('<p>%s</p>' % s.name)
            s.key.delete()


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>) (<a href ="/forum">Go to the forum page?</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/forum', forumHandler)
], debug=True)
