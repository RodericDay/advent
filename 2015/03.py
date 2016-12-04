from collections import Counter

moves = dict(zip('v^<>', [-1j,1j,-1,1]))

with open('03.txt') as fp:
    path = fp.read().replace('\n','')

def gift(path):
    pos = 0
    counter = Counter()
    for char in path:
        counter[pos] += 1
        pos += moves[char]
    return counter

ans1 = len(gift(path))
print(ans1)

ans2 = 1+len(gift(path[::2])+gift(path[1::2]))
print(ans2)
