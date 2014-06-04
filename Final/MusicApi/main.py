#!/usr/bin/env python
# Damasio Eli Gerena IV
# Final Exam Practical
# June 4th 2014
import webapp2
import json
import urllib2
import lib


class MainHandler(webapp2.RequestHandler):
    def get(self):
        html=lib.View()
        self.response.write(html.Print())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
