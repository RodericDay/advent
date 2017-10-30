import re
import itertools
from collections import defaultdict

graph = defaultdict(dict)
text = open('challenge_09.txt').read()
for a, b, v in re.findall(r'(\w+) to (\w+) = (\d+)', text):
    graph[a][b] = int(v)
    graph[b][a] = int(v)

def distance(seq):
    return sum(graph[a][b] for a, b in zip(seq, seq[1:]))

ans = max(distance(seq) for seq in itertools.permutations(graph))
print(ans)
