import math


def combos(record, dist):
    a, b, c = 1, -record, dist
    x1, x2 = sorted([
        (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a),
        (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a),
    ])
    return int(x2) - int(x1)


text = open(0).read()

records, distances = [[int(n) for n in line.split()[1:]] for line in text.splitlines()]
print(math.prod(combos(a, b)for a, b in zip(*[records, distances])))

records, distances = [[int(''.join(line.split()[1:]))] for line in text.splitlines()]
print(math.prod(combos(a, b)for a, b in zip(*[records, distances])))
