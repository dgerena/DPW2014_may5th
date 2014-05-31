import urllib2
import json

class Page(object):
    def __init__(self):
        self.head="""<!Doctype html>
<html>
    <head>
        <title>Beer for drinker</title>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-offset-2 col-md-8">
        <header class="col-md-12">
            <h1 class="col-md-4 col-sm-4">Beer</h1>
            <p class="col-md-8 col-sm-8">For the Beer Enthusiast, a Match made in Glass.</p>
            <form class="col-md-8 col-sm-8" method="get" action="/">
                <select name="glasswareId" class="col-md-4">
                    <option value="1">Flute</option><option value="2">Goblet</option><option value="3">Mug</option><option value="4">Pilsner</option><option value="5">Pint</option><option value="6">Snifter</option><option value="7">Stange</option><option value="8">Tulip</option><option value="9">Weizen</option><option value="10">Oversized Wine Glass</option><option value="13">Willi</option><option value="14">Thistle
                    </option>
                </select>
                <button class="btn btn-default col-md-4">FIND EPIC DRANK!</button>
            </form>
            <h2 class="col-md-12"> Select your Glass above to find the perfect libation for your chalice at hand.</h2>
        </header>"""
        self.foot="""
    </body>
</html>"""
    def Body(self):
        return self.head+self.foot

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

    def GetGlass(self,glasswareId):
        self.Get('beers','&glasswareId='+glasswareId)
        return self.obj['data']

class BeerView(Page):
    def __int__(self):
        Page.__init__(self)

    def Content(self,arr):
        description = ""
        content= u'<section class="col-md-12 col-sm-12" >'
        dataArr=arr
        for obj in arr:
            # dataArr=[]
            # dataArr=dataArr+[obj]
            # print dataArr[0]['name']
            # instead of looking for it create the key value of labels if it doesnt exist
            name = obj['name']
            try:
                icon = obj['labels']['medium']
                print obj['labels']['large']
            except:
                pass

            description = obj.pop("description", "Sorry no description set by retailer, but the best description can be found with your own palate.")
            content = content + u"""
            <article class="col-md-12">
                <h3 class="col-md-4"><img style="background-image:url({icon})" src="{icon}"/>{name}</h3>
                <p class="col-md-8">{description}</p>
            </article>"""
            content = content.format(**locals())
        content = content + u"</section>"

        return self.head +content+self.foot


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