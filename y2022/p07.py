import collections
import itertools


text = open(0).read()


path = []
dirs = collections.defaultdict(int)
for line in map(str.split, text.splitlines()):
    match line:
        case ('$', 'cd', '..'):
            path.pop()
        case ('$', 'cd', loc):
            path.append(loc)
        case ('$', 'ls'):
            pass
        case ('dir', _):
            pass
        case (size, _):
            for leg in itertools.accumulate(path):
                dirs[leg] += int(size)


ans1 = sum(size for size in dirs.values() if size <= 100_000)
print(ans1)

free = 70_000_000 - dirs['/']
ans2 = min(size for size in dirs.values() if free + size >= 30_000_000)
print(ans2)
