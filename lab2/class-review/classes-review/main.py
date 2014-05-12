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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        yoda =Character()
        yoda.name="Yoda"
        yoda.age=900
        yoda.gender="Male"
        yoda.occupation="Jedi Master"
        yoda.print_info()
        #instance.attribute
        #instance.method()
        #instance.property

        luke=Character()
        luke.name="Luke Skywalker"
        luke.gender="Male"
        luke.age="24"
        luke.occupation="Farmer"
        luke.print_info()

        leia=Character()
        leia.name="Leia Organa"
        leia.gender="Female"
        leia.age=luke.age
        leia.occupation="Princess"
        leia.print_info()

class Character(object):
    def __init__(self):
        self.name =""
        self.age =0
        self.occupation =""
        self.gender=""

    def print_info(self):
        print self.name+" is a(n) "+self.occupation

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
