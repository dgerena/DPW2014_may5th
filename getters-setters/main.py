#!/usr/bin/env python
#   Damasio Eli gerena
#getters setters notes
#may 12 2014
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_page=Page()
        home_page.title="Contact Us"
        home_page.update()

        contact_page=Page()
        contact_page.title="Contact Us"
        contact_page.update()
        self.response.write(contact_page.print_out())

class Page(object):
    def __init__(self):
        self.__title="Home Page"
        self.__open='''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
    </head>
    <body>'''
        self.__content="""
        hello!
        """

        self.__close='''
    </body>
<html>
        '''
        self.__all=self.__open+self.__content+self.__close

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,new_title):
        self.__title=new_title
        self.update()# setters can have multiple lines of code thus allowing us to have it update with as many lines of code as we want

    def print_out(self):
        return self.__all

    def update(self):
        #**locals() replaces all the {} with the values of the corresponding varaiables
        self.__all=self.__all.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
