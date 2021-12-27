import re


def net_volume(cubes):
    if not cubes:
        return 0

    (is_on, cube), *rest = cubes
    if not is_on:
        return net_volume(rest)

    return volume(cube) - net_volume(intersect(cube, rest)) + net_volume(rest)


def intersect(cube, rest):
    return [
        (True, new)
        for _, other in rest
        for new in [[f(a, b) for a, b, f in zip(cube, other, [max, min] * 3)]]
        if volume(new)
    ]


def volume(cube):
    xA, xB, yA, yB, zA, zB = cube
    return max(xB - xA + 1, 0) * max(yB - yA + 1, 0) * max(zB - zA + 1, 0)


cubes = tuple(
    (line.split()[0] == 'on', [int(n) for n in re.findall(r'-?\d+', line)])
    for line in open(0).read().splitlines()
)
print(net_volume(cubes[:20]))
print(net_volume(cubes))
