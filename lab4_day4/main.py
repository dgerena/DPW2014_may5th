#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Damasio Eli GErena
# may 12th 2014
#
import webapp2
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
        self.response.write('Hello world!')
        shu=["Guan_Yu","Zhao_Yun","Zhang_Fei","Liu_Bei"]
        Guan_Yu.health=872
        Guan_Yu.attack=880
        Guan_yu.defense=872

        Zhao_Yun.health=862
        Zhao_Yun.attack=866
        Zhao_Yun.defense=876

        Zhang_Fei.health=876
        Zhang_Fei.attack=884
        Zhang_Fei.defense=862

        Liu_Bei.health=850
        Liu_Bei.attack=848
        Liu_Bei.defense=872


class Warriors(object):#warriors is the class that each shu soldier fits in
    def __init__(self):
        self.health=0
        self.attack=0
        self.defense=0






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
