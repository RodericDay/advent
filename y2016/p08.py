import re
import sys

import toolkit


def rect(w, h):
    for y in range(h):
        for x in range(w):
            screen[y][x] = '#'


def rotate_row(y, by):
    screen[y] = screen[y][-by:] + screen[y][:-by]


def rotate_column(x, by):
    tmp = list(zip(*screen))
    tmp[x] = tmp[x][-by:] + tmp[x][:-by]
    screen[:] = list(map(list, zip(*tmp)))


def display(screen):
    print('\n'.join(''.join(line) for line in screen) + '\n')


W, H, text = 50, 6, sys.stdin.read()
screen = [[' ' for _ in range(W)] for _ in range(H)]

text = text.replace('rotate ', 'rotate_')
text = text.replace('=', ' ')
text = re.sub(r'(\d+)x(\d+)', r'w \1 h \2', text)

for line in text.splitlines():
    toolkit.interpret(line, globals())

print(sum(row.count('#') for row in screen))
display(screen)
