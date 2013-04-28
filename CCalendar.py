from datetime import date,datetime,timedelta
from pascha import traditions,computus
from Exceptions import *

class CCalendar():
    """
    Put a date to check
    """
    __WESTERN__ = 1
    __EASTERN__ = 2
    
    def __init__(self, mydate, tradition = 'western'):
        if type(mydate) != type(date(2013,04,28)):
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
        year = self.date.year
        self.easter_date = 0
        if self.tradition == self.__WESTERN__:
            self.easter_date=computus.western(year)
        elif self.tradition == self.__EASTERN__:
            self.easter_date=computus.eastern(year)
        self.easter_date = date(self.easter_date.year, self.easter_date.month, self.easter_date.day)
    
    def is_easterDay(self):
        if self.date == self.easter_date:
            return True
        return False
    
    def get_easterDay(self):
        return self.easter_date
        
    def is_ascensionDay(self):
        if self.date == self.easter_date+self.offsets['Ascension Day']:
            return True
        return False
    
    def get_ascensionDay(self):
        return self.easter_date+self.offsets['Ascension Day']
    
    def is_ashWednesday(self):
        if self.date == self.easter_date+self.offsets['Ash Wednesday']:
            return True
        return False
    
    def get_ashWednesday(self):
        return self.easter_date+self.offsets['Ash Wednesday']
        

