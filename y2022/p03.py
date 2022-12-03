import string
import itertools


abc = ' ' + string.ascii_lowercase + string.ascii_uppercase
common = lambda ss: set.intersection(*map(set, ss))
tally = lambda sss: sum(abc.index(common(ss).pop()) for ss in sss)
lns = open(0).read().splitlines()
print(tally([[ln[:len(ln) // 2], ln[len(ln) // 2:]] for ln in lns]))
print(tally(zip(*[iter(lns)] * 3)))
