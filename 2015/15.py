import re

with open('15.txt') as fp:
    data = [[int(x) for x in re.findall(r'-?\d+',line)] for line in fp]

ans1 = ans2 = 0
goal = 100
for a in range(goal):
    for b in range(goal-a):
        for c in range(goal-a-b):
            d = goal-a-b-c

            qty = a,b,c,d
            dot = [[x*v for v in arr] for x, arr in zip(qty, data)]
            p,q,r,s,t = [max(sum(row), 0) for row in zip(*dot)]
            score = p*q*r*s
            ans1 = max(ans1, score)
            if t==500:
                ans2 = max(ans2, score)

print(ans1)
print(ans2)
