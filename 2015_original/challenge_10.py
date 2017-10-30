import itertools

def solve(seq):
    out = ''
    for v, group in itertools.groupby(seq):
        out += '{}{}'.format(len(list(group)), v)
    return out

ans = '1113122113'
for _ in range(50):
    ans = solve(ans)
print(len(ans))

# finished #27
