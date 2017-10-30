import re

def decompress(trailing, exhaustive, len=len):
    # send len=str for debug output
    out = len('')
    while trailing and not trailing.isalpha():
        leading, n, r, trailing = re.findall(r'([A-Z]*)\((\d+)x(\d+)\)(.+)', trailing)[0]
        out += len(leading)
        # but actually, n denotes a section that is a substring, not trailing
        substring, trailing = trailing[:int(n)], trailing[int(n):]
        if exhaustive:
            out += int(r) * decompress(substring, exhaustive, len)
        else:
            out += int(r) * len(substring)
    # ensure any trailing left is captured
    return out + len(trailing)

test = decompress('X(8x2)(3x3)ABCY', True, str)
assert test == 'XABCABCABCABCABCABCY', test

with open('09.txt') as fp:
    string = fp.read().strip()
print(decompress(string, False))
print(decompress(string, True))
