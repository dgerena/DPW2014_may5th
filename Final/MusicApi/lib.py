
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
        for i in self.pRet()['songs']['track'][0]:
            print testArr[i['title']]
        return testArr

# create class to .syntax the different keys to .syntax values.

class DO(object):
    def __init__(self):
        self.__data = Model().pRet()
        self.tList =''
        # print self.__data
        this=[{}]
        count=0
        try:
            this.pop(0)
            for each in self.__data:
                if each['title'] == "Satisfaction" or "Respect":
                    this = this + [{u'index': count, u'cover':each['cover'],u'title':each['title'],u'artist':each['artist'],u'length':each['length'],u'year':each['year'],u'label':each['label']}]
                else:
                    this = this + [{u'index': count, u'file':each['file'],u'cover':each['cover'],u'title':each['title'],u'artist':each['artist'],u'length':each['length'],u'year':each['year'],u'label':each['label']}]
                count=count+1
        finally:
            pass
        self.arWdict=this

        # for tracks in self.__data:
        #     self.tList += str(tracks)
        # # print self.tList

    @property
    def ret(self):
        return self.arWdict


class View(object):
    def __init__(self,arr):
        self.__objArr=arr
        self.list=''


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
        for track in self.__objArr:
            self.nav=self.nav+'<li><a href="?index='+str(track['index'])+'">'+str(track['title'])+'</a></li>'

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

    def tView(self,index):
        track=self.__objArr
        print index
        print track[int(index)]

        content=""
        for each in track:
            if track[int(index)]['index'] == each['index'] :
                try:
                    print "correct"
                    self._title = track[int(index)]['title']
                    self._artist = track[int(index)]['artist']
                    self._length = track[int(index)]['length']
                    self._year = track[int(index)]['year']
                    self._cover = track[int(index)]['cover']
                except:
                    self._fileUrl = track[int(index)]['File']
                finally:
                    pass
                    #     <li><audio src="{track.__file}></li>


                content='<li><img src="'+self._cover+'"></li><h2>'+self._title+'</h2><ul><li>Artist: '+self._artist+'</li><li>Track Length: '+self._length+'</li><li>Year Produced: '+self._year+'</li><li><p><a href="+self._fileUrl+">Play Me If Available</a></p></li></ul>'
            else:
                pass

            self._content=content

    def Print(self):
        self.page=self.__open+self.nav+self.ulClose+self._content+self.__close
        return self.page