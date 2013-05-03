from datetime import date,datetime,timedelta
from pascha import traditions,computus
from Exceptions import *

class CCalendar:
    """
    Put a date to check and call is_xxx functions to receive a boolean 
    or call get_xxxDay to get the date of this day for the year of the given date.
    """
    __WESTERN__ = "western"
    __EASTERN__ = "eastern"
    
    def __init__(self, mydate, tradition = __WESTERN__):
        """
        mydate - a date of type datatime.date to check
        tradition - a string "western" or "eastern" to check it for catholic or orthodox church
        """
        if type(mydate) != type(date.today()):
            raise BadArgumentException(mydate)
        self.date = mydate
        self.offsets = {}
        if tradition.lower() == 'western':
            self.tradition = self.__WESTERN__
            self.offsets = traditions.Western().offset
        elif tradition.lower() == 'eastern':
            self.tradition = self.__EASTERN__
            self.offsets = traditions.Eastern().offset
        else:
            raise BadTraditionException(tradition)
        self.year = self.date.year
        self.easter_date = 0
        if self.tradition == self.__WESTERN__:
            self.easter_date=computus.western(object,  self.year)
        elif self.tradition == self.__EASTERN__:
            self.easter_date=computus.eastern(object,  self.year)
        self.easter_date = date(self.easter_date.year, self.easter_date.month, self.easter_date.day)
    
    def is_easterDay(self):
        """it is a day of easter?"""
        if self.date == self.easter_date:
            return True
        return False
    
    def get_easterDay(self):
        """returns datetime.date of easter in this year"""
        return self.easter_date
        
    def is_ascensionDay(self):
        """is is a ascension day?"""
        if self.date == self.easter_date+self.offsets['Ascension Day']:
            return True
        return False
    
    def get_ascensionDay(self):
        """returns a datetime.date of ascension day in this year"""
        return self.easter_date+self.offsets['Ascension Day']
    
    def is_ashWednesday(self):
        """it is a ash wednesday?"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Ash Wednesday', self.tradition)
        if self.date == self.easter_date+self.offsets['Ash Wednesday']:
            return True
        return False
    
    def get_ashWednesday(self):
        """returns datetime.date of ash wednesday in this year"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Ash Wednesday', self.tradition)
        return self.easter_date+self.offsets['Ash Wednesday']
    
    def is_palmSunday(self):
        """it is the palm sunday?"""
        if self.date == self.easter_date+self.offsets['Palm Sunday']:
            return True
        return False
        
    def get_palmSunday(self):
        """return datetime.date of the palm sunday in this year"""
        return self.easter_date+self.offsets['Palm Sunday']
    
    def is_goodFriday(self):
        """it is a good friday?"""
        if self.date == self.easter_date+self.offsets['Good Friday']:
            return True
        return False
    
    def get_goodFriday(self):
        """return datetime.date of the good friday in this year"""
        return self.easter_date+self.offsets['Good Friday']
    
    def is_pentecostDay(self):
        """it is a Pentecost day?"""
        if self.date == self.easter_date+self.offsets['Pentecost']:
            return True
        return False
    
    def get_pentecostDay(self):
        """return datetime.date of the Pentecost dayin this year"""
        return self.easter_date+self.offsets['Pentecost']
    
    def is_trinitySunday(self):
        """it is a trinity sunday?"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Trinity Sunday', self.tradition)
        if self.date == self.easter_date+self.offsets['Trinity Sunday']:
            return True
        return False
    
    def get_trinitySunday(self):
        """return datetime.date of the trinity sunday in this year"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Trinity Sunday', self.tradition)
        return self.easter_date+self.offsets['Trinity Sunday']
    
    
    def is_corpusChristi(self):
        """it is a corpus christi day?"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Corpus Christi', self.tradition)
        if self.date == self.easter_date+self.offsets['Corpus Christi']:
            return True
        return False
    
    def get_corpusChristi(self):
        """return datetime.date of the corpus christi in this year"""
        if self.tradition == self.__EASTERN__:
            raise UnknownSolemnityException('Corpus Christi', self.tradition)
        return self.easter_date+self.offsets['Corpus Christi']

import re

class MagicCCalendar:
    def __init__(self,  mydate = '', tradition = CCalendar.__WESTERN__):
        if type(mydate) == type(date.today()):
            self.date = mydate
        else:
            self.date = date.today()
        if tradition in (CCalendar.__WESTERN__,  CCalendar.__EASTERN__):
            self.tradition = tradition
            if self.tradition == CCalendar.__WESTERN__:
                self.traditionObj = traditions.Western()
            if self.tradition == CCalendar.__EASTERN__:
                self.traditionObj = traditions.Eastern()
        else:
            raise BadTraditionException(tradition)
        self.eastern = CCalendar(self.date,  self.tradition).get_easterDay()
        
    def __getattr__(self, name):
        varname = re.sub(r'([A-Z1-9])', ' \g<1>', name)[1:].replace(' Of ',  ' of ').replace(' The ',  ' the ').replace(' And ',  ' and ')
        if varname in self.traditionObj.offset:
            return self.eastern+self.traditionObj.offset[varname]
        else:
            raise UnknownSolemnityException(varname, self.tradition)
        

