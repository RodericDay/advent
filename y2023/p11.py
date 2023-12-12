import itertools


def star_dist(a, b, N):
    (xa, xb), (ya, yb) = map(sorted, zip(a, b))
    sx = sum(xa < x < xb for x in xs)
    sy = sum(ya < y < yb for y in ys)
    return (xb - xa) + (yb - ya) + (N - 1) * (sx + sy)


text = open(0).read()
ys = {i for i, ln in enumerate(text.splitlines()) if set(ln) == {'.'}}
xs = {i for i, ln in enumerate(zip(*text.splitlines())) if set(ln) == {'.'}}
stars = {(x, y) for y, row in enumerate(text.splitlines()) for x, val in enumerate(row) if val == '#'}
print(sum(star_dist(a, b, 2) for a, b in itertools.combinations(stars, 2)))
print(sum(star_dist(a, b, 1_000_000) for a, b in itertools.combinations(stars, 2)))
