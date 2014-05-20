#!/usr/bin/env python
#Damasio Eli Gerena IV
# day 5 quiz
# may 19 2014
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        fiveseven=Pistol()
        fiveseven.ProjType("bullet")
        print fiveseven.ProjType
        self.response.write('Hello world!')

# I will make a class that shows the relation between guns.

class Gun(object):
    def __init__(self):
        self.name=""
        self._size=""
        self._ammoCount=""
        self.__projectile=""

    def Fire(self,weapon):
        def __init__(self):
            if weapon.ammo >=1:
                self.fire="true"
            else:
                return "Nothing to fire."


    @property
    def ProjType(self):
        def __init__(self):
            return self.__projectile

    @ProjType.setter
    def ProjType(self,newType):
        def __init__(self):
            self.__projectile = newType

class Pistol(Gun):
    def __init__(self):
        Gun.__init__(self)
        self.name="Five-Seven"
        self._size="5.56X7"
        self._ammoCount="30"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
