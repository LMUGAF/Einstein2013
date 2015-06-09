DAY_FILES   := $(wildcard days/*.tex)


## Target if make is invoked without any parameter (goal)
.DEFAULT_GOAL: all

## "Virtual" targets without actual files to update/create
.PHONY: all clean distclean new


all: main.pdf


FORCE:
	@true


tmp/kalender-days.tex: createcal.py week.tpl $(DAY_FILES)
	mkdir -p tmp
	./createcal.py 2014-09-30 2015-04-13 >tmp/kalender-days.tex


.ONESHELL:
tmp/main.pdf: tmp/kalender-days.tex FORCE
	@export max_print_line=1000
	export error_line=254
	export half_error_line=238
	
	if ! latexmk ; then
		grep  -H -C 10 --color=always -n -E '^(\./|\!).*' tmp/main.log | \
		python  -c 'import sys;print(sys.stdin.read().replace(sys.argv[1], sys.argv[2]))' tmp/main.log "" | \
		python  -c 'import sys;print(sys.stdin.read().replace(sys.argv[1], sys.argv[2]))' $$'\033[K./' "$$PWD/"
		
		rm -f "tmp/main.pdf"
		false
	fi


main.pdf: tmp/main.pdf
	ln --force $^ $@


clean:
	@rm --force --verbose --recursive tmp


distclean: clean
	@rm --force --verbose main.pdf


new: distclean all
