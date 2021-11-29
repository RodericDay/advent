from toolkit import product


def combine(qtys):
    return [max(0, sum(a * b for a, b in zip(qtys, vs))) for vs in zip(*data)]


data = [
    [int(n) for n in re.findall(r'-?\d+', ln)]
    for ln in df.read_text().splitlines()
]
qtys = [
    combine([A, B, C, 100 - A - B - C])
    for A in range(101)
    for B in range(101 - A)
    for C in range(101 - A - B)
]
ans1 = max(product(combo[:-1]) for combo in qtys)
ans2 = max(product(combo[:-1]) for combo in qtys if combo[-1] == 500)
