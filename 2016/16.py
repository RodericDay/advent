import hashlib, collections

def options(moves):
    digest = hashlib.md5((key+moves).encode()).hexdigest()
    return [k for k,v in zip('UDLR', digest) if int(v, 16) > 10]

key = 'qljzarfv'
goal = 3+3j
state = collections.deque([('',0)])
M = {'D':1j,'U':-1j,'L':-1,'R':1}
path = None
while state:
    s,i = state.popleft()
    for k in options(s):
        j = i+M[k]
        if j == goal:
            if path is None: print(s+k)
            path = s+k
        elif 0 <= j.imag < 4 and 0 <= j.real < 4:
            state.append((s+k,j))
print(len(path))

