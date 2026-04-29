#!/usr/bin/python3
"""
this is global enviroment
"""


class SwimMixin():

    def swim(self):
        print("The creature swims!")


class FlyMixin():

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        print("The dragon roars!")
