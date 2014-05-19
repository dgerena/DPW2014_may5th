#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
# Damasio Eli Gerena IV
#
# Phylum
# Class
# Order
# Family
# Genus
# URL for the image of the animal
# Average Lifespan
# Habitat
# Geolocation
#

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        whiteCastle=Horse()
        whiteCastle._geolocation="North Eastern USA."
        whiteCastle._sound="Gurgle Gurgle"

        bacon=Pig()
        bacon._geolocation="My belly."
        bacon._sound="NomNomNom"

        steak = Cow()
        steak._geolocation="My Fridge."
        steak._sound = 'Sizzle sizzle.'

        food=[whiteCastle,bacon,steak]
        for i in food:
            self.response.write(i._sound)
            # self.response.write(i)

        main_page=Page()


        #will get instantiated animals and place into pen, returning a array.




#animal stuff--------
class Animal(object):
    def __init__(self):
        self._phylum=""
        self._sci_class=""
        self._order=""
        self._family=""
        self._genus=""
        self._image=""
        self._lifespan=0
        self._habitat=""
        self._geolocation="My Kitchen"
        self._sound="Air!"

    #----- Hey Rebecca is this a way to do this also? K thanks bye.
    @property
    def sound(self):
        print self.sound

    @sound.setter
    def sound(self,value):
        self._sound = value

class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._phylum="Chordata"
        self._sci_class="Mammalia"
        self._order="Perissodactyla"
        self._family="Equidae"
        self._genus="Equus"
        self._lifespan=0
        self._habitat=""
        self._geolocation="Earth"

class Pig(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._phylum="Chordata"
        self._sci_class="Mammalia"
        self._order="Artiodactyla"
        self._family="Suidae"
        self._genus="Sus"
        self._lifespan=0
        self._habitat=""
        self._geolocation="Earth"

class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._phylum="Chordata"
        self._sci_class="Mammalia"
        self._order="Artiodactyla"
        self._family="Bovidae"
        self._genus="Bos"
        self._lifespan=0
        self._habitat=""
        self._geolocation="Earth"

#page script----

class Page(object):
    def __init__(self):
        self._logo="Logo tbd"
        self._nav="Nav items"
        self._name="Name with desired properties"
        self._stats="Properties"
        self._result=""
        self._title="Unset"

        self.__open='''
<!Doctype html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">'''

        self.__content="""
        <header class="col-md-12">
            <h1>{self._logo}</h1>
            <nav>
                <li>{self._nav}</li>
            </nav>
        </header>
        <section class="col-md-4">
            <ul>
                <li>{self._name}</li>
            </ul>
        </section>
        <div class="main-content">
            <h3>{self._name}</h1>
            <p>{self._stats}</p>
        </div>
        <footer></footer>
        """

        self.__close='''
        <script type="text/javascript" src="js/jquery-1.11.0.min.js"></script>
        <script type="text/javascript" src="js/main.js"></script>
    </body>
</html>
        '''
        self.__all=self.__open+self.__content+self.__close

    def print_out(self):

        return self.__all

    def update(self,result,):
        self.result = result
        for i in self.anim_house:
            self.stats=self.stats+"<li ><h3>"+i["name"]+"</h3>"+"<ul>"+"<li>Health:"+str(i["health"])+"</li>"+"<li>Attack:"+str(i["Att"])+"</li>"+"<li>Defence:"+str(i["defense"])+"</li></ul></li>"
            self.option= self.option+"<option >"+i["name"]+"</option>"
        #**locals() replaces all the {} with the values of the corresponding varaiables
        self.__all=self.__all.format(**locals())

#               #   #First Attempt # ALL WRONG
# #Kingdom
# class Animalia(object):
#     def __init__(self):
#         self._kingdom ='Animalia'
#         self._multicelular="Many celled organism."
#         self._heterotrophs="Consumes of something else."
#         self.all=self._kingdom+self._multicelular+self._heterotrophs
#     def print_out(self):
#         return self.all
# #Phylum
# class Chordata(Animalia):
#     def __init__(self):
#         Animalia.__init__(self)
#         self._phylum="Chordata"
#         self._spine="Has a spinal cord at some time during life."
#         self._pharynx="Has a throat."
#         self._sound="Air moving!"
#         self.all=self.all+self._phylum+self._spine+self._pharynx+self._sound
# #Class
# class Mammalia(Chordata):
#     def __init__(self):
#         Chordata.__init__(self)
#         self._sci_class="Mammalia"
#         self._hair="Has hair."
#         self._earBones="Has 3 middle ear bones."
#         self._mammary="Has mammaries to nourish young."
#         self._sound="Momma I'm hungry!"
#         self.all=self.all+self._sci_class+self._hair+self._hair+self._earBones+self._mammary+self._sound
# #Order
# class Artiodactyla(Mammalia):
#     def __init__(self):
#         Mammalia.__init__(self)
#         self._order = "Artiodactyla"
#         self._evenToed="Even numbered hooved toes."
#         self._sound="Neigh!"
#         self.all=self.all+self._order+self._evenToed+self._sound
#
# class Perissodactyla(Mammalia):
#     def __init__(self):
#         Mammalia.__init__(self)
#         self._order = "Perissodactyla"
#         self._oddToed="Odd number of hooved toes."
#         self._sound="Neigh!"
#         self.all=self.all+self._order+self._oddToed+self._sound
# #Family
# class Suidae(Artiodactyla):
#     def __init__(self):
#         Artiodactyla.__init__(self)
#         self._family='Suidae'
#         self._pig="Is a pig."
#         self._sound="Squeee!"
#         self.all=self.all+self._family+self._pig+self._sound
#
# class Equidae(Perissodactyla):
#     def __init__(self):
#         Perissodactyla.__init__(self)
#         self._family="Equidae"
#         self._horseIsh="Horse like build."
#         self._sound="Neigh!"
#         self.all=self.all+self._family+self._horseIsh+self._sound
#
# class Bovidae(Artiodactyla):
#     def __init__(self):
#         Artiodactyla.__init__(self)
#         self._family="Bovidae"
#         self._bovid="Horned animal."
#         self._sound="pffff"
#         self.all=self.all+self._family+self._bovid+self._sound
# #Genus
# class Sus(Suidae):
#     def __init__(self):
#         Suidae.__init__(self)
#         self._genus='Sus'
#         self._isPig="Is of the pig family."
#         self.all=self.all+self._genus+self._isPig
#
# class Equus(Equidae):
#     def __init__(self):
#         Equidae.__init__(self)
#         self._genus="Equus"
#         self._isHorse="Is of the horse family."
#         self.all=self.all+self._genus+self._isHorse
#
#
# class Bos(Bovidae):
#     def __init__(self):
#         Bovidae.__init__(self)
#         self._Genus= "Bos"
#         self._bovine="Of cattle and bull family."
#         self.all=self.all+self._Genus+self._bovine
# #Species
# class Domestica(Sus):
#     def __init__(self):
#         Sus.__init__(self)
#         self._species="Domestica"
#         self._pig="Is a common domestic pig or swine."
#         self.all=self.all+self._species+self._pig
#
# class Caballus(Equus):
#     def __init__(self):
#         Caballus.__init__(self)
#         self._species="Caballus"
#         self._horse="Domestic common horse."
#         self.all=self.all+self._species+self._horse
#
# class Taurus(Bos):
#     def __init__(self):
#         Taurus.__init__(self)
#         self._species="Taurus"
#         self._cattle="Domestic cattle."
#         self._sound="Moo!"
#         self.all=self.all+self._species+self._cattle+self._sound
#
#
# # self.response.write(Taurus(mike).all)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)