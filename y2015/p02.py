import sys


ans1 = 0
ans2 = 0
for line in sys.stdin.readlines():
    a, b, c = sorted(map(int, line.split('x')))
    ans1 += 2 * (a * b + b * c + a * c) + a * b
    ans2 += a * b * c + 2 * (a + b)
print(ans1)
print(ans2)
