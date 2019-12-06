import sys
import collections


# build
text = sys.stdin.read()
directed = {}
undirected = collections.defaultdict(set)
for line in text.splitlines():
    A, B = line.split(')')
    directed[B] = A
    undirected[B].add(A)
    undirected[A].add(B)

# pop stack
i = 0
for k in directed:
    while k in directed:
        k = directed[k]
        i += 1
print(i)

# bfs
hops = 0
seen = set()
edge = {'YOU'}
while 'SAN' not in edge:
    hops += 1
    seen |= edge
    edge = {new for node in edge for new in undirected[node]} - seen
print(hops - 2)
