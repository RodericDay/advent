# flake8: noqa
import sys


text = sys.stdin.read()


pos = 0
aim = 1
for line in text.splitlines():
    char, step = line[0], int(line[1:])
    if char == 'N': pos += step * 1j
    elif char == 'S': pos -= step * 1j
    elif char == 'E': pos += step
    elif char == 'W': pos -= step
    elif char == 'F': pos += step * aim
    elif char == 'L': aim *= 1j ** (step // 90)
    elif char == 'R': aim /= 1j ** (step // 90)
print(abs(pos.real) + abs(pos.imag))


pos = 0
way = 10 + 1j
for line in text.splitlines():
    char, step = line[0], int(line[1:])
    if char == 'N': way += step * 1j
    elif char == 'S': way -= step * 1j
    elif char == 'E': way += step
    elif char == 'W': way -= step
    elif char == 'F': pos += step * way
    elif char == 'L': way *= 1j ** (step // 90)
    elif char == 'R': way /= 1j ** (step // 90)
print(abs(pos.real) + abs(pos.imag))
