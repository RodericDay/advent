import re
import sys
from collections import Counter


def decode(string, n):
    def replacer(match):
        char = match.group(0)
        return chr((ord(char) + n - ord('a')) % 26 + ord('a'))
    return re.sub(r'\w', replacer, string)


text = sys.stdin.read()
ans1 = 0
for line in text.splitlines():
    name, sid, checksum = re.match(r'^(.+)-(\d+)\[(.+)\]$', line).groups()
    by_count = ''.join(dict(Counter(sorted(name)).most_common()))
    calc = by_count.replace('-', '')[:5]
    if calc == checksum:
        ans1 += int(sid)
        decoded = decode(name, int(sid))
        if 'north' in decoded:
            ans2 = sid
print(ans1)
print(ans2)
