import re
import numpy as np

A = np.zeros([6, 50], dtype=int)
with open('08.txt') as fp:
    for line in fp:
        a, b = map(int,re.findall(r'\d+', line))
        inst, *text = line.split(' ')
        if inst=='rect': A[:b,:a] = 1
        elif text[0]=='row': A[a] = np.roll(A[a], b)
        elif text[0]=='column': A.T[a] = np.roll(A.T[a], b)
screen = '\n'.join(map(''.join, A.astype(str)))
print(screen.translate(str.maketrans('01',' *')))
