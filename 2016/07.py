import re, itertools, string

singles, pairs = [], {}
for a, b in itertools.product(string.ascii_lowercase, repeat=2):
    if a!=b:
        singles += [a+b+b+a]
        x, y = a+b+a, b+a+b
        pairs[x] = y
        pairs[y] = x

ans1 = ans2 = 0
with open('07.txt') as fp:
    for line in fp.read().splitlines():
        seqs = re.findall(r'[a-z]+', line)
        outer = '-'.join(seqs[::2])
        inner = '-'.join(seqs[1::2])

        if any(s in line for s in singles):
            if not any(s in inner for s in singles):
                ans1 += 1

        if any(x in outer and y in inner for x, y in pairs.items()):
            ans2 += 1

print(ans1)
print(ans2)
