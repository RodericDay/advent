inp = open(0).read()

rows = [[int(n) for n in row.split()] for row in inp.splitlines()]
cols = [sorted(col) for col in zip(*rows)]
print(sum(abs(a - b) for a, b in zip(*cols)))

print(sum(n * cols[1].count(n) for n in cols[0]))
