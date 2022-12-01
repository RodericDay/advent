packs = [sum(map(int, block.splitlines())) for block in open(0).read().split('\n\n')]
print(max(packs))
print(sum(sorted(packs)[-3:]))
