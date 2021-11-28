from itertools import groupby


def mod(string):
    return ''.join(f'{len(list(vs))}{k}' for k, vs in groupby(string))


inp = df.read_text().splitlines()
for _ in range(50):
    inp.append(mod(inp[-1]))
ans1 = len(inp[40])
ans2 = len(inp[50])
