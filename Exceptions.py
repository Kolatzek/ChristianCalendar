#!/usr/bin/env python

###############################
## Author Robert Kolatzek
## Exceptions.py license: 
## The MIT License (MIT)
## http://opensource.org/licenses/mit-license.php
###############################

# vim: tabstop=4 expandtab shiftwidth=4

class BadTraditionException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return 'Bad tradition value given. Possible are "eastern" and "western". But '+repr(self.value)+' given.'
    
class BadArgumentException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return 'A given date argument is not of type '+type(date(2013,04,28))
    
class UnknownSolemnityException(Exception):
    def __init__(self,solemnity, tradition):
        self.solemnity = solemnity
        self.tradition = tradition
    def __str__(self):
        return 'The solemnity '+self.solemnity+' is unknown in '+self.tradition+' tradition.'
