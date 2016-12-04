import itertools

string = '1113122113'

for _ in range(40):
    string = ''.join(str(c) for n, g in itertools.groupby(string) for c in [len(list(g)), n])

ans1 = len(string)
print(ans1)

for _ in range(10):
    string = ''.join(str(c) for n, g in itertools.groupby(string) for c in [len(list(g)), n])

ans2 = len(string)
print(ans2)
