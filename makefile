include .env
FILE = $(shell find . -path "./y????/p??.py" -type f | xargs ls -rt | tail -n 1)
DATA = $(shell echo $(FILE) | sed s/.py/.dat/)
PYTHONPATH = .
export

main: venv/
	@venv/bin/python -u toolkit.py $(FILE)
	@cat $(DATA) | venv/bin/python -u $(FILE)

flake: venv/
	venv/bin/flake8 --exclude=venv/

venv/: requirements.txt
	rm -rf venv/
	~/.pyenv/versions/3.8.0/bin/python -m venv venv
	venv/bin/pip install -r requirements.txt
	touch requirements.txt venv/
	# install flake8 git hook
	# echo 'venv/bin/flake8 --exclude=venv/' > .git/hooks/pre-commit
	# chmod +x .git/hooks/pre-commit
