#!/usr/bin/env python
#Damasio Eli GerenaIV
#
#Beer app to get beer
import webapp2
import json
import urllib2
from page import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view=FormPage()
        view.form_header="Open Weather Map Api App"
        view._css_url="css/main.css"
        look=""
        params=""
        # if there are url variables..
        if self.request.GET:
            code = self.request.GET['code']
            url ="http://api.brewerydb.com/v2/"+look+"?"+params+"key=0a1a3d54ec43b25abe64eaaff2c12970"
            req =urllib2.Request(url)
            opener = urllib2.build_opener()
            data=opener.open(req)
            obj=json.load(data)
            self.response.write(obj)
        else:
            print "doesnt work."

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
