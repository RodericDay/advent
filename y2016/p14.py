import re
import sys

import toolkit


text = sys.stdin.read().strip()
found = {i: toolkit.md5(f'{text}{i}') for i in range(30_000)}
print([
    i
    for i, dig in found.items()
    for c in re.findall(r'(.)\1\1', dig)[:1]
    if any(c * 5 in found.get(i + j + 1, '') for j in range(1000))
][63])

for _ in range(2016):
    found = {k: toolkit.md5(v) for k, v in found.items()}

print([
    i
    for i, dig in found.items()
    for c in re.findall(r'(.)\1\1', dig)[:1]
    if any(c * 5 in found.get(i + j + 1, '') for j in range(1000))
][63])
