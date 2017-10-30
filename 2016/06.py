import collections

xs, ys = '', ''
with open('06.txt') as fp:
    for line in zip(*fp.read().splitlines()):
        (x,_),*body,(y,_) = collections.Counter(line).most_common()
        xs += x
        ys += y
print(xs, ys)
