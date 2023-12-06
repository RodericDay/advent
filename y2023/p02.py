import math
import re


text = open(0).read()
ans1 = 0
ans2 = 0
for idx, line in enumerate(text.splitlines(), 1):
    parse = lambda string: {v: int(k) for k, v in re.findall(r'(\d+) (r|g|b)', string)}
    games = [parse(game) for game in re.findall(r'[^:;]+', line)[1:]]
    rgb = [max(game.get(k, 0) for game in games) for k in 'rgb']
    ans1 += all(qty <= lim for qty, lim in zip(rgb, [12, 13, 14])) and idx
    ans2 += math.prod(rgb)
print(ans1)
print(ans2)

