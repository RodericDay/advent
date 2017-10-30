
txt = '''
Disc #1 has 13 positions; at time=0, it is at position 1.
Disc #2 has 19 positions; at time=0, it is at position 10.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 3.
Disc #6 has 17 positions; at time=0, it is at position 5.
Disc #7 has 11 positions; at time=0, it is at position 0.
'''

# txt = '''
# Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.
# '''

import re
from itertools import count

levels = [list(map(int,t)) for t in re.findall(r' (\d+) .+(\d+)\.', txt)]

for x in count(0):
    n = None
    for t, (npos, p1) in enumerate(levels, 1):
        y = (p1+t+x)%npos
        if n is None: n = y
        elif n != y: break
    else:
        print(x)
        exit()
    continue
