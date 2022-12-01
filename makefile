include .env
export

PYTHONPATH := .
FILE := $(shell find . -path "./y????/p??.py" -type f | xargs ls -rt | tail -n 1)
YEAR := $(shell echo ${FILE} | sed 's/[^0-9]/ /g' | cut -d' ' -f4)
DAY := $(shell echo ${FILE} | sed 's/[^0-9]/ /g' | cut -d' ' -f6 | bc)
URL := https://adventofcode.com/${YEAR}/day/${DAY}/input
DATA := $(shell echo ${FILE} | sed s/.py/.dat/)

main:
	@test -f ${DATA} || curl -s -b "session=${SESSION}" ${URL} > ${DATA}
	@cat $(DATA) | python3 -u $(FILE)
