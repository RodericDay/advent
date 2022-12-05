import re


ans1 = ans2 = 0
for line in open(0).read().splitlines():
    a, b, c, d = map(int, re.findall(r'\d+', line))
    ab = set(range(a, b + 1))
    cd = set(range(c, d + 1))
    ans1 += ab <= cd or cd <= ab
    ans2 += any(ab & cd)
print(ans1)
print(ans2)
