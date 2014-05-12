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
        yoda.age=-1
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
        leia.squad_no="Pink 5"
        print leia.squad_no

class Character(object):
    def __init__(self):#constructor function, init
        self.name = ""          #properties
        self.__age = 0
        self.occupation = ""
        self.gender = ""
        self.__rogue_squadron_no ="DEFAULT"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age <0 or new_age >1000:
            print "Error with age input!!!!"
        else:
            self.__age=new_age

    #all after are methods
    def print_info(self):
        print self.name+" is a(n) "+self.occupation

    # getter, provides read access and stops write if no setter is present.
    @property
    def squad_no(self):
        return self.__rogue_squadron_no

    #setter, provides write access.
    @squad_no.setter
    def squad_no(self,new_no):
        if new_no=="Pink 5":# example of in setter validation
            new_no="Red 5"
        #showing info -more code at once!
        print new_no
        self.__rogue_squadron_no=new_no

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
