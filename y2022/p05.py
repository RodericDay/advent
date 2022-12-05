import re
import copy


top, bottom = open(0).read().split('\n\n')
transpose = '\n'.join(map(''.join, zip(*top.splitlines())))
stacks = [list(ln[::-1][1:].strip()) for ln in transpose.splitlines()[1::4]]


def operate(stacks, is_upgraded):
    for line in bottom.splitlines():
        qty, fro, to = map(int, re.findall(r'\d+', line))
        fro, to = fro - 1, to - 1  # shift
        carry = [stacks[fro].pop() for _ in range(qty) if stacks[fro]]
        stacks[to].extend(carry[::-1] if is_upgraded else carry)
    return ''.join(s[-1] for s in stacks if s)


print(operate(copy.deepcopy(stacks), 0))
print(operate(copy.deepcopy(stacks), 1))
