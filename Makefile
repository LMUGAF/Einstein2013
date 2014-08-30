DAY_FILES   := $(wildcard days/*.tex)


## Target if make is invoked without any parameter (goal)
.DEFAULT_GOAL: all

## "Virtual" targets without actual files to update/create
.PHONY: all EE2013 clean distclean new


all: EE2013


kalender-days.tex: createcal.py week.tpl $(DAY_FILES)
	./createcal.py 2014-09-30 2015-04-13 >kalender-days.tex


EE2013: kalender-days.tex
	@tput rev ; tput bold ; echo " Making $@ " ; tput sgr0
	@exec 3>&1 ; \
	latexmk 2>&1 >&3 | \
	sed -l -e "s#\(.*\)#`tput bold`\1`tput sgr0`#"
	@echo -e "\a"
	@ln --force tmp/main.pdf $@.pdf

clean:
	@rm --force --verbose --recursive tmp

distclean: clean
	@rm --force --verbose EE2013.pdf

new: distclean all