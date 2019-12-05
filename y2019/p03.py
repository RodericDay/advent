import sys


text = sys.stdin.read()
maps = {'R': -1, 'D': -1j, 'L': 1, 'U': 1j}


info = []
for path in text.splitlines():
    i, p = 0, 0
    best = {}
    for a, *n in path.split(','):
        d = maps[a]
        for _ in range(int(''.join(n))):
            i += 1
            p += d
            if p not in best:
                best[p] = i
    info.append(best)


isect = set(info[0]) & set(info[1])
print(int(min((abs(p.real) + abs(p.imag), p) for p in isect)[0]))
print(min(info[0][p] + info[1][p] for p in isect))
