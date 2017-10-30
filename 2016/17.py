key = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
ans = 0
for i in range(400000):
    ans += key.count('.')
    buff = '.'+key+'.'
    key = ''.join('^' if buff[i-1]!=buff[i+1] else '.' for i in range(1,len(key)+1))
print(ans)
