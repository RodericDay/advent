import collections
import itertools
import re
import sys

import toolkit


Node = collections.namedtuple('Node', 'x, y, size, used, avail, pc')
nodes = []
text = sys.stdin.read()
for line in text.splitlines():
    found = list(map(int, re.findall(r'\d+', line)))
    if found:
        nodes.append(Node(*found))

ans1 = 0
for a, b in itertools.permutations(nodes, 2):
    if a.used and a.used <= b.avail:
        ans1 += 1
print(ans1)


def glyph(node):
    if node.used == 0:
        return '_'
    elif node.x == 0 and node.y == 0:
        return '^'
    elif node.x == 29 and node.y == 0:
        return '@'
    elif node.used > 100:
        return '#'
    elif node.size > 70:
        return '.'
    else:
        return ' '


print(toolkit.render({complex(node.x, node.y): glyph(node) for node in nodes}))
print(5 + 33 + 6 + 5 * 28 + 1)
