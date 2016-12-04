import re

transform = {}
with open('19.txt') as fp:
    for line in fp:
        try:
            b, a = line.strip().split(' => ')
            transform[a] = b
        except:
            goal = line.strip()

seen = set()
for b, a in transform.items():
    for i in range(len(goal)):
        j = i+len(a)
        if goal[i:j] == a:
            seen.add(goal[:i]+b+goal[j:])
ans1 = len(seen)
print(ans1)

ans2 = 0
while goal != 'e':
    for key in transform:
        if key in goal:
            ans2 += 1
            goal = goal.replace(key, transform[key], 1)
print(ans2)
