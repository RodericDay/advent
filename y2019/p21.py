import sys

from intcode import compute


walk = [
    'NOT A J',
    'NOT C T',
    'AND D T',
    'OR T J',
    'WALK',
]
run = [
    'NOT A J',
    'NOT C T',
    'AND D T',
    'AND H T',
    'OR T J',
    'NOT B T',
    'AND D T',
    'OR T J',
    'RUN',
]
text = sys.stdin.read()
for code in [walk, run]:
    *chars, ans = compute(text, iter('\n'.join(code + ['']).encode()))
    if ans == 10:
        print(bytearray(chars).decode())
    else:
        print(ans)
