FILE = $(shell find . -name p??.py -type f | xargs ls -rt | tail -n 1)
DATA = $(shell echo $(FILE) | sed -e s/\.py/\.dat/)
PYTHONPATH=.

main: venv/
	@touch $(DATA)
	@cat $(DATA) | venv/bin/python -u $(FILE)

venv/: requirements.txt
	rm -rf venv/
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	touch requirements.txt venv/
