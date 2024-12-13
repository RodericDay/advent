import re
from functools import lru_cache

inp = open(0).read()

ns = re.findall(r'\d+', inp)

@lru_cache(maxsize=None)
def transform(n, cnt):
    if cnt == 0:
        return 1
    elif n == '0':
        return transform('1', cnt - 1)
    elif len(n) % 2 == 0:
        mid = len(n) // 2
        return transform(n[:mid], cnt - 1) + transform(n[mid:].lstrip('0') or '0', cnt - 1)
    else:
        return transform(str(int(n) * 2024), cnt - 1)

print(sum(transform(n, 25) for n in ns))
print(sum(transform(n, 75) for n in ns))
