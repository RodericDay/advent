import sys


sids = []
for line in sys.stdin.read().splitlines():
    rows = list(range(1, 128))
    for char in line[:7]:
        rows = [rows[:len(rows)//2], rows[len(rows)//2:]]['FB'.index(char)]
    row, = rows

    cols = list(range(8))
    for char in line[7:]:
        cols = [cols[:len(cols)//2], cols[len(cols)//2:]]['LR'.index(char)]
    col, = cols

    sids.append(row * 8 + col)

ans1 = max(sids)
ans2, = set(range(min(sids), max(sids) + 1)).difference(sids)

print(ans1)
print(ans2)
