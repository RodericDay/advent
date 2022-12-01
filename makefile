include .env
export

.SILENT:

CODE := $(shell find . -path "./y????/p??.py" -type f | xargs ls -rt | tail -n 1)
DATA := $(shell echo ${CODE} | sed s/.py/.dat/)
YEAR := $(shell echo ${CODE} | sed 's/[^0-9]/ /g' | cut -d' ' -f4)
DAY := $(shell echo ${CODE} | sed 's/[^0-9]/ /g' | cut -d' ' -f6)
URL := https://adventofcode.com/${YEAR}/day/`echo ${DAY} | bc`/input

pyrun: ${DATA}
	PYTHONPATH=. python3 -u ${CODE} < ${DATA}

${DATA}:
	# avoid spam in the lead up to the event
	test ${YEAR}${DAY} -le `date +%Y%d`
	# only poll if data isn't yet stored locally
	test -f ${DATA} || curl -s -b "session=${SESSION}" ${URL} > ${DATA}
