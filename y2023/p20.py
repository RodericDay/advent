import math


def send(parent, sender, signal):
    match kinds[sender], signal:
        case 'rx' | 'output', _:
            signal = None
        case 'button' | 'broadcaster', _:
            pass
        case '%', 0:
            signal = state[sender] = int(not state[sender])
        case '%', 1:
            signal = None
        case '&', _:
            state[sender][parent] = signal
            seen = set(state[sender].values())
            signal = 0 if seen == {1} else 1
        case default:
            raise RuntimeError(default)

    if signal is not None:
        for target in targets[sender]:
            # print(sender, signal, target)
            output.append(signal)
            yield (sender, target, signal)


def deps(p):
    seen = set()
    state = {p}
    while state:
        seen |= state
        state = {k for p in state for k, vs in targets.items() if p in vs and k not in seen}
    return tuple(sorted(seen))


text = open(0).read()
targets = {'button': ['broadcaster']}
kinds = {'button': 'button', 'rx': 'rx', 'output': 'output'}
for line in text.splitlines():
    src, dst = line.split(' -> ')
    dst = dst.split(', ')
    if src == 'broadcaster':
        label = kind = 'broadcaster'
    else:
        label, kind = src[1:], src[0]
    targets[label] = dst
    kinds[label] = kind
state = {}
state |= {l: 0 for l, k in kinds.items() if k == '%'}
state |= {l: {i: 0 for i, ts in targets.items() if l in ts} for l, k in kinds.items() if k == '&'}

families = {}
for k in kinds:
    families.setdefault(hash(deps(k)), []).append(k)
families = {tuple(vs): set() for vs in families.values() if len(vs) > 1}

seq = []
seen = set()
while True:
    output = []
    active = [(None, 'button', 0)]
    while active:
        active = [new for old in active for new in send(*old)]
    seq.append(output)

    before = [len(vs) for vs in families.values()]
    for ks in families:
        families[ks].add(hash(str([state[k] for k in ks])))
    after = [len(vs) for vs in families.values()]
    if before == after:
        break

    if len(seq) == 1000:
        # pt 1
        los = [sum(v == 0 for v in vs) for vs in seq]
        his = [sum(v == 1 for v in vs) for vs in seq]
        print(sum(los[i % len(los)] for i in range(1000)) * sum(his[i % len(his)] for i in range(1000)))
print(math.prod(after))
