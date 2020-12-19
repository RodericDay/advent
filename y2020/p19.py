import re
import sys


def recurse(rule):
    return re.sub(r'(\d+)', lambda m: f'({recurse(rules[m.group(1)])})', rule)


text = sys.stdin.read()
rules, stuff = text.split('\n\n')
rules = dict([ln.split(': ') for ln in rules.splitlines()])

ans = 0
rex = re.compile(recurse(rules['0']).replace('"', '').replace(' ', '') + '$')
for line in text.splitlines():
    ans += bool(rex.match(line))
print(ans)
