import os, re

fixed = set()
with open('22.txt') as fp:
    next(fp)
    next(fp)
    X,Y,S,U,A,P = zip(*[tuple(map(int,re.findall(r'\d+', line)))
                      for line in fp.read().splitlines()])

    rows = [1j*n for n in range(max(Y)+1)]
    cols = [n for n in range(max(X)+1)]
    for x,y,s,u in zip(X,Y,S,U):
        p = x+1j*y
        if s>max(S)/2: fixed |= {p}
        if y==0 and x==max(X): data = p
        if y==0 and x==0: me = p
        if u==0: actual = p

def render(actual, data):
    for p in (i+j for j in rows for i in cols):
        if p.real==0: print()
        c = '.'
        if p==me: c = '?'
        if p==data: c = '!'
        if p==actual: c = '_'
        if p in fixed: c = '#'
        print(c, end=' ')
    print()

i = 0
def move(actual, data, v):
    global i
    i += 1
    actual += v
    if actual==data:
        data -= v
    if data!=me:
        return actual, data

state = (actual, data)
for i, v in enumerate([-1]*5+[-1j]*34+[1]*6+[1j,-1,-1,-1j,1]*30):
    state = move(*state, v)
    if not state:
        print(i)
        break
