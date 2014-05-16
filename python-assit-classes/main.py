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

class Page(object):
    def __init__(self):
        self.option=""
        self.stats=""
        self.result=""
        self.__open='''
<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">'''
        self.__content="""

        <header class="col-md-6 col-md-offset-4">
            <h1>TBD</h1>
        </header>
        <div class="main-content">
            <h1>Replace Me with content!</h1>
        </div>
        <footer></footer>
        """
        self.__close='''
        <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
    </body>
</html>
        '''
        self.__all=self.__open+self.__content+self.__close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
