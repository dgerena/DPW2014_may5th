#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Damasio Eli GErena
# may 12th 2014
#
import webapp2
import json
'''
Zhao Yun
Health - 862
Attack - 866
Defense - 876
Guan Yu
Health - 872
Attack - 880
Defense - 872
Zhang Fei
Health - 876
Attack - 884
Defense - 862
Liu Bei
Health - 850
Attack - 848
Defense - 872
'''
class MainHandler(webapp2.RequestHandler):
    def get(self):# this will create the shu warriors and set there stats from the class Warriors
        shu=["Guan_Yu","Zhao_Yun","Zhang_Fei","Liu_Bei"]

        warriors = dict()

        for per in shu:
            warriors[per]= Warriors()

        print warriors


        warriors["Guan_Yu"].Hp=872
        warriors["Guan_Yu"].Att=880
        warriors["Guan_Yu"].defense=872

        warriors["Zhao_Yun"].Hp=862
        warriors["Zhao_Yun"].Att=866
        warriors["Zhao_Yun"].defense=876

        warriors["Zhang_Fei"].Hp=876
        warriors["Zhang_Fei"].Att=884
        warriors["Zhang_Fei"].defense=862

        warriors["Liu_Bei"].Hp=850
        warriors["Liu_Bei"].Att=848
        warriors["Liu_Bei"].defense=872

        home_page=Page()
        home_page.update(shu,warriors)
        self.response.write(home_page.print_out())


#warriors is the class that each shu soldier fits in
class Warriors(object):
    def __init__(self):
        self.__health=0
        self.__attack=0
        self.__defense=0

    def fight(self,attack):
        self.__health-=attack
        return self.__health

    @property
    def Hp(self):
        self.__health
        pass

    @Hp.setter
    def Hp(self,new_health):
        self.__health=new_health

    @property
    def Att(self):
        self.__attack
        pass

    @Att.setter
    def Att(self,new_attack):
        self.__attack=new_attack
'''
<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">
        <header class="col-md-6 col-md-offset-4"><h1>Prepare for the battle ahead!</h1></header>
        <section class="col-md-4">
            <select class="char-1 form-control" >
                <option > Select a Warrior: </option>
            </select>
        </section>
        <section class="col-md-4" >
            <h2 class="col-md-6">Name:health</h2>
            <h2 class="col-md-6">Name:health</h2>
            <button class="btn btn-lg">Fight</button>
        </section>
        <section class="col-md-4">
            <select class="char-2">
                <option > Select a Warrior: </option>
            </select>
        </section>
        <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
    </body>
</html>
'''
class Page(object):
    def __init__(self):
        self.warriorsObj = ""
        self.option=""
        self.__open='''
<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">'''
        self.__content="""
        <script>var warriors = {self.warriorsObj}</script>
        <header class="col-md-6 col-md-offset-4"><h1>An Ancient Battle Lies ahead!</h1></header>
        <section class="col-md-4">
            <select class="char-1 form-control" >
                {self.option}
            </select>
            <ul id="p1-stats">
            </ul>
        </section>
        <section class="col-md-4 text-center" >
            <h2 class="col-md-6">Name:health</h2>
            <h2 class="col-md-6">Name:health</h2>
            <button class="btn btn-lg">Fight</button>
        </section>
        <section class="col-md-4">
            <select class="char-2 form-control">
                {self.option}
            </select>
            <ul id="p2-stats">
            </ul>
        </section>
        """

        self.__close='''
        <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
    </body>
</html>
        '''
        self.__all=self.__open+self.__content+self.__close

    @property
    def content(self,shu):
        for i in shu:
            self.option= self.option+"<option >"+i+"</option>"
        return self.__content.format(**locals())

    @content.setter
    def content(self,new_content):

        self.__content=new_content
        self.update()# setters can have multiple lines of code thus allowing us to have it update with as many lines of code as we want

    def print_out(self):
        return self.__all

    def update(self,shu,warriors):
        self.warriorsObj = json.dumps(warriors)
        for i in shu:
            self.option= self.option+"<option >"+i+"</option>"
        #**locals() replaces all the {} with the values of the corresponding varaiables
        self.__all=self.__all.format(**locals())
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
