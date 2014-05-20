#damasio eli gerena
#classwork day 6 or 7
# may 19th 2014
#
import webapp2
from page import *
#library for working with json in python
import json
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #seting upi the basic page
        view=FormPage()
        view.form_header="Open Weather Map Api App"
        view._css_url="css/main.css"
        # if there are url variables..
        if self.request.GET:
            code = self.request.GET['code']
            url = "http://api.openweathermap.org/data/2.5/weather?q="+code
            #go get api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            jsondoc = json.load(data)
            lat= jsondoc['coord']['lat']
            long=jsondoc['coord']['lon']
            #farenheiht to kelvins
            kel=jsondoc['main']['temp']
            view.page_content="Lat "+str(lat)+" Long "+str(long)+'<br/>'
            view.page_content+="Current temperature in Farenheit: "+str(1.8*(kel-273)+32)

        #print out
        self.response.write(view.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
