import re, itertools
from collections import deque


with open('20.txt') as fp:
    instructions = fp.read().splitlines()

def decode(code, line):
    for a, b in re.findall(r'swap \w+ (.+) with \w+ (.+)', line):
        i = int(a) if a.isdigit() else code.index(a)
        j = int(b) if b.isdigit() else code.index(b)
        t = str.maketrans(code[i]+code[j],code[j]+code[i])
        return code.translate(t)

    for c in re.findall(r'rotate based on position of letter (.+)', line):
        D = deque(code)
        i = code.index(c)
        D.rotate(sum([1, i, i>=4]))
        return ''.join(D)

    for d, n in re.findall(r'rotate (right|left) (.+) steps?', line):
        D = deque(code)
        n = int(n) * (-1 if d=='left' else 1)
        D.rotate(n)
        return ''.join(D)

    for m in re.findall(r'(\d+) to position (\d+)', line):
        i, j = map(int, m)
        c = code[i]
        code = code[:i]+code[i+1:]
        return code[:j]+c+code[j:]

    for m in re.findall(r'(\d+) through (\d+)', line):
        i, j = map(int, m)
        return code[:i]+code[i:j+1][::-1]+code[j+1:]


code = 'abcdefgh'
for line in instructions:
    code = decode(code, line)
print(code)

for code in map(''.join, itertools.permutations('abcdefgh')):
    start = code
    for line in instructions:
        code = decode(code, line)
    if code == 'fbgdceah':
        print(start)
        exit()
