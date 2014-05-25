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
        pint=5
        # beer glass keys of note. totalResults,data[]<this will let you choose a result
        BeerGlassSearch=self.BeerSearch(pint)

        # BeerGlassSearch['data'][0] this wil return the first(array num 0) search result for a *beer *search of *pint
        # available gives a obj that has a descript. and name stating weather year round or otherwise.
        print BeerGlassSearch['data'][0]['available']
        k=''
        for i in glassObj['data']:
            k+='<option href="/?'+str(i['name'])+' >'+str(i['name'])+'</option>'
        h=''
        for j in BeerGlassSearch['data']:
            h+='<div>'+str(j)+'</div>'
        view._inputs=k
        self.response.write(str(view.print_out())+str(h))



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
        url ="http://api.brewerydb.com/v2/?key=0a1a3d54ec43b25abe64eaaff2c12970"
        req =urllib2.Request(url)
        opener = urllib2.build_opener()
        data=opener.open(req)
        obj=json.load(data)
        return obj

    def BeerSearch(self,glassId):
        url ="http://api.brewerydb.com/v2/beers?key=0a1a3d54ec43b25abe64eaaff2c12970&glasswareId="+str(glassId)
        req =urllib2.Request(url)
        opener = urllib2.build_opener()
        data=opener.open(req)
        obj=json.load(data)
        return obj


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
