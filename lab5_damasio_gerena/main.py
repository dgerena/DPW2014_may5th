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
        main_page=Page()

        whiteCastle=Horse()
        whiteCastle._name="White Castle Burger"
        whiteCastle._geolocation="North Eastern USA."
        whiteCastle.sound="Gurgle Gurgle (As heard from stomach.)"
        whiteCastle._image="http://assets3.whitecastle.com/system/pages/photos/2/large/food.jpg?1255036013"
        whiteCastle._habitat="White Castle Fast food restaurants."
        whiteCastle._lifespan="5 min. from purchase."
        whiteCastle._wasA="Horse"

        bacon=Pig()
        bacon._name="Bacon"
        bacon._geolocation="My belly."
        bacon.sound="NomNomNom"
        bacon._image="http://cdn2-b.examiner.com/sites/default/files/styles/image_content_width/hash/dd/49/dd496638625503072eac92a428654527.jpg?itok=rpImMEqz"
        bacon._lifespan="7 days unrefrigerated. 2 days in my kitchen."
        bacon._wasA="Pig"

        steak = Cow()
        steak._name="Steak"
        steak._geolocation="My Fridge."
        steak.sound = 'Sizzle sizzle.'
        steak._image="https://c2.staticflickr.com/4/3033/2589279995_f29574b45e_z.jpg"
        steak._lifespan="7 days unrefrigerated. 2 days in my kitchen."
        steak._wasA="Cow"

        food=[whiteCastle,bacon,steak]
        if self.request.GET:
            Animal = self.request.GET['Animal']
            for i in food:
                if i._genus == Animal:
                    print i
                    self.response.write(main_page.print_out(food,i))
        else:
            self.response.write(main_page.print_out(food,""))


        #will get instantiated animals and place into pen, returning a array.




#animal stuff--------
class Animal(object):
    def __init__(self):
        self._phylum="Chordata"
        self._sci_class="Mammalia"
        self._order=""
        self._family=""
        self._genus=""
        self._image=""
        self._lifespan=0
        self._habitat="Your local Grocer."
        self._geolocation="My Kitchen"
        self._name=""
        self._sound="Air!"

    #----- Hey Rebecca is this a way to do this also? K thanks bye.
    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self,value):
        self._sound = value

class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._order="Perissodactyla"
        self._family="Equidae"
        self._genus="Equus"
        self._lifespan=25
        self._habitat=""
        self._geolocation="Earth"

class Pig(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._order="Artiodactyla"
        self._family="Suidae"
        self._genus="Sus"
        self._lifespan=8
        self._habitat=""
        self._geolocation="Earth"

class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)
        self._order="Artiodactyla"
        self._family="Bovidae"
        self._genus="Bos"
        self._lifespan=15
        self._habitat=""
        self._geolocation="Earth"

#page script----

class Page(object):
    def __init__(self):
        self._logo="Consumption Junction"
        self._nav=""
        self._name=""
        self._stats=""
        self._result=""
        self._title="ALL THE FOODS!"

        self.__open='''
<!Doctype html>
<html>
    <head>
        <title>{self._title}</title>
        <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body class=" col-md-12">'''

        self.__content="""
        <header class="col-md-8 col-md-offset-2">
            <h1 class="col-md-4">{self._logo}</h1>
            <nav class="col-md-8">
                {self._nav}
            </nav>
        </header>
        <div class="main-content col-md-8 col-md-offset-2">
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

    def print_out(self,food,result):
        for i in food:
            self._nav = self._nav +"<li class='col-md-3'>"+"<a href='/?Animal="+i._genus+"'+>"+str(i._genus)+"</a>"+"</li>"
        if result != "":
            self.update(result)
        self.__all=self.__all.format(**locals())
        return self.__all

    def update(self,result):# changes the page based on where you are.
        self.result = result

        self._stats= self._stats+"<li>Phylum: "+result._phylum+"</li>"+\
                     "<li>Class: "+result._sci_class+"</li>"+\
                     "<li>Order: "+result._order+"</li>"+\
                     "<li>Family: "+result._family+"</li>"+"<li>Genus: "+\
                     result._genus+"</li>"+"<li>"+"<a href='"+result._image+"'><img class='imgMove' src='"+result._image+"'/></a>"+"</li>"+"<li>Lifespan: "+str(result._lifespan)+"</li>"+\
                     "<li>Habitat: "+result._habitat+"</li>"+\
                     "<li>Geolocation: "+result._geolocation+"</li>"+"<li>Originated from a "+result._wasA+".</li>"+"<li>Sound: "+result._sound+"</li>"
        #**locals() replaces all the {} with the values of the corresponding varaiables


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