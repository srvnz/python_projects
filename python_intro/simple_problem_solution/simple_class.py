#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:37:01 2021

@author: mr.hsp
"""
# =============================================================================
# Classes are great to encapsulate functionality, that can be kept together and passed around as a complete module for use in another project.
# =============================================================================


class myClass():
    # Object-oriented terminology. Usually the first argument is a 'self'.
    # This argument refers to the object itself.
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


class anotherClass():
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        myClass.method2(self, someString)
        print("anotherClass method2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is another string")


main()
