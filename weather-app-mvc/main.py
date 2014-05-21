#damasio eli gerena
#classwork day 6 or 7
# may 19th 2014
#
import webapp2
from page import *

#library for working with xml in python
from xml.dom import minidom
import urllib2
# for this class the mainhandler will be a bit of a suedo controller..
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #seting upi the basic page
        view=FormPage()
        view.form_header="Yahoo's Weather App"
        view._css_url="css/main.css"

        # if there are url variables..
        if self.request.GET:
            self.__code = self.request.GET['code']
            w_model=WeatherModel() #creates a instance of the model
            w_model.code=self.request.GET['code'] # passes the url var into the model
            w_model.send_req() #connect to API

        #     #look at elements within the xml
        #     list = xmldoc.getElementsByTagName('yweather:forecast')
        #     c= xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue+"<br />"
        #     for item in list:
        #         c += item.attributes['day'].value
        #         c += " | High of: "+item.attributes['high'].value
        #         c += " | Low of: "+item.attributes['low'].value
        #         c += " | Condition: "+item.attributes['text'].value
        #         c += '<br /><img src="images/'+item.attributes['self.__code'].value+'.png" />'
        #         c += '<br />'
        #
        #     # self.response.write(c)
        #     view.page_content=c #passes that string into our form content
        #
        # #print out
        self.response.write(view.print_out())

class WeatherModel(object):
    '''This is the weather model handles data requests and sorting of data from api.'''
    def __init__(self):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.full_url=''
        self.__code=''

    def send_req(self):
        #go get api info
        self.full_url=self.url+self.__code
        req = urllib2.Request(self.full_url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        #parse it
        xmldoc = minidom.parse(data)
        #find the tag that we want.. and put that info into the wdo
        self.__wdo=WeatherDataObject()#create instance of data object class
        condition= xmldoc.getElementsByTagName('yweather:condition')
        self.__wdo.condition=condition[0].attributes['text'].value
        self.__wdo.temp=condition[0].attributes['temp'].value
        self.__wdo.code=condition[0].attributes['code'].value
        # print condition[0].attributes['text'].value

# '''nodes:
#     <tag>
#         <x>
#             <tag></tag>
#     in the above you would have to use firsChild to understand where it is.
#
#     if a tag has no end tag and is self closing you will not need a specific such as firstChild you may still need to use [] as if it was an array
# '''

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self,c):
        self.__code=c

class WeatherDataObject(object):
    '''This holds the information sent by the api '''
    def __init__(self):
        self.location=''
        self.temp=''
        self.condition=''
        self.code=0 #this is the weather code (not the zip code).


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
