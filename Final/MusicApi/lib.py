
import json
import urllib2

class Model(object):
    def __init__(self):
        #get info
        self.url = urllib2.Request("http://rebeccacarroll.com/api/music/music.json")
        self.opener = urllib2.build_opener()
        self.jObj= self.opener.open(self.url)
        self.parse=json.load(self.jObj)

    def pRet(self):
        return self.parse['songs']['track']



    def aRet(self):
        testArr=[]
        for i in self.pRet()['songs']['track']:
            print testArr[i['title']]
        # return self.objArr

# create class to .syntax the different keys to .syntax values.

class dO(object):
    def __init__(self):
        self.data= Model.pRet()

    def Ret(self):
        return  self.data

class View(object):
    def __init__(self):
        # objArr=arr

        self.__open='''
<!Doctype html>
<html>
    <head>
        <title>Music Api</title>
        <link type="text/css" href="css/main.css">
    </head>
    <body>
        <header>
            <h1>Music</h1>
            <p>Ice Cream For The Ears!</p>
        </header>
        <aside><ul>'''

        self.nav=""

        self.ulClose='''</ul></aside>'''

        self._content=''

        self.__close='''
        <footer><p>Brought to you by Awesome Eli! 2014</p></footer>
    </body>
</html>'''

    @property
    def Content(self):
        pass

    @Content.setter
    def Content(self):
        return self._content

    def Print(self):
        self.page=self.__open+self._content+self.__close
        return self.page