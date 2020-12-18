import re
import sys


def reval1(ln):
    a, *rest = ln.split()
    for b, c in zip(*[iter(rest)] * 2):
        a = eval(f'{a} {b} {c}')
    return a


def reval2(ln):
    while '+' in ln:
        ln = re.sub(r'\d+ \+ \d+', lambda m: str(eval(m.group(0))), ln)
    return eval(ln)


def process(ln, reval):
    while '(' in ln:
        ln = re.sub(r'\(([^\(\)]+)\)', lambda m: str(reval(m.group(1))), ln)
    return reval(ln)


text = sys.stdin.read()
ans1 = 0
ans2 = 0
for ln in text.splitlines():
    ans1 += int(process(ln, reval=reval1))
    ans2 += int(process(ln, reval=reval2))
print(ans1)
print(ans2)
