import re, collections

instructions = []
with open('07.txt') as fp:
    for line in (fp.read().strip()
            .replace('RSHIFT', '>>')
            .replace('LSHIFT', '<<')
            .replace('AND', '&')
            .replace('OR', '^')
            .replace('NOT', '~')
            # .replace('1674 -> b', '46065 -> b')
            .swapcase()
            .split('\n')
        ):
        instructions.append(re.sub(r'(.+) -> (.+)', r'\2 = \1', line))

while instructions:
    current, *instructions = instructions
    try:
        exec(current)
        print(current)
    except NameError:
        instructions.append(current)

print(A)
