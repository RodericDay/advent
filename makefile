include .env
export

.SILENT:

FILE := $(shell find . -path "./y????/p??.*" -type f | xargs ls -rt | tail -n 1)

YEAR := $(shell echo ${FILE} | sed -E 's/.+y([0-9]+).+/\1/')
DAY := $(shell echo ${FILE} | sed -E 's/.+p([0-9]+).+/\1/' | bc)
URL := https://adventofcode.com/${YEAR}/day/${DAY}

BASE := $(shell echo ${FILE} | sed -E 's/\....?$$//')
CODE := $(BASE).py
DATA := $(BASE).dat
TEST := $(BASE).dtt


main: ${TEST}
	echo 'test':
	cat ${TEST} | docker compose run --rm advent python -u ${CODE}

clean: ${DATA}
	echo 'real:'
	cat ${DATA} | docker compose run --rm advent python -u ${CODE}

save:
	git add .
	test `git log -1 --format=%s` == `cat VERSION` \
		&& git commit --amend --reuse-message=head \
		|| git commit -m `cat VERSION`

${DATA} ${TEST}:
	# avoid spam in the lead up to the event
	test ${DAY} -le `date +%d` || test ${YEAR} -lt `date +%Y`
	# only poll if data isn't yet stored locally
	test -f ${DATA} || curl -s -b "session=${SESSION}" ${URL}/input > ${DATA}
	# try to get test data
	test -f ${TEST} || curl -s ${URL} | tr '\n' '@' | perl -pe 's|.+?<pre><code>(.+?)</code></pre>.+|\1|' | tr '@' '\n' > ${TEST}
