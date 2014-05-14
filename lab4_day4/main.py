#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Damasio Eli GErena
# may 12th 2014
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):# this will create the shu warriors and set there stats from the class Warriors
        shu=[{"name":"Guan_Yu","health":872,"Att":880,"defense":872},{"name":"Zhao_Yun","health":862,"Att":866,"defense":876},{"name":"Zhang_Fei","health":876,"Att":884,"defense":862},{"name":"Liu_Bei","health":850,"Att":848,"defense":872}]

        warriors = dict()

        home_page=Page()


        for per in shu:
            warriors[per["name"]]= Warriors()
            # vvv<-this uses the setter-I vvv<- this sets it from that instances object
            warriors[per["name"]].Hp = per["health"]
            warriors[per["name"]].Att = per["health"]
            warriors[per["name"]].Def = per["health"]
        print warriors


        if self.request.GET:

            p1 = warriors[str(self.request.GET['p1'])]
            p2 = warriors[str(self.request.GET['p2'])]

            while p1.Hp or p2.Hp >0:
                p1.fight(p2.Att)
                p2.fight(p1.Att)
            if p1.Hp <= 0:
                home_page.update(str(self.request.GET['p1'])+" Won!",shu)
            elif p2.Hp <= 0:
                home_page.update(str(self.request.GET['p1'])+" Won!",shu)
            else:
                home_page.update("DOUBLE SUICIDE!",shu)
        else:
            home_page.update("",shu)
        self.response.write(home_page.print_out())

#warriors is the class that each shu soldier fits in
class Warriors(object):
    def __init__(self):
        self.__health=0
        self.__attack=0
        self.__defense=0

    def fight(self,attack):
        self.health -= attack
        return self.health

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

    @property
    def Def(self):
        self.__defense
        pass

    @Def.setter
    def Def(self,new_def):
        self.__defense=new_def

class Page(object):
    def __init__(self):
        self.option=""
        self.stats=""
        self.result=""
        self.__open='''
<!Doctype html>
<html>
    <head>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">'''
        self.__content="""

        <header class="col-md-6 col-md-offset-4"><h1>An Ancient Battle Lies ahead!</h1></header>
        <section class="col-md-4">
            <select class="char-1 form-control" >
                {self.option}
            </select>
            <ul id="p1-stats">
                {self.stats}
            </ul>
        </section>
        <section class="col-md-4 text-center" >
            <h2 class="col-md-6">Name:health</h2>
            <h2 class="col-md-6">Name:health</h2>
            <form action="/" method="get">
                <input type="hidden" name="p1" id="p1" val="" />
                <input type="hidden" name="p2" id="p2" val="" />
                <button class="btn btn-lg">Fight</button>
            </form>
            <h1>{self.result}</h1>
        </section>
        <section class="col-md-4">
            <select class="char-2 form-control">
                {self.option}
            </select>
            <ul id="p2-stats">
                {self.stats}
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

    def update(self,result,shu):
        self.result = result
        for i in shu:
            self.stats=self.stats+"<li ><h3>"+i["name"]+"</h3>"+"<ul>"+"<li>Health:"+str(i["health"])+"</li>"+"<li>Attack:"+str(i["Att"])+"</li>"+"<li>Defence:"+str(i["defense"])+"</li></ul></li>"
            self.option= self.option+"<option >"+i["name"]+"</option>"
        #**locals() replaces all the {} with the values of the corresponding varaiables
        self.__all=self.__all.format(**locals())
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
