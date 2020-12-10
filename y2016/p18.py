import sys


def march(text):
    base = '.' + text + '.'
    for i in range(len(text)):
        yield '.^'[base[i:i + 3] in {'^^.', '.^^', '^..', '..^'}]


text = sys.stdin.read().strip()
seen = [text]
for i in range(400_000):
    seen.append(''.join(march(seen[-1])))
print(''.join(seen[:40]).count('.'))
print(''.join(seen[:400_000]).count('.'))
