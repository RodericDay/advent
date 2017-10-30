'''
Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning
        off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle
        four lights.

After following the instructions, how many lights are lit?
'''

import re

grid = [[False for _ in range(1000)] for _ in range(1000)]
# for line in ["turn on 0,0 through 999,999"]:
# for line in ["turn on 0,0 through 999,0"]:
for line in open('challenge_06.txt').read().strip().split('\n'):
    if line.startswith('turn off'): action = lambda state: max(0, state - 1) # 0
    if line.startswith('turn on'): action = lambda state: state + 1 # 1
    if line.startswith('toggle'): action = lambda state: state + 2 # not state
    x1, y1, x2, y2 = map(int, (n for pair in re.findall(r"(\d+),(\d+)", line) for n in pair))
    for y in range(y1, y2+1):
        line = grid[y]
        for x in range(x1, x2+1):
            line[x] = action(line[x])

print(sum(state for line in grid for state in line))
