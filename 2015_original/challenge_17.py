# smrt
sample  = sorted([20, 15, 10, 5, 5])
options = sorted([50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40])

def recurse(target, options):
    for i, opt in enumerate(options):
        if target-opt==0:
            yield [opt]
        for tail in recurse(target-opt, options[i+1:]):
            yield [opt]+tail

valid = list(recurse(150, options))
print(len(valid))
mini = min(map(len, valid))
valid = [v for v in valid if len(v)==mini]
print(len(valid))

# brute
import itertools

ans = []
for combo in itertools.product([0, 1], repeat=len(options)):
    vals = [b for a, b in zip(combo, options) if a]
    if sum(vals) is not 150: continue
    ans.append(tuple(vals))
print(len(ans))
mini = min(map(len, ans))
print(len([s for s in ans if len(s)==mini]))
