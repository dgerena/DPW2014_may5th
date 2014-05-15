#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
# Damasio Eli Gerena IV
#
#
import webapp2
'''
HORSE:
Kingdom - Animalia
Phylum - Chordata
Class - Mammalia
Order - Perissodactyla
Family - Equidae
Genus - Equus
Species - caballus

COW:
Kingdom - Animalia
Phylum - Chordata
Class - Mammalia
Order - Artiodactyla
Family - Bovidae
Genus - Bos
Species - taurus

PIG:
Kingdom - Animalia
Phylum - Chordata
Class - Mammalia
Order - Artiodactyla
Family - Suidae
Genus - Sus
Species - domestica
'''
class MainHandler(webapp2.RequestHandler):
    def get(self):


class Animalia(object):
    def __init__(self):
        kingdom ='Animalia'
        phylum='Chordata'
        sci_class='Mammalia'

class Chordata(Animalia):
    def __init__(self):
        phylum="Chordata"

class Mammalia(Chordata):
    def __init__(self):
        sci_class="Mammalia"

class Artiodactyla(Mammalia):
    def __init__(self):
        order = "Artiodactyla"

class Perissodactyla(Mammalia):
    def __init__(self):
        order = "Perissodactyla"

class Suidae(Artiodactyla):
    def __init__(self):
        family='Suidae'

class Equidae(Perissodactyla):
    def __init__(self):
        family="Equidae"
#genus
class Sus(Suidae):
    def __init__(self):
        genus='Sus'

class Equus(Equidae):
    def __init__(self):
        genus="Equus"
#species
class Domestica(Sus):
    def __init__(self):
        species="Domestica"

class Caballus(Equus):
    def __init__(self):
        species="Caballus"

        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
