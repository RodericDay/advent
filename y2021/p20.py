def enhance(pos, cache={}):
    seq = tuple(image.get(pos + d, infinity) for d in D9)
    key = infinity, seq
    if key not in cache:
        cache[key] = alg[int(''.join({'.':'0', '#':'1'}[x] for x in seq), 2)]
    return cache[key]


text = open(0).read()
alg, text = text.split('\n\n')
D9 =  [dx + dy for dy in [-1j, 0, 1j] for dx in [-1, 0, 1]]

image = {}
for y, line in enumerate(text.splitlines()):
    for x, char in enumerate(line):
        image[complex(x, y)] = char

X, Y = x, y
for i in range(1, 50 + 1):
    infinity =  '#.'[i % 2]
    image = {(x + y * 1j): enhance(x + y * 1j)
        for x in range(0 - 2 * i, X + 2 * i)
        for y in range(0 - 2 * i, Y + 2 * i)
    }
    if i in {2, 50}:
        print(sum(v == '#' for v in image.values()))
