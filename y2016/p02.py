import sys

import toolkit


def travel(text, start, image):
    grid, _, _ = toolkit.read_image(image)
    pos = {v: k for k, v in grid.items()}[start]
    for line in text.splitlines():
        for step in map(moves.get, line):
            if grid[pos + step].strip():
                pos += step
        yield grid[pos]


text = sys.stdin.read()
moves = {'U': -1j, 'L': -1, 'R': 1, 'D': 1j}
keypad1 = '''
123
456
789
'''
keypad2 = '''
  1
 234
56789
 ABC
  D
'''
print(''.join(travel(text, '5', keypad1)))
print(''.join(travel(text, '7', keypad2)))
