## Requirements:
# https://pypi.python.org/pypi/landslide‎
# https://pypi.python.org/pypi/Pygments
# https://github.com/gniezen/n3pygments
# Graphviz

all: presentation.html example.json

%.json: %.trig
	python save_jsonld.py $< $@

%.html: %.md
	landslide  -i -t catalyst -r -d $@ -x codehilite,graphviz,attr_list $<
