top = 4294967295
with open('19.txt') as fp:
    ranges = sorted(tuple(map(int,line.split('-'))) for line in fp.read().splitlines())


starts = [b+1 for a,b in ranges]
ends = [a-1 for a,b in ranges][1:] + [top]
total = sorted(starts+ends)
ans = 0
for a,b in zip(total, total[1:]):
    for A,B in ranges:
        if (a < A and b < A) or (a > B and b > B):
            pass
        else:
            break
    else:
        ans += b-a+1
print(ans)
