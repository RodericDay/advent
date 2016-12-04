with open('17.txt') as fp:
    eggnog = [int(n) for n in fp.read().strip().split('\n')]

goal = 150

def partitions(goal, eggnog, n=1):
    for i, size in enumerate(eggnog):
        if size < goal:
            yield from partitions(goal-size, eggnog[i+1:], n+1)
        elif size == goal:
            yield n

combos = list(partitions(goal, eggnog))
ans1 = len(combos)
print(ans1)

ans2 = sum(min(combos)==size for size in combos)
print(ans2)
