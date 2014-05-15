#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
# Damasio Eli Gerena IV
#
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

#Kingdom
class Animalia(object):
    def __init__(self):
        self._kingdom ='Animalia'
        self._multicelular="Many celled organism."
        self._heterotrophs="Consumes of something else."
        self.all=self._kingdom+self._multicelular+self._heterotrophs
#Phylum
class Chordata(Animalia):
    def __init__(self):
        Animalia.__init__(self)
        self._phylum="Chordata"
        self._spine="Has a spinal cord at some time during life."
        self._pharynx="Has a throat."
        self._sound="Air moving!"
        self.all=self.all+self._phylum+self._spine+self._pharynx+self._sound
#Class
class Mammalia(Chordata):
    def __init__(self):
        Chordata.__init__(self)
        self._sci_class="Mammalia"
        self._hair="Has hair."
        self._earBones="Has 3 middle ear bones."
        self._mammary="Has mammaries to nourish young."
        self._sound="Momma I'm hungry!"
        self.all=self.all+self._sci_class+self._hair+self._hair+self._earBones+self._mammary+self._sound
#Order
class Artiodactyla(Mammalia):
    def __init__(self):
        Mammalia.__init__(self)
        self._order = "Artiodactyla"
        self._evenToed="Even numbered hooved toes."
        self._sound="Neigh!"
        self.all=self.all+self._order+self._evenToed+self._sound

class Perissodactyla(Mammalia):
    def __init__(self):
        Mammalia.__init__(self)
        self._order = "Perissodactyla"
        self._oddToed="Odd number of hooved toes."
        self._sound="Neigh!"
        self.all=self.all+self._order+self._oddToed+self._sound
#Family
class Suidae(Artiodactyla):
    def __init__(self):
        Artiodactyla.__init__(self)
        self._family='Suidae'
        self._pig="Is a pig."
        self._sound="Squeee!"
        self.all=self.all+self._family+self._pig+self._sound

class Equidae(Perissodactyla):
    def __init__(self):
        Perissodactyla.__init__(self)
        self._family="Equidae"
        self._horseIsh="Horse like build."
        self._sound="Neigh!"
        self.all=self.all+self._family+self._horseIsh+self._sound

class Bovidae(Artiodactyla):
    def __init__(self):
        Artiodactyla.__init__(self)
        self._family="Bovidae"
        self._bovid="Horned animal."
        self._sound="pffff"
        self.all=self.all+self._family+self._bovid+self._sound
#Genus
class Sus(Suidae):
    def __init__(self):
        Suidae.__init__(self)
        self._genus='Sus'
        self._isPig="Is of the pig family."
        self.all=self.all+self._genus+self._isPig

class Equus(Equidae):
    def __init__(self):
        Equidae.__init__(self)
        self._genus="Equus"
        self._isHorse="Is of the horse family."
        self.all=self.all+self._genus+self._isHorse


class Bos(Bovidae):
    def __init__(self):
        Bovidae.__init__(self)
        self._Genus= "Bos"
        self._bovine="Of cattle and bull family."
        self.all=self.all+self._Genus+self._bovine
#Species
class Domestica(Sus):
    def __init__(self):
        Sus.__init__(self)
        self._species="Domestica"
        self._pig="Is a common domestic pig or swine."
        self.all=self.all+self._species+self._pig

class Caballus(Equus):
    def __init__(self):
        Caballus.__init__(self)
        self._species="Caballus"
        self._horse="Domestic common horse."
        self.all=self.all+self._species+self._horse

class Taurus(Bos):
    def __init__(self):
        Taurus.__init__(self)
        self._species="Taurus"
        self._cattle="Domestic cattle."
        self._sound="Moo!"
        self.all=self.all+self._species+self._cattle+self._sound

        self.response.write(Taurus(mike).all)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
