import sys


def is_open(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y + inp
    return f'{n:b}'.count('1') % 2 == 0


inp = int(sys.stdin.read())
valid = {
    complex(x, y)
    for y in range(50)
    for x in range(50)
    if is_open(x, y)
}
steps = (1, -1, 1j, -1j)
edge = {1 + 1j}
seen = set()
hop = 0
while 31 + 39j not in seen:
    edge = {old + step for old in edge for step in steps} & valid - seen
    seen |= edge
    hop += 1
    if hop == 50:
        ans2 = len(seen)
print(hop)
print(ans2)
