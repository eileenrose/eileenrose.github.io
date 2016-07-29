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
from student import Student

class MainHandler(webapp2.RequestHandler):
    def get(self):
        student = Student(name="Adina Wallis", university="U. Mich.")
        # print student.name
        # print student.university
        # print student.birthday
        # student.put()

class AddStudentHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        school = self.request.get('school')
        student = Student(name=name, university=school)
        student.put()
        message = '<ul><li>%s, %s</li></ul>' % (name, school)
        self.response.write(message)


class listStudentsHandler(webapp2.RequestHandler):
    def get(self):
        query = Student.query().filter(Student.name == "Adina Wallis")
        student_list = query.fetch()
        for s in student_list:
            self.response.write('<p>%s</p>' % s.name)
            # s.birthday = '01/01/2000'
            # s.put()
            s.key.delete()


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add-student', AddStudentHandler),
    ('/list-students', listStudentsHandler),
], debug=True)
