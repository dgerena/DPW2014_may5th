#!/usr/bin/env python
# Damasio Eli Gerena IV
# Final Exam Practical
# June 4th 2014
import webapp2
import json
import urllib2
from lib import *


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stuff = "<h1>hello</h1>"
        html = View()
        html._content='''<h1>test</h1>'''
        # jObj = Model().pRet()
        test = DO()
        print test.ret()
        self.response.write(html.Print())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
