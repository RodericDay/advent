import collections


inp = open(0).read()

aa, bb = inp.split('\n\n')

dd = collections.defaultdict(set)
for row in aa.splitlines():
    a, b = row.split('|')
    dd[int(a)].add(int(b))

bb = [[int(n) for n in row.split(',')] for row in bb.splitlines()]


def is_bad(row):
    for idx, n in enumerate(row):
        if any(n in dd.get(x, []) for x in row[idx + 1:]):
            return True
    return False


def my_sort(row):
    for hop in range(len(row)):
        for ii in range(len(row) - hop - 1):
            jj = ii + 1
            if row[ii] in dd.get(row[jj], []):
                row[ii], row[jj] = row[jj], row[ii]
    return row


print(sum(row[len(row) // 2] for row in bb if not is_bad(row)))
print(sum(my_sort(row)[len(row) // 2] for row in bb if is_bad(row)))
