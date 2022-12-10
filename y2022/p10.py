text = open(0).read()

cycles = [1]
for ln in map(str.split, text.splitlines()):
    match ln:
        case ['addx', i]:
            cycles.extend([0, int(i)])
        case ['noop']:
            cycles.extend([0])

ans1 = 0
ans2, W, H = '', 40, 6
for y in range(H):
    for x in range(W):
        i = 1 + y * W + x
        p = sum(cycles[:i])
        if i % 40 == 20:
            ans1 += i * p
        ans2 += '##' if abs(x - p) <= 1 else '  '
    ans2 += '\n'
print(ans1)
print(ans2)
