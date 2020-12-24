import sys


def play(start, cycles):
    lim = len(start)
    cur = start[0]
    ns = [None for _ in range(lim + 1)]

    for a, b in zip(start, start[1:] + start[:1]):
        ns[a] = b

    for _ in range(cycles):
        a = ns[cur]
        b = ns[a]
        c = ns[b]

        dest = (cur - 1) or lim
        while dest in (a, b, c):
            dest = (dest - 1) or lim

        ns[dest], ns[c], ns[cur] = a, ns[dest], ns[c]
        cur = ns[cur]

    return ns


text = sys.stdin.read().strip()
ns = [int(n) for n in text]

ordering = play(ns, 100)
sol = [1]
for _ in range(len(ordering) - 2):
    sol.append(ordering[sol[-1]])
print(''.join(str(n) for n in sol[1:]))

ns.extend(n + 1 for n in range(len(ns), 1_000_000))
ordering = play(ns, 10_000_000)
print(ordering[1] * ordering[ordering[1]])
