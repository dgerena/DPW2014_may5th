import urllib2
import json

class Page(object):
    def __init__(self):
        self.head="""<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="{self.css_url}" />
        <title>{self.title}</title>
    </head>
    <body>
"""
        self.foot="""
    </body>
</html>"""
    def Body(self):
        pass

    def index(self,arr):

        select = '<form method="get" action="/"><select>'
        for obj in arr:
            select = select + '<option value="'+str(obj['id'])+'">'+obj['name']+'</option>'
        select = select + '</select><button>FIND EPIC DRANK!</button></form>'
        return self.head+select+self.foot

class GetDo(object):
    def __init__(self):
        pass

    def Get(self,direct,query):
        apiKey="0a1a3d54ec43b25abe64eaaff2c12970"
        self.url ="http://api.brewerydb.com/v2/"+direct+"/?key="+apiKey+query
        self.req =urllib2.Request(self.url)
        self.opener = urllib2.build_opener()
        self.data=self.opener.open(self.req)
        self.obj=json.load(self.data)

    def GetGlass(self):
        self.Get('glassware','')
        return self.obj['data']

# class Page(object):
#     def __init__(self):
#         self._open='''
# <!Doctype html>
# <html>
#     <head>
#         <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
#         <link rel="stylesheet" type="text/css" href="{self.css_url}" />
#         <title>{self.title}</title>
#     </head>
#     <body>'''
#         self._content=''
#         self._close='''
#     </body>
# </html>
#         '''
#         self._css_url=''
#         self._title=''
#         self.all=''
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self,t):
#         self._title=t
#     @property
#     def css_url(self):
#         return self._css_url
#
#     @css_url.setter
#     def css_url(self,c):
#         self._css_url=c
#
#     def print_out(self):
#         self.update()
#         return self.all
#
#     def update(self):
#         self.all = self._open + self._content + self._close
#         self.all = self.all.format(**locals())
#
# class FormPage(Page):
#     def __init__(self):
#         #call the supers init
#         Page.__init__(self)
#         #alternate way is super(FormPage,self).__init__()
#         self.__form_open='<form method="get" action=""><select>'
#         #should use a apropriate loop to make inputs dynamic based off of given arguments.
#         self._inputs='''
#         '''
#         self.__form_close='</select class="btn"></form>'
#         self.form_header=">>Form Header<<"
#         self.page_content=''
#         self._content=self.form_header+self.__form_open+self._inputs+self._close
#
#     def update(self):
#         self.all = self._open + self.form_header+self.__form_open+self._inputs+self.__form_close+self.page_content+self._close
#         self.all = self.all.format(**locals())
# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)