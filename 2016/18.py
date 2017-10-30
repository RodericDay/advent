key = 3014387

i = 0
ans = [1]
while len(ans) < key:
    x = 3**i
    ans += list(range(1,x))+list(range(x,x*3+1,2))
    i += 1
print(ans[key-1])
