from collections import Counter


nums = open(0).read().splitlines()

app = eps = ''
for col in zip(*nums):
    n, *_, m = Counter(col).most_common()
    app += n[0]
    eps += m[0]
print(int(app, 2) * int(eps, 2))

xs = nums[:]
ys = nums[:]
for idx in range(len(nums[0])):
    n, _ = Counter(sorted([x[idx] for x in xs])).most_common()[::-1][0]
    xs = [x for x in xs if x[idx] == n]
    m, _ = Counter(sorted([y[idx] for y in ys])).most_common()[::-1][-1]
    ys = [y for y in ys if y[idx] == m]
print(int(xs[0], 2) * int(ys[0], 2))
