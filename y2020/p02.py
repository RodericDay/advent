import re
import sys


ans1 = 0
ans2 = 0
for line in sys.stdin.read().splitlines():
    lo, hi, char, pw = re.findall(r'(\d+)-(\d+) (\w): (\w+)', line)[0]
    lo, hi = int(lo), int(hi)
    ans1 += lo <= pw.count(char) <= hi
    ans2 += sum([pw[lo - 1] == char, pw[hi - 1] == char]) == 1
print(ans1)
print(ans2)
