dots, instructions = open(0).read().split('\n\n')
dots = {eval(pair) for pair in dots.splitlines()}
ans1 = None
for line in instructions.splitlines():
    axis, zz = line.split()[-1].split('=')
    zz = int(zz)
    if axis == 'x':
        dots = {(x, y) if x < zz else (2 * zz - x, y) for x, y in dots}
    elif axis == 'y':
        dots = {(x, y) if y < zz else (x, 2 * zz - y) for x, y in dots}
    if ans1 is None:
        ans1 = len(dots)
x, *_, X = sorted(x for x, y in dots)
y, *_, Y = sorted(y for x, y in dots)
ans2 = ''
for yi in range(y, Y + 1):
    for xi in range(x, X + 1):
        ans2 += '#' if (xi, yi) in dots else ' '
    ans2 += '\n'
print(ans1)
print(ans2)
