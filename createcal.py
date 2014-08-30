#!/usr/bin/python3

from dateutil import rrule
from datetime import datetime, timedelta
import dateutil.parser
import sys
import locale
import os.path
from string import Template


def weekStartFromText(text):
	dt = datetime.strptime(text, "%Y-%m-%d")
	return dt - timedelta(days = dt.weekday())

def fromFile(path, default = None):
	if not os.path.isfile(path):
		return default
	
	with open(path, "r") as f:
		return f.read()

feiertage = {}

def addFeiertag(month, day, title, noUni = False):
	key = (month, day)
	
	if key not in feiertage:
		feiertage[key] = []
	
	feiertage[key].append({
		"title": title,
		"no_uni": noUni
	})



def getFeiertag(month, day):
	key = (month, day)
	
	if key not in feiertage:
		return ""
	
	l = feiertage[key]
	l.sort(key=lambda x: (not x["no_uni"], x["title"]))
	l = map((lambda x: ("\\textbf{%s}" % x["title"]) if x["no_uni"] else x["title"]), l)
	return "[%s]" % ", ".join(l)


template = Template(fromFile("week.tpl"))

locale.setlocale(locale.LC_ALL, "de_DE.utf8")

start = weekStartFromText(sys.argv[1])
end   = weekStartFromText(sys.argv[2])

# http://de.wikipedia.org/wiki/Feiertage_in_Deutschland
addFeiertag( 1,  1, "Neujahrstag"              , True) # Fix
addFeiertag( 1,  6, "Heilige Drei Könige"      , True) # Fix
addFeiertag( 4,  3, "Karfreitag"               , True) # Variabel (Freitag vor Ostern)
addFeiertag( 4,  5, "Ostersonntag"                   ) # Variabel
addFeiertag( 4,  6, "Ostermontag"              , True) # Variabel (Montag nach Ostersonntag)
addFeiertag( 5,  1, "Tag der Arbeit"           , True) # Fix
addFeiertag( 0,  0, "Christi Himmelfahrt"      , True) # Variabel (39. Tag nach Ostersonntag)
addFeiertag( 0,  0, "Pfingstsonntag"                 ) # Variabel (49. Tag nach Ostersonntag)
addFeiertag( 0,  0, "Pfingstmontag"            , True) # Variabel (Montag nach Pfingstsonntag)
addFeiertag( 0,  0, "Fronleichnam"             , True) # Variabel (60. Tag nach Ostersonntag)
addFeiertag( 8, 15, "Mariä Himmelfahrt"        , True) # Fix
addFeiertag(10,  3, "Tag der deutschen Einheit", True) # Fix
addFeiertag(11,  1, "Allerheiligen"            , True) # Fix
addFeiertag(12, 24, "Heiligabend"                    ) # Fix
addFeiertag(12, 25, "1. Weihnachtsfeiertag"    , True) # Fix
addFeiertag(12, 26, "2. Weihnachtsfeiertag"    , True) # Fix

# http://de.wikipedia.org/wiki/Diskordianischer_Kalender
addFeiertag( 1,  5, "Mungtag"                        ) # Fix
addFeiertag( 2, 19, "Chaoflux"                       ) # Fix
addFeiertag( 2, 29, "St. Tib’s Day"                  ) # Fix
addFeiertag( 3, 19, "Mojotag"                        ) # Fix
addFeiertag( 5,  3, "Discoflux"                      ) # Fix
addFeiertag( 5, 31, "Syatag"                         ) # Fix
addFeiertag( 7, 15, "Confuflux"                      ) # Fix
addFeiertag( 8, 12, "Zaratag"                        ) # Fix
addFeiertag( 9, 26, "Bureflux"                       ) # Fix
addFeiertag(10, 24, "Malatag"                        ) # Fix
addFeiertag(12,  8, "Afflux"                         ) # Fix



for curWeek in rrule.rrule(rrule.WEEKLY, dtstart=start, until=end):
	subst = {}
	subst["start_month"] = curWeek.month
	subst["start_year"]  = curWeek.year
	subst["kw"]    = curWeek.isocalendar()[1]
	
	for dayOfWeek in range(7):
		curDay = curWeek + timedelta(days = dayOfWeek)
		subst["wd%i_dayOfMonth" % dayOfWeek] = curDay.day
		subst["wd%i_text" % dayOfWeek] = fromFile(curDay.strftime("days/%m-%d.tex"), "")
		subst["wd%i_feiertage" % dayOfWeek] = getFeiertag(curDay.month, curDay.day)
		
	
	subst["end_month"] = curDay.month
	subst["end_year"]  = curDay.year
	
	print(template.substitute(subst))
