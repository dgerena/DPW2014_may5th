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
        # so i need to count...
        #vvv current number i start with
        currentCount=0
        # instance of count
        newCount=Count()
        if self.request.GET:
            print newCount.currentCount
            newCount.add
            self.response.write("Your current number is "+str(newCount.currentCount)+".<br /> <a href='/?"+str(newCount.currentCount+newCount.add)+"'><button action='get'>Add</button></a>")
        else:
            self.response.write("Your current number is "+str(newCount.currentCount)+".<br /> <a href='/?"+str(newCount.currentCount)+"'><button action='get'>Add</button></a>")
        #well cant remmber how to do it...


class Count(object):
    def __init__(self):
        #wanted to hold a number here
        self.currentCount=0
        #have a var for adding


    @property
    def add(self):

        pass

    @add.setter
    def add(self,number):
        #have the current count set useing add
        self.currentCount=self.currentCount+number
        #return the new current number
        return self.currentCount


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
