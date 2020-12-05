import sys


def bin(string, trans=str.maketrans('FBLR', '0101')):
    return int(string.translate(trans), 2)


sids = {bin(ln[:7]) * 8 + bin(ln[7:]) for ln in sys.stdin.read().splitlines()}

ans1 = max(sids)
print(ans1)

ans2, = sids ^ set(range(min(sids), max(sids) + 1))
print(ans2)
