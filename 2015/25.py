x = 20151125
f = lambda x: x*252533%33554393

row, col = 1, 1
goal = 2981, 3075
while (row,col)!=goal:
    x = f(x)
    row -= 1
    col += 1
    if row==0:
        row = col
        col = 1
print(x)
