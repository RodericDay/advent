ans1 = 0
ans2 = None
for i, char in enumerate(open(0).read(), 1):
    ans1 += {'(': 1, ')': -1}[char]
    if ans1 == -1 and ans2 is None:
        ans2 = i
print(ans1)
print(ans2)
