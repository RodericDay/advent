from itertools import product


pairs = [(ord(a) - 64, ord(b) - 87) for a, b in map(str.split, open(0).read().splitlines())]
ab_to_c = {(a, b): 3 if a == b else 6 if (b - a) in {1, -2} else 0 for a, b in product([1, 2, 3], repeat=2)}
print(sum(b + ab_to_c[a, b] for a, b in pairs))
ac_to_b = {(a, c): b for (a, b), c in ab_to_c.items()}
x_to_c = {1: 0, 2: 3, 3: 6}
print(sum(ac_to_b[a, x_to_c[x]] + x_to_c[x] for a, x in pairs))
