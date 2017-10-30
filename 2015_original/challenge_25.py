import collections as cl

manual = cl.defaultdict(cl.Counter)

"To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075."

current = 20151125
for diag in range(7000):
    for l in range(diag+1):
        manual[diag-l][l] = current
        current = (current * 252533) % 33554393

for i in range(10):
    for j in range(10):
        print(manual[i][j], end=' ')
    print()

print(manual[2981-1][3075-1])
