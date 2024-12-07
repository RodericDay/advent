import re


inp = open(0).read()
print(sum(int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', inp)))


tot = 0
toggle = True
for do, dont, mul, a, b in re.findall(r'(do)\(\)|(don\'t)\(\)|(mul)\((\d+),(\d+)\)', inp):
    if do:
        toggle = True
    if dont:
        toggle = False
    if mul and toggle:
        tot += int(a) * int(b)
print(tot)
