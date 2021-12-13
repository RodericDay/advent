import toolkit


dots, instructions = text.split('\n\n')
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
ans2 = '\n' + toolkit.render({complex(*k): '#' for k in dots})
