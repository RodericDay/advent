keypad = '''
123
456
789
'''

keypad = '''
  1
 234
56789
 ABC
  D
'''

table = keypad.split('\n')[1:-1]
grid = {}
for j, line in enumerate(table):
    for i, char in enumerate(line):
        if char != ' ':
            grid[i-j*1j] = char

step = {'U':+1j, 'D':-1j, 'L':-1, 'R':+1}
pos = {v:k for k, v in grid.items()}['5']

with open('02.txt') as fp:
    for line in fp.read().strip().split('\n'):
        for char in line.strip():
            if pos + step[char] in grid:
                pos += step[char]
        print(grid[pos])
