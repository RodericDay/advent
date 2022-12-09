include .env
export

.SILENT:

CODE := $(shell find . -path "./y????/p??.*" -type f | xargs ls -rt | tail -n 1)
YEAR := $(shell echo ${CODE} | sed 's/[^0-9]/ /g' | cut -d' ' -f4)
DAY0 := $(shell echo ${CODE} | sed 's/[^0-9]/ /g' | cut -d' ' -f6)
DATA := ./y${YEAR}/p${DAY0}.dat
URL := https://adventofcode.com/${YEAR}/day/`echo ${DAY0} | bc`/input

pyrun: ${DATA}
	cat ${DATA} | docker run -v `pwd`:/app/ -w /app/ -i --rm python:latest python -u ./y${YEAR}/p${DAY0}.py

${DATA}:
	# avoid spam in the lead up to the event
	test ${YEAR}${DAY0} -le `date +%Y%d`
	# only poll if data isn't yet stored locally
	test -f ${DATA} || curl -s -b "session=${SESSION}" ${URL} > ${DATA}
