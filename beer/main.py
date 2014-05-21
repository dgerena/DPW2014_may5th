#!/usr/bin/env python
#Damasio Eli GerenaIV
#
#Beer app to get beer
import webapp2
import json
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        code = self.request.GET('code')
        url ="http://api.brewerydb.com/v2/?key=0a1a3d54ec43b25abe64eaaff2c12970"
        req =urllib2.request(url)
        opener = urllib2.build_opener()

        self.response.write('Hello world!')
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
