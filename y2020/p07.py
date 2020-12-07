import collections
import sys


text = sys.stdin.read()
text = text.replace('bags', 'bag')


reverse = collections.defaultdict(list)
bags = collections.defaultdict(list)
for line in text.splitlines():
    source, targets = line.split('contain')
    source = source.strip()
    for target in targets.strip('.').split(','):
        n, stuff = target.strip().split(' ', 1)
        n = int('0' if n == 'no' else n)
        reverse[stuff.strip()].append(source)
        bags[source].append((n, stuff))


edge = {'shiny gold bag'}
seen = set()
while edge:
    edge = {new for old in edge for new in reverse[old]} - seen
    seen |= edge
print(len(seen))


edge = [(1, 'shiny gold bag')]
seen = []
while edge:
    edge = [(n * m, name) for n, sub in edge for m, name in bags[sub] if n * m]
    seen += edge
print(sum(n for n, _ in seen))
