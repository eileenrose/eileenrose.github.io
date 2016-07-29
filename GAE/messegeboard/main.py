#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
from google.appengine.api import users
from data_model import Message
import time


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url('/'))
        else:
            self.show_message_board()

    def show_message_board(self):
        template = jinja_env.get_template('messages.html')
        messages = self.get_messages()
        variables = {
        'username': users.get_current_user().nickname(),
        'logout_url': users.create_logout_url('/'),
        'messages_list': messages,
        }
        self.response.write(template.render(variables))

    def get_messages(self):
        query = Message.query().order(-Message.timestamp) # - in front to reverse order
        messages = query.fetch()
        return messages


class PostMessageHandler(webapp2.RequestHandler):
    def post(self):
        username = users.get_current_user().nickname()
        message_text = self.request.get('text')
        now = int(time.time()*1000)
        new_message = Message(timestamp=now, author=username, text=message_text)
        print '/n%s/n' % new_message
        key = new_message.put()
        time.sleep(0.5)
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post-message', PostMessageHandler)
], debug=True)
