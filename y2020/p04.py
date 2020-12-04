import re
import sys


def checks(byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
    yield 1920 <= int(byr) <= 2002
    yield 2010 <= int(iyr) <= 2020
    yield 2020 <= int(eyr) <= 2030
    if hgt.endswith('cm'):
        yield 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith('in'):
        yield 59 <= int(hgt[:-2]) <= 76
    else:
        yield False
    yield re.match(r'^#[0-9a-f]{6}$', hcl)
    yield re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', ecl)
    yield re.match(r'^\d{9}$', pid)


ans1 = 0
ans2 = 0
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
for blob in sys.stdin.read().split('\n\n'):
    passport = dict(re.findall(r'(\S+):(\S+)', blob))
    valid = not fields.difference(passport)
    ans1 += valid
    if valid:
        ans2 += all(checks(**passport))
print(ans1)
print(ans2)
