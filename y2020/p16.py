import sys

import toolkit


def parse_info(info):
    out = {}
    for line in info.splitlines():
        key, vals = line.split(':')
        out[key] = set()
        for a, b in zip(*[iter(toolkit.integers(vals))] * 2):
            out[key] |= set(range(a, b + 1))
    return out


text = sys.stdin.read()
info, mine, rest = text.split('\n\n')
info = parse_info(info).items()
mine = toolkit.integers(mine)

rest = [toolkit.integers(ln) for ln in rest.splitlines()][1:]
valid = {v for _, vs in info for v in vs}
error_rate = sum(n for row in rest for n in row if n not in valid)
print(error_rate)

rows = [row for row in rest if valid.issuperset(row)]
options = [{k for k, vs in info if vs.issuperset(col)} for col in zip(*rows)]
ans2 = 1
found = set()
for k, vs in sorted(enumerate(options), key=lambda pair: len(pair[1])):
    v, = vs - found
    found.add(v)
    if v.startswith('departure'):
        ans2 *= mine[k]
print(ans2)
