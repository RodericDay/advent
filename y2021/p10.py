pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
objs = '()[]{}<>'
fam = lambda c: objs.index(c) // 2
val = lambda c: objs.index(c) % 2
ans1 = 0
scores = []
for ln in open(0).read().splitlines():
    stack = []
    for c in ln:
        if val(c) == 0:
            stack.append(c)
        elif fam(c) == fam(stack[-1]) and val(c) == 1:
            stack.pop()
        else:
            ans1 += pts[c]
            break
    else:
        score = 0
        while stack:
            score *= 5
            score += fam(stack.pop()) + 1
        scores.append(score)
ans2 = sorted(scores)[len(scores) // 2]
print(ans1)
print(ans2)
