import re


def intersect(cube, other):
    return not (
        cube[1] <= other[0] or
        cube[0] >= other[1] or
        cube[3] <= other[2] or
        cube[2] >= other[3] or
        cube[5] <= other[4] or
        cube[4] >= other[5]
    )


def insert(cube, val):
    to_break = {other for other in seen if intersect(cube, other)}
    for cu in to_break:
        seen.discard(cu)

    xAs, xBs, yAs, yBs, zAs, zBs = zip(*{cube} | to_break)
    xs = sorted(set(xAs + xBs))
    ys = sorted(set(yAs + yBs))
    zs = sorted(set(zAs + zBs))
    N = 0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            for k in range(len(zs) - 1):
                new = (xs[i], xs[i + 1], ys[j], ys[j + 1], zs[k], zs[k + 1])

                if val == 'off' and intersect(new, cube):
                    seen.discard(new)

                elif val == 'on' and intersect(new, cube):
                    seen.add(new)

                elif any(intersect(old, new) for old in to_break):
                    seen.add(new)


def volume(xA, xB, yA, yB, zA, zB):
    return abs(xB - xA) * abs(yB - yA) * abs(zB - zA)


text = open(0).read()
cubes = {}
for line in text.splitlines():
    val = line.split()[0]
    xA, xB, yA, yB, zA, zB = [int(n) for n in re.findall(r'-?\d+', line)]
    cubes[xA, xB + 1, yA, yB + 1, zA, zB + 1] = val


seen = set()
for i, (cube, val) in enumerate(cubes.items(), 1):
    insert(cube, val)
    if i == 20:
        print(sum(volume(*cu) for cu in seen))
print(sum(volume(*cu) for cu in seen))
