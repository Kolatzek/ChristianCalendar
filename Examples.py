from datetime import date
import CCalendar as cc

c=cc.CCalendar(date(2013,03,31))
print c.is_easterDay()
print c.get_easterDay()
c=cc.CCalendar(date(2013,5,9))
print c.is_ascensionDay()
print c.get_ascensionDay()
print c.get_ashWednesday()

c=cc.CCalendar(date(2013,03,31), cc.CCalendar.__WESTERN__)
print c.get_corpusChristi()
print c.get_trinitySunday()
print c.is_ashWednesday()

c=cc.CCalendar(date(2013,03,31), cc.CCalendar.__EASTERN__)
try:
    print c.is_corpusChristi()
except cc.UnknownSolemnityException, e:
    print e
try:
    print c.get_trinitySunday()
except cc.UnknownSolemnityException, e:
    print e
try:
    print c.is_ashWednesday()
except cc.UnknownSolemnityException, e:
    print e
