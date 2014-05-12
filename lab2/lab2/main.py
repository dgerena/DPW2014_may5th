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

from pages import HTMLPage

class MainHandler(webapp2.RequestHandler):
        # This is the catalyst - to start our web app
        #when the app loads this function gets called automaticaly
        # V
    def get(self):
        p=HTMLPage()# cals constructor __init__ function inside of HTMLPage class
        ##atribute:
        #instance.attribute
        ##method
        #instance.method()

        if self.request.GET:
            fn=self.request.get(self.request.GET['firstName'])
            ln=self.request.get(self.request.GET['lastName'])
            self.response.write(p.print_out(fn +" "+ ln))

        self.response.write(p.print_out("Oh hell naw!!!"))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
