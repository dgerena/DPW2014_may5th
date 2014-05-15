#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#Damasio eli GErena IV
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p =FormPage()
        p.title = "enter to all"
        p.css_url = "css/style.css"
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._open='''
<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="{self.css_url}" />
        <title>{self.title}</title>
    </head>
    <body>'''
        self._content=''
        self._close='''
    </body>
</html>
        '''
        self._css_url=''
        self._title=''
        self.all=''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,t):
        self._title=t
    @property
    def css_url(self):
        return self._css_url

    @css_url.setter
    def css_url(self,c):
        self._css_url=c

    def print_out(self):
        self.update()
        return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class FormPage(Page):
    def __init__(self):
        #call the supers init
        Page.__init__(self)
        #alternate way is super(FormPage,self).__init__()
        self.__form_open='<form method="get" action="">'
        #should use a apropriate loop to make inputs dynamic based off of given arguments.
        self.__inputs='''
        <input type='text' name='f_name' />
        <input type='text' name='l_name' />
        <input type='submit' name='f_name' />
        '''
        self.__form_close='</form>'
        self.form_header=">>Form Header<<"
        self._content=self.form_header+self.__form_open+self.__inputs+self._close

    def update(self):
        self.all = self._open + self.form_header+self.__form_open+self.__inputs+self._close+ self._close
        self.all = self.all.format(**locals())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
