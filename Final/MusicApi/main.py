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
        html = View(DO().arWdict)
        if not self.request.GET:
            html._content='''<h1>Please Select A Track</h1>'''
            self.response.write(html.Print())
        else:
            keyVar=self.request.GET['index']# if i use index instead of title i believe i can workfrom there.
            html.tView(keyVar)
            self.response.write(html.Print())
            # this will set the content apropriately by passin in the  keyvar

        # jObj = Model().pRet()
        # test = DO()
        # print test.ret()
        # self.response.write(html.Print())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
