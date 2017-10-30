import re
import collections
import itertools

text = open('challenge_13.txt').read()

# total change in happiness
mapping = collections.defaultdict(dict)
regex = r'(\w+) .* (lose|gain) (\d+) .* (\w+)\.'
for a, change, n, b in re.findall(regex, text):
    mapping[a][b] = (1 if change=='gain' else -1)*int(n)

# part 2
for person in list(mapping):
    mapping[person]['me'] = 0
    mapping['me'][person] = 0

def happiness(combo):
    return sum(mapping[a][b]+mapping[b][a]
        for a, b in zip(combo, combo[1:]+combo[:1]))

ans = max(happiness(combo) for combo in itertools.permutations(mapping))
print(ans)
