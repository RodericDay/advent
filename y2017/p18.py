import collections


def program(qsnd, qrcv, known=tuple()):
    i, j = 0, 0
    regs = collections.defaultdict(int)
    regs.update(known)
    read = lambda value: regs[value] if value.isalpha() else int(value)
    while True:
        line = lines[i]
        op, *args = line.split()
        if op == 'set':
            x, y = args
            regs[x] = read(y)
        elif op == 'mul':
            x, y = args
            regs[x] *= read(y)
        elif op == 'jgz':
            x, y = args
            if read(x) > 0:
                i += read(y)
                continue
        elif op == 'add':
            x, y = args
            regs[x] += read(y)
        elif op == 'snd':
            x, = args
            qsnd.append(read(x))
        elif op == 'rcv':
            x, = args
            if not known:
                if read(x) != 0:
                    yield False
                    continue
            else:
                if j < len(qrcv):
                    regs[x] = qrcv[j]
                    j += 1
                else:
                    yield False
                    continue
        elif op == 'mod':
            x, y = args
            regs[x] %= read(y)
        i += 1
        yield True


lines = df.read_text().splitlines()

q = []
p = program(q, None)
while next(p): pass
ans1 = q[-1]

qA, qB = [], []
p0 = program(qA, qB, {'p': 0})
p1 = program(qB, qA, {'p': 1})
while next(p0) + next(p1): pass
ans2 = len(qB)
