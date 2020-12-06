import collections
import sys

import toolkit


def handle(string):
    if string.startswith('value'):
        _, value, _, _, t0, i0 = string.split()
        regs[t0 + i0].append(int(value))
        return True
    elif string.startswith('bot'):
        t0, i0, _, _, _, t1, i1, _, _, _, t2, i2 = string.split()
        try:
            lo, hi = sorted(regs[t0 + i0])
        except ValueError:
            return False
        regs[t1 + i1].append(lo)
        regs[t2 + i2].append(hi)
        return True


regs = collections.defaultdict(list)
toolkit.loop_consume(sys.stdin.read().splitlines(), handle)
print(next(k for k, v in regs.items() if set(v) == {17, 61}))
print(regs['output0'][0] * regs['output1'][0] * regs['output2'][0])
