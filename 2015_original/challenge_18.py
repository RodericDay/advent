import functools

def visualize(string):
    print('\n'.join(''.join(string[n:n+W]) for n in range(0, W*H, W))+'\n')

def sides(n):
    row = n//W
    return [x for x in [n-1, n+1] if W*row <= x < W*(row+1)]

@functools.lru_cache(maxsize=None)
def neighbors(n):
    lr = sides(n)
    ud = [x for x in [n-W, n+W] if 0 <= x < W*H]
    dg = [x for y in ud for x in sides(y)]
    return lr + ud + dg

rows = open('challenge_18.txt').read().strip().split()
H, W = len(rows), len(rows[0])
string = list(''.join(rows))
corners = [0, W-1, W*H-1, W*H-W]

for i in corners: string[i] = '#'
for _ in range(100):
    copy = string[:]
    for i, v in enumerate(copy):
        n = sum(copy[j]=='#' for j in neighbors(i))
        if v=='#' and n not in [2, 3]:  string[i] = '.'
        if v=='.' and n == 3:           string[i] = '#'
        if i in corners:                string[i] = '#'

ans = sum(v=='#' for v in string)
print(ans)
