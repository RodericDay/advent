import re
import sys


def run(text):
    acc = 0
    pos = 0
    seen = set()
    instructions = text.splitlines()
    while pos not in seen:
        seen.add(pos)
        inst, n = instructions[pos].split()
        if inst == 'acc':
            acc += int(n)
            pos += 1
        elif inst == 'jmp':
            pos += int(n)
        elif inst == 'nop':
            pos += 1

        if pos == len(instructions):
            raise RuntimeError(acc)

    return acc


text = sys.stdin.read()
print(run(text))
for match in re.finditer(r'(jmp|nop)', text):
    seen, (a, b) = match.group(0), match.span()
    pair, = {'jmp', 'nop'} - {seen}
    var = text[:a] + pair + text[b:]
    try:
        run(var)
    except RuntimeError as error:
        print(error)
