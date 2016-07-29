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
import json
import urllib2



class MainHandler(webapp2.RequestHandler):
    def get(self):
        response = urllib2.urlopen("http://api.randomuser.me/?results=3")
        content = response.read()
        content_obj = json.loads(content)
        name1 = content_obj['results'][0]['name']['first']
        email1 = content_obj['results'][0]['email']
        state1 = content_obj['results'][0]['location']['state']
        name2 = content_obj['results'][1]['name']['first']
        email2 = content_obj['results'][1]['email']
        state2 = content_obj['results'][1]['location']['state']
    #    print "my name is " + name + " and my email is " + email + "."  shows up in log
        msg1 = "My name is %s (%s), and I live in %s." % (name1, email1, state1)
        msg2 = "My name is %s (%s), and I live in %s." % (name2, email2, state2)
        self.response.write(msg1+"<br>"+msg2)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
