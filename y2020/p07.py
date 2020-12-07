import collections
import re
import sys


text = sys.stdin.read()
rev = collections.defaultdict(list)
fwd = collections.defaultdict(list)
for line in text.splitlines():
    (_, src), *targets = re.findall(r'(\d*) ?(\w+ \w+) bag', line)
    for n, tgt in targets:
        rev[tgt].append(src)
        fwd[src].append((tgt, int(n or '0')))


edge = {'shiny gold'}
seen = set()
while edge:
    edge = {new for old in edge for new in rev[old]} - seen
    seen |= edge
print(len(seen))


edge = [('shiny gold', 1)]
seen = []
while edge:
    edge = [(new, n * m) for old, n in edge for new, m in fwd[old] if n * m]
    seen += edge
print(sum(n for _, n in seen))
