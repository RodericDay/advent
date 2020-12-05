import re
import sys


def is_tls(line):
    rx = re.compile(r'(\w)(\w)\2\1')
    parts = re.split(r'\[(.+?)\]', line)
    good = [m for p in parts[::2] for m in rx.findall(p) if m[0] != m[1]]
    bad = [m for p in parts[1::2] for m in rx.findall(p) if m[0] != m[1]]
    return bool(good and not bad)


def is_ssl(line):
    rx = re.compile(r'(?=(\w)(\w)\1)')
    parts = re.split(r'\[(.+?)\]', line)
    good = {m for p in parts[::2] for m in rx.findall(p) if m[0] != m[1]}
    bad = {m[::-1] for p in parts[1::2] for m in rx.findall(p) if m[0] != m[1]}
    return bool(good & bad)


ans1 = 0
ans2 = 0
text = sys.stdin.read()
for line in text.strip().splitlines():
    ans1 += is_tls(line)
    ans2 += is_ssl(line)
print(ans1)
print(ans2)
