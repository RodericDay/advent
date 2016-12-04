import re

ans1 = 0
ans2 = 0
with open('02.txt') as fp:
    for line in fp:
        w, h, l = map(int, re.findall(r'\d+', line))
        # 1
        areas = (w*h, h*l, w*l)
        ans1 += 2*sum(areas)+min(areas)
        # 2
        vol = w*h*l
        per = 2*min(w+h, h+l, w+l)
        ans2 += per + vol

print(ans1)
print(ans2)
