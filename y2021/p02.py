s1 = 0
s2, aim = 0, 0
for line in text.splitlines():
    k, v = line.split()
    ds = {'forward': 1, 'down': 1j, 'up': -1j}[k] * int(v)
    s1 += ds
    aim += ds.imag
    s2 += ds.real + aim * ds.real * 1j
ans1 = int(s1.real * s1.imag)
ans2 = int(s2.real * s2.imag)
