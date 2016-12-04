moves = {dx+dy for dx in [-1,0,1] for dy in [-1j,0,1j]} - {0}

with open('18.txt') as fp:
    array = {i+j*1j: char=='#'
        for j, line in enumerate(fp.read().strip().split('\n'))
        for i, char in enumerate(line)
    }

for n in range(100):
    copy = array.copy()
    for pos in array:
        n = sum(copy.get(pos+step, False) for step in moves)
        array[pos] = (n in [2,3]) if array[pos] else (n == 3)
    array[0] = array[99] = array[99j] = array[99+99j] = True

ans = sum(array.values())
print(ans)
