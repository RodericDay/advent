import sys


def op(a, trans=str.maketrans('01', '10')):
    return a + '0' + a[::-1].translate(trans)


def checksum(string):
    return ''.join('01'[a == b] for a, b in zip(string[::2], string[1::2]))


def expand(string, lim):
    while len(string) < lim:
        string = op(string)
    string = string[:lim]

    chk = checksum(string)
    while len(chk) % 2 == 0:
        chk = checksum(chk)
    return chk


text = sys.stdin.read().strip()
print(expand(text, 272))
print(expand(text, 35651584))
