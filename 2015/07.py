import re, collections

d = {
    'or': '^',
    'and': '&',
    'not': '~',
    'rshift': '>>',
    'lshift': '<<',
}

with open('07.txt') as fp:
    code = fp.read()

_ = code.swapcase()
_ = re.sub(r'(.+) -> (.+)', r'\2 = \1', _)
_ = re.sub(r'[a-z]+', lambda m: d[m.group(0)], _)
instruction = collections.deque(_.splitlines())

while instruction:
    try:
        exec(instruction[-1])
        instruction.pop()
    except NameError:
        instruction.rotate(1)
print(A)
