import re
import collections
import itertools
import copy

text = open('challenge_19.txt').read()
# text = open('challenge_19_test.txt').read()
target = text.split()[-1]
mapping = {b:a for a, b in re.findall(r'(\w+) => (\w+)', text)}

def disassemble(molecule):
    return list(re.findall(r'([A-Z][a-z]?)', molecule))

def outcomes(molecule):
    split = disassemble(molecule)
    for i, v in enumerate(split):
        for x in (b for b, a in mapping.items() if a == v):
            yield ''.join(split[:i] + [x] + split[i+1:])

ans1 = len(set(outcomes(target)))
print(ans1)

def replace_one(target):
    for key in order:
        if key in target:
            return target.replace(key, mapping[key], 1)

order = sorted(sorted(mapping), key=len, reverse=True)
for ans2 in range(1, 1000):
    target = replace_one(target)
    if target == 'e': break
print(ans2)
