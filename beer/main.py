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
        view = FormPage()
        view.form_header = "Beer"
        view._css_url="css/main.css"
        # glassware section
        glassObj=self.Glassware()
        dataObj= self.data()
        print dataObj
        k=''
        for i in glassObj['data']:
            k+='<option >'+str(i['name'])+'</option>'
        view._inputs=k
        self.response.write(str(view.print_out()))



    def Glassware(self):
        look="glassware"
        params=''
        url ="http://api.brewerydb.com/v2/glassware?key=0a1a3d54ec43b25abe64eaaff2c12970"
        req =urllib2.Request(url)
        opener = urllib2.build_opener()
        data=opener.open(req)
        obj=json.load(data)
        return obj

    def data(self):
        look="glassware"
        params=''
        url ="http://api.brewerydb.com/v2/?key=0a1a3d54ec43b25abe64eaaff2c12970"
        req =urllib2.Request(url)
        opener = urllib2.build_opener()
        data=opener.open(req)
        obj=json.load(data)
        return obj


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
