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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
