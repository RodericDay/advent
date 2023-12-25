import collections
import itertools
import re


def part1(H):
    """
    2 variables, 2 equations

    px1 + vx1 * t1 == px2 + vx2 * t2
    py1 + vy1 * t1 == py2 + vy2 * t2

    t1 = (px2 - px1) / vx1 + (vx2 / vx1) * t2
    t1 = (py2 - py1) / vy1 + (vy2 / vy1) * t2

    (px2 - px1) / vx1 - (py2 - py1) / vy1 = (vy2 / vy1 - vx2 / vx1) * t2
    t2 = c1 / c2
    c1 = (px2 - px1) / vx1 - (py2 - py1) / vy1
    c2 = (vy2 / vy1 - vx2 / vx1)
    """
    n = 0
    lo, hi = (7, 27) if len(H) < 100 else (2e14, 4e14)
    for aa, bb in itertools.combinations(H, 2):
        px1, py1, pz1, vx1, vy1, vz1 = aa
        px2, py2, pz2, vx2, vy2, vz2 = bb

        c1 = (px2 - px1) / vx1 - (py2 - py1) / vy1
        c2 = (vy2 / vy1 - vx2 / vx1)
        if c2 == 0: continue
        t2 = (c1 / c2)
        t1 = (px2 - px1) / vx1 + (vx2 / vx1) * t2
        if t1 <= 0 or t2 <= 0: continue
        if not lo < px1 + vx1 * t1 < hi: continue
        if not lo < py1 + vy1 * t1 < hi: continue
        if not lo < px2 + vx2 * t2 < hi: continue
        if not lo < py2 + vy2 * t2 < hi: continue
        n += 1
    return n


def part2(H):
    """
    6 + t variables, 3 * t equations
    """
    try:
        import z3
    except:
        return 'Need z3-solver'
    Q = {k: z3.Real(k) for k in 'px py pz vx vy vz t0 t1 t2'.split()}
    solver = z3.Solver()
    solver.add(H[0].px + H[0].vx * Q['t0'] == Q['px'] + Q['vx'] * Q['t0'])
    solver.add(H[0].py + H[0].vy * Q['t0'] == Q['py'] + Q['vy'] * Q['t0'])
    solver.add(H[0].pz + H[0].vz * Q['t0'] == Q['pz'] + Q['vz'] * Q['t0'])
    solver.add(H[1].px + H[1].vx * Q['t1'] == Q['px'] + Q['vx'] * Q['t1'])
    solver.add(H[1].py + H[1].vy * Q['t1'] == Q['py'] + Q['vy'] * Q['t1'])
    solver.add(H[1].pz + H[1].vz * Q['t1'] == Q['pz'] + Q['vz'] * Q['t1'])
    solver.add(H[2].px + H[2].vx * Q['t2'] == Q['px'] + Q['vx'] * Q['t2'])
    solver.add(H[2].py + H[2].vy * Q['t2'] == Q['py'] + Q['vy'] * Q['t2'])
    solver.add(H[2].pz + H[2].vz * Q['t2'] == Q['pz'] + Q['vz'] * Q['t2'])
    solver.check()
    model = solver.model()
    return model.eval(Q['px'] + Q['py'] + Q['pz'])


text = open(0).read()
Hail = collections.namedtuple('Hail', 'px py pz vx vy vz')
H = [Hail(*[int(n) for n in re.findall(r'-?\d+', line)]) for line in text.splitlines()]
print(part1(H))
print(part2(H))
