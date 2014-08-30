DAY_FILES   := $(wildcard days/*.tex)

all: EE2013.pdf


kalender-days.tex: createcal.py week.tpl $(DAY_FILES)
	./createcal.py 2014-09-30 2015-04-13 >kalender-days.tex


EE2013.pdf: kalender-days.tex
	xelatex EE2013.tex
	xelatex EE2013.tex
