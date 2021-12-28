def valid_z1s(z2, w, c1, c2, c3):
    valid = {(z2 - w - c3) // 26} | {(z2 * 26 + i) for i in range(26)}
    for z1 in valid:
        if evolve(z1, w, c1, c2, c3) == z2:
            yield z1


def evolve(z, w, c1, c2, c3):
    return (z // c1) if (z % 26 + c2 == w) else (z * 26 + w + c3)


consts = []
for block in open(0).read().split('inp w\n')[1:]:
    els = [ln.split()[-1] for ln in block.splitlines()]
    consts.append((int(els[3]), int(els[4]), int(els[14])))

valid_zs = {0: {0}}
for c1, c2, c3 in consts[:7]:
    valid_zs[len(valid_zs)] = {
        evolve(z, w, c1, c2, c3)
        for z in valid_zs[len(valid_zs) - 1]
        for w in map(int, '123456789')
    }

state = [('', 0)]
idx = 14
for c1, c2, c3 in consts[::-1]:
    idx -= 1
    state = [
        (w + s, z1)
        for s, z2 in state
        for w in '123456789'
        for z1 in valid_z1s(z2, int(w), c1, c2, c3)
        if idx not in valid_zs or z1 in valid_zs[idx]
    ]

(head, _), *body, (tail, _) = sorted(state)
print(tail)
print(head)
