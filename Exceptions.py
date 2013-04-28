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
    