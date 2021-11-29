import itertools


def is_win(p_hp, p_atk, p_def, b_hp, b_atk, b_def):
    while True:
        b_hp -= max(1, p_atk - b_def)
        if b_hp <= 0:
            return True
        p_hp -= max(1, b_atk - p_def)
        if p_hp <= 0:
            return False


weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]
rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]
opts = [
    [sum(vs) for vs in zip(*[w, a, r1, r2])]
    for w, a in itertools.product(weapons, armors)
    for r1, r2 in itertools.combinations(rings, 2)
]
p_hp = 100
b_hp, b_atk, b_def = map(int, re.findall(r'(\d+)', text))
wins = {True: set(), False: set()}
for cost, p_atk, p_def in opts:
    wins[is_win(p_hp, p_atk, p_def, b_hp, b_atk, b_def)].add(cost)
ans1 = min(wins[True])
ans2 = max(wins[False])
