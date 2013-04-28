ChristianCalendar
=================

christian calendar calculation for python

A module to check christian hollydays or get a date of it in same year as given date.

    from ChristianCalendar.CCalendar import CCalendar
    c=CCalendar(date(2013,3,31))
    if c.is_easterDay():
        print 'Christ is Risen!'
    print c.get_ascensionDay()

Requires module pascha from PIP. Install it with 
    
    easy_install pascha
