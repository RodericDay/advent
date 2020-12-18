import re
import sys


class X(int):
    def __sub__(a, y): return X(int(a) * y)
    def __add__(a, y): return X(int(a) + y)
    def __mul__(a, y): return X(int(a) + y)


text = sys.stdin.read()
ans1 = 0
ans2 = 0
trans = str.maketrans('*+', '-*')
for ln in text.splitlines():
    ans1 += eval(re.sub(r'(\d+)', r'X(\1)', ln.replace('*', '-')))
    ans2 += eval(re.sub(r'(\d+)', r'X(\1)', ln.translate(trans)))
print(ans1)
print(ans2)
