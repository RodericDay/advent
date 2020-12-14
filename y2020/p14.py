import re
import sys
from itertools import product


text = sys.stdin.read()


mem = {}
idem = {'0': '0', '1': '1'}
for line in text.splitlines():
    typ, val = line.split(' = ')
    if typ.startswith('mask'):
        mask = val
    if typ.startswith('mem'):
        pos = int(typ[4:-1])
        known = f'{int(val):b}'.zfill(len(mask))
        string = ''.join(idem.get(c, known[i]) for i, c in enumerate(mask))
        mem[pos] = int(string, 2)
print(sum(mem.values()))


mem = {}
idem = {'X': 'X', '1': '1'}
for line in text.splitlines():
    typ, val = line.split(' = ')
    if typ.startswith('mask'):
        mask = val
    elif typ.startswith('mem'):
        known = f'{int(typ[4:-1]):b}'.zfill(len(mask))
        string = ''.join(idem.get(c, known[i]) for i, c in enumerate(mask))
        for gen in map(iter, product('01', repeat=string.count('X'))):
            tmp = re.sub('X', lambda m: next(gen), string)
            pos = int(tmp, 2)
            mem[pos] = int(val)
print(sum(mem.values()))
