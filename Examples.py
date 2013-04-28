from datetime import date
import CCalendar as cc

c=cc.CCalendar(date(2013,03,31))
print c.is_easterDay()
print c.get_easterDay()
c=cc.CCalendar(date(2013,5,9))
print c.is_ascensionDay()
print c.get_ascensionDay()
print c.get_ashWednesday()
