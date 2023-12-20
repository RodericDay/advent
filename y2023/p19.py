import math


def consume(cc, label, step):
    if label in 'AR':
        return label
    else:
        op, new = workflows[label][step]
        if eval(op, None, cc):
            return consume(cc, new, 0)
        else:
            return consume(cc, label, step + 1)


text = open(0).read()
aa, bb = text.split('\n\n')
workflows = {}
for line in aa.splitlines():
    key, rest = line.split('{')
    workflows[key] = [('True:' + ln).split(':')[-2:] for ln in rest[:-1].split(',')]

candidates = [{k[0]: int(k[2:]) for k in ln[1:-1].split(',')} for ln in bb.splitlines()]
print(sum(sum(cc.values()) for cc in candidates if consume(cc, 'in', 0) == 'A'))


def consume2(cc, label, step):
    if label in 'AR':
        yield math.prod(len(vs) for vs in cc.values()), label
    else:
        op, new = workflows[label][step]
        if op == 'True':
            yield from consume2(cc, new, 0)
        else:
            k = op[0]
            vs = {v for v in cc[k] if eval(op, None, {k: v})}
            yield from consume2(cc | {k: vs}, new, 0)
            yield from consume2(cc | {k: cc[k] - vs}, label, step + 1)


bop = {k: set(range(1, 4000 + 1)) for k in 'xmas'}
print(sum(m for m, label in consume2(bop, 'in', 0) if label == 'A'))
