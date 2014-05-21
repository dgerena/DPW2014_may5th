#damasio eli gerena
#classwork day 6 or 7
# may 19th 2014
#
import webapp2
from page import *

#library for working with xml in python
from xml.dom import minidom
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #seting upi the basic page
        view=FormPage()
        view.form_header="Yahoo's Weather App"
        view._css_url="css/main.css"
        # if there are url variables..
        if self.request.GET:
            code = self.request.GET['code']
            url = "http://xml.weather.yahoo.com/forecastrss?p="+code
            #go get api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            xmldoc = minidom.parse(data)
            #look at elements within the xml
            list = xmldoc.getElementsByTagName('yweather:forecast')
            c= xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue+"<br />"
            for item in list:
                c += item.attributes['day'].value
                c += " | High of: "+item.attributes['high'].value
                c += " | Low of: "+item.attributes['low'].value
                c += " | Condition: "+item.attributes['text'].value
                c += '<br /><img src="images/'+item.attributes['code'].value+'.png" />'
                c += '<br />'
            # self.response.write(c)
            view.page_content=c #passes that string into our form content
        #print out
        self.response.write(view.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
