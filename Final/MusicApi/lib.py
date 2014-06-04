class Model(object):
    def __init__(self):
        pass

class View(object):
    def __init__(self):

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
        <aside><ul></ul></aside>'''

        self._content=''

        self.__close='''
        <footer><p>Brought to you by Awesome Eli! 2014</p></footer>
    </body>
</html>'''

    @getter
    def Content(self):
        self.

    def Print(self):
        self.page=self.__open+self.content+self.__close
        return self.page