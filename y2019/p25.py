import itertools
import sys

from intcode import compute


'''
. . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . .

. . . . . . . # . . . . . . . . . .
              |
. . . . . . @-@-#-# . . . . . . . .
                |
. . . . . . . . C . . . . . . . . .
                |
. . . . . . . @ @-@ . . . . . . . .
              | | |
. . . . . . #-#-# #w@w@ . . . . . .
                    | |
. . . . . . . . Pn@e# # . . . . . .
                e
. . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . .

'''

text = sys.stdin.read()

code = '''
north
west
take mug
west
take easter egg
east
east
south
south
take asterisk
south
west
north
take jam
south
east
north
east
take klein bottle
south
west
take tambourine
west
take cake
east
south
east
take polygon
north
'''

bytes_ = list(code.lstrip().encode())
items = {line for line in code.splitlines() if line.startswith('take')}
combos = itertools.combinations(sorted(items), 4)
last_line = ''
history = ''
for c in map(chr, compute(text, iter(bytes_))):
    history += c
    if history.endswith('== Security Checkpoint =='):
        take = next(combos)
        drop = items.difference(take)
        instructions = '\n'.join(
            [line for line in take] +
            [line.replace('take', 'drop') for line in drop] +
            ['east\n']
        )
        bytes_.extend(instructions.encode())
print(history.splitlines()[-1])
