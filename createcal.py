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

NORMAL_DAY = 0
NO_UNI_DAY = 1
HOLIDAY_DAY = 2
DAY_TYPE_NAMES = ["Normal", "NoUni", "Holiday"]

def addFeiertag(month, day, title, t = NORMAL_DAY):
	key = (month, day)
	
	if key not in feiertage:
		feiertage[key] = []
	
	feiertage[key].append({
		"title": title,
		"type": t,
		"tex": "\\calSpecialDay%s{%s}" % (
			DAY_TYPE_NAMES[t],
			title
		)
	})


def getFeiertag(month, day):
	key = (month, day)
	
	if key not in feiertage:
		return {"tex": "", "type": NORMAL_DAY}
	
	l = feiertage[key]
	l.sort(key=lambda x: (not x["type"], x["title"]))
	lTex = map(lambda x: x["tex"], l)
	return {
		"tex": ", ".join(lTex),
		"type": l[0]["type"]
	}


template = Template(fromFile("week.tpl"))

locale.setlocale(locale.LC_ALL, "de_DE.utf8")

start = weekStartFromText(sys.argv[1])
end   = weekStartFromText(sys.argv[2])

# http://de.wikipedia.org/wiki/Feiertage_in_Deutschland
addFeiertag( 1,  1, "Neujahrstag"              , HOLIDAY_DAY) # Fix
addFeiertag( 1,  6, "Heilige Drei Könige"      , HOLIDAY_DAY) # Fix
addFeiertag( 4,  2, "Gründonnerstags"          , NO_UNI_DAY ) # Variabel (Donnerstag vor Ostern)
addFeiertag( 4,  3, "Karfreitag"               , HOLIDAY_DAY) # Variabel (Freitag vor Ostern)
addFeiertag( 4,  4, "Karsamstag"               , NO_UNI_DAY ) # Variabel (Samstag vor Ostern)
addFeiertag( 4,  5, "Ostersonntag"                          ) # Variabel
addFeiertag( 4,  6, "Ostermontag"              , HOLIDAY_DAY) # Variabel (Montag nach Ostersonntag)
addFeiertag( 4,  7, "Osterdienstag"            , NO_UNI_DAY ) # Variabel (Dienstag nach Ostersonntag)
addFeiertag( 5,  1, "Tag der Arbeit"           , HOLIDAY_DAY) # Fix
addFeiertag( 0,  0, "Christi Himmelfahrt"      , HOLIDAY_DAY) # Variabel (39. Tag nach Ostersonntag)
addFeiertag( 0,  0, "Pfingstsonntag"                        ) # Variabel (49. Tag nach Ostersonntag)
addFeiertag( 0,  0, "Pfingstmontag"            , HOLIDAY_DAY) # Variabel (Montag nach Pfingstsonntag)
addFeiertag( 0,  0, "Pfingstdienstag"          , NO_UNI_DAY ) # Variabel (Dienstag nach Pfingstsonntag)
addFeiertag( 0,  0, "Fronleichnam"             , HOLIDAY_DAY) # Variabel (60. Tag nach Ostersonntag)
addFeiertag( 8, 15, "Mariä Himmelfahrt"        , HOLIDAY_DAY) # Fix
addFeiertag(10,  3, "Tag der deutschen Einheit", HOLIDAY_DAY) # Fix
addFeiertag(11,  1, "Allerheiligen"            , HOLIDAY_DAY) # Fix
addFeiertag(11, 29, "1. Advent"                             ) # Variabel
addFeiertag(12,  6, "2. Advent"                             ) # Variabel
addFeiertag(12, 13, "3. Advent"                             ) # Variabel
addFeiertag(12, 20, "4. Advent"                             ) # Variabel
addFeiertag(12, 24, "Heiligabend"                           ) # Fix
addFeiertag(12, 25, "1. Weihnachtsfeiertag"    , HOLIDAY_DAY) # Fix
addFeiertag(12, 26, "2. Weihnachtsfeiertag"    , HOLIDAY_DAY) # Fix

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

def addVorlesungsfrei(start, end, text = "Vorlesungsfreie Zeit"):
	for curDay in rrule.rrule(rrule.DAILY, dtstart=start, until=end):
		addFeiertag(curDay.month,  curDay.day, text, NO_UNI_DAY)





## Vorlesungsfreie Tage nach LMU beschreibung
##  * die gesetzlichen Feiertage
##  * Pfingstdienstag
##  * Gründonnerstag bis einschließlich Osterdienstag
##  * Weihnachtspause vom 24.12. bis 6.1.


addVorlesungsfrei(datetime(2015,  2,  1), datetime(2015,  4, 12)) # Variabel
addVorlesungsfrei(datetime(2014, 12, 24), datetime(2015,  1,  6), "Weihnachtspause") # Fix
addVorlesungsfrei(datetime(2014,  7, 13), datetime(2014, 10,  5)) # Variabel


for curWeek in rrule.rrule(rrule.WEEKLY, dtstart=start, until=end):
	subst = {}
	subst["start_month"] = curWeek.month
	subst["start_year"]  = curWeek.year
	subst["kw"]    = curWeek.isocalendar()[1]
	
	for dayOfWeek in range(7):
		curDay = curWeek + timedelta(days = dayOfWeek)
		feiertag = getFeiertag(curDay.month, curDay.day)
		t = max(dayOfWeek - 4, feiertag["type"])
		subst["wd%i_dayOfMonth" % dayOfWeek] = curDay.day
		subst["wd%i_text" % dayOfWeek] = fromFile(curDay.strftime("days/%m-%d.tex"), "")
		subst["wd%i_feiertage" % dayOfWeek] = feiertag["tex"]
		subst["wd%i_type" % dayOfWeek] = t
	
	subst["end_month"] = curDay.month
	subst["end_year"]  = curDay.year
	
	print(template.substitute(subst))
