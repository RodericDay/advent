from itertools import accumulate

with open('01.txt') as fp:
    txt = fp.read()

ans1 = txt.count('(')-txt.count(')')
print(ans1)

ans2 = 1+next(i for i, n in enumerate(accumulate({'(':1,')':-1}[c] for c in txt)) if n < 0)
print(ans2)
