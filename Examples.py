from datetime import date

#### Test for standard usage with is_ and get_ ####

import CCalendar as cc

c=cc.CCalendar(date(2013,3,31))
print(c.is_easterDay())
print(c.get_easterDay())
c=cc.CCalendar(date(2013,5,9))
print(c.is_ascensionDay())
print(c.get_ascensionDay())
print(c.get_ashWednesday())

c=cc.CCalendar(date(2013,3,31), cc.CCalendar.__WESTERN__)
print(c.get_corpusChristi())
print(c.get_trinitySunday())
print(c.is_ashWednesday())

c=cc.CCalendar(date(2013,3,31), cc.CCalendar.__EASTERN__)
try:
    print(c.is_corpusChristi())
except cc.UnknownSolemnityException:
    import sys
    e = sys.exc_info()[1]
    print(e)
    del e
try:
    print(c.get_trinitySunday())
except cc.UnknownSolemnityException:
    import sys
    e = sys.exc_info()[1]
    print(e)
    del e
try:
    print(c.is_ashWednesday())
except cc.UnknownSolemnityException:
    import sys
    e = sys.exc_info()[1]
    print(e)
    del e


#### Test for usage of camel case variable names to get dates ####

from CCalendar import MagicCCalendar

print(MagicCCalendar().PalmSunday)
print(MagicCCalendar(date(2008, 4, 11)).PalmSunday)
print(MagicCCalendar(date(2009, 4, 11)).Pentecost)
print(MagicCCalendar(date(2010, 4, 11)).TheOctaveOfEaster)
try:
    print(MagicCCalendar(date(2008, 4, 11)).GreatAndHolySaturday)
except cc.UnknownSolemnityException:
    import sys
    e = sys.exc_info()[1]
    print(e)
    del e
try:
    print(MagicCCalendar(date(2008, 4, 11),  cc.CCalendar.__EASTERN__).CorpusChristi)
except cc.UnknownSolemnityException:
    import sys
    e = sys.exc_info()[1]
    print(e)
    del e
print(MagicCCalendar(date(2006, 4, 11),  cc.CCalendar.__EASTERN__).ThePublicanAndThePharisee)
print(MagicCCalendar(date(2006, 4, 11),  cc.CCalendar.__EASTERN__).MemorialSaturday3)
print(MagicCCalendar(date(2006, 4, 11),  cc.CCalendar.__EASTERN__).TheBlindMan)
