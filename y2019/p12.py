import functools
import itertools
import re
import sys
from math import gcd


def calculate_energy(moons, vels):
    return sum(
        sum(abs(p) for p in moon) * sum(abs(v) for v in vel)
        for moon, vel in zip(moons, vels)
    )


def simulate(text, axes=slice(0, 3), lim=None):
    g = (int(n) for n in re.findall(r'-?\d+', text))
    moons = [point[axes] for point in zip(*[g] * 3)]
    vels = [[0, 0, 0] for m in moons]

    seen = set()
    for step in itertools.count():
        if lim is not None and step >= lim:
            break

        for (i, A), (j, B) in itertools.combinations(enumerate(moons), 2):
            dV = [max(a < b, 0) or -max(b < a, 0) for a, b in zip(A, B)]
            vels[i] = [v + d for v, d in zip(vels[i], dV)]
            vels[j] = [v - d for v, d in zip(vels[j], dV)]

        for i, moon in enumerate(moons):
            moons[i] = [p + v for p, v in zip(moons[i], vels[i])]

        key = str(moons) + str(vels)
        if key in seen:
            break
        seen.add(key)

    return step, calculate_energy(moons, vels)


text = sys.stdin.read()

_, energy = simulate(text, lim=1000)
print(energy)

nX, _ = simulate(text, axes=slice(0, 1))
nY, _ = simulate(text, axes=slice(1, 2))
nZ, _ = simulate(text, axes=slice(2, 3))
lcm = functools.reduce(lambda a, b: a * b // gcd(a, b), [nX, nY, nZ])
print(lcm)
