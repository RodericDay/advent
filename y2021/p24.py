def valid_z1s(z2, w, c1, c2, c3):
    valid = {(z2 - w - c3) // 26} | {(z2 * 26 + i) for i in range(26)}
    for z1 in valid:
        if z1 < 26 ** exp:
            if evolve(z1, w, c1, c2, c3) == z2:
                yield z1


def evolve(z, w, c1, c2, c3):
    return (z // c1) if (z % 26 + c2 == w) else (z * 26 + w + c3)


consts = [
    (int(els[4]), int(els[5]), int(els[15]))
    for block in open(0).read().split('inp w')[1:]
    for els in [[ln.split()[-1] for ln in block.splitlines()]]
]
state = [('', 0)]
for exp, (c1, c2, c3) in list(enumerate(consts, 1))[::-1]:
    print(exp, len(state))
    state = [
        (w + s, z1)
        for s, z2 in state
        for w in '123456789'
        for z1 in valid_z1s(z2, int(w), c1, c2, c3)
    ]

(head, _), *body, (tail, _) = sorted(state)
print(tail)
print(head)
