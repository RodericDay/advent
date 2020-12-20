import re
import sys


def recurse(rule):
    def replacer(m):
        return f'({recurse(rules[m.group(1)])})'
    return re.sub(r'(\d+)', replacer, rule).replace('"', '').replace(' ', '')


text = sys.stdin.read()
rules, stuff = text.split('\n\n')
rules = dict([ln.split(': ') for ln in rules.splitlines()])

rule0 = re.compile(recurse(rules['0'])).fullmatch
print(sum(bool(rule0(line)) for line in stuff.splitlines()))


def rule8(line):
    # 8 = 42 | 42 8
    for i in range(1, len(line) + 1):
        a, b = line[:i], line[i:]
        if rule42(a):
            if not b or rule8(b):
                return True


def rule11(line):
    # 11 = 42 31 | 42 11 31
    for i in range(1, len(line) + 1):
        for j in range(i, len(line)):
            a, b, c = line[:i], line[i:j], line[j:]
            if rule42(a) and rule31(c):
                if not b or rule11(b):
                    return True


rule42 = re.compile(recurse(rules['42'])).fullmatch
rule31 = re.compile(recurse(rules['31'])).fullmatch
# 0 = 8 11
ans2 = 0
for ln in stuff.splitlines():
    valid = any(rule8(ln[:i]) and rule11(ln[i:]) for i in range(1, len(ln)))
    ans2 += bool(valid)
print(ans2)
