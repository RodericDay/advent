import sys

from toolkit import render


w, h = 25, 6
text = sys.stdin.read()

count = lambda m: lambda layer: sum(n == m for n in layer)  # noqa

layers = list(zip(*[(int(n) for n in text.strip())] * w * h))
min_layer = min(layers, key=count(0))
print(count(1)(min_layer) * count(2)(min_layer))

px = (next(n for n in stack if n != 2) for stack in zip(*layers))
grid = {complex(x, y): next(px) for y in range(h) for x in range(w)}
print(render(grid, ' #'))
