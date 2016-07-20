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
#import logging
import jinja2
import os


#class GoodbyeHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Goodbye, world!')
"""
class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 101):
            self.response.write(i)

def is_prime(n):
  #A simple (but inefficient) check to see whether a number is prime.
  if n == 2:
      return True
  for possible_factor in range(2, n):
      if n % possible_factor == 0:
          logging.info('Found a factor: %d', possible_factor)
          return False
  return True


class MainHandler(webapp2.RequestHandler):
  def get(self):

    n = 9
    if is_prime(n):
      self.response.write('%d is prime' % n)
    else:
      self.response.write('%d is not prime' % n)



def talk_like_a_pirate(sentence):
  #Converts a sentence to pirate-speak.
  # Strip whitespace and punctuation.
  sentence = sentence.strip().rstrip('.!')

  # Lowercase the first letter of the sentence.
  sentence = sentence[0].lower() + sentence[1:]

  # Piratify the text.
  sentence = 'Yarr, ' + sentence + ', me hearties.'

  return sentence

class MainHandler(webapp2.RequestHandler):
  def get(self):
    sentence = 'Hello, world!'
    self.response.write(talk_like_a_pirate(sentence))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    if True:
      self.response.write('The truth will set you free.')
    else:
      self.response.write('How did I get here?')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
"""


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/count', CountHandler),
    #('/bye', GoodbyeHandler),
], debug=True)
