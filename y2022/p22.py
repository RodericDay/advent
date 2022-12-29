import re


def transform(pos, drx, rotations, size, X, Y):
    x, y = pos.real % size, pos.imag % size
    for _ in range(rotations % 4):
        x, y = size - 1 - y, x
    return size * complex(X, Y) + complex(x, y), drx * 1j ** rotations


def wrap1(pos, drx, size):
    x, y = pos.real, pos.imag
    match x // 50, y // 50, drx:
        case  0,  0, -1 : return size *  2  + pos, -1
        case  0,  1, -1 : return size *  1  + pos, -1
        case  0,  1, -1j: return size *  2j + pos, -1j
        case  0,  4,  1j: return size * -2j + pos,  1j
        case  1,  3,  1 : return size * -1  + pos,  1
        case  1,  3,  1j: return size * -3j + pos,  1j
        case  1, -1, -1j: return size *  3j + pos, -1j
        case  2,  1,  1 : return size * -1  + pos,  1
        case  2,  1,  1j: return size * -1j + pos,  1j
        case  2,  2,  1 : return size * -2  + pos,  1
        case  2, -1, -1j: return size *  1j + pos, -1j
        case  3,  0,  1 : return size * -2  + pos,  1
        case -1,  2, -1 : return size *  2  + pos, -1
        case -1,  3, -1 : return size *  1  + pos, -1


def wrap2(pos, drx, size):
    x, y = pos.real, pos.imag
    match x // 50, y // 50, drx:
        case  0,  0, -1 : return transform(pos, drx,  2, size, 0, 2)
        case -1,  2, -1 : return transform(pos, drx,  2, size, 1, 0)
        case  1, -1, -1j: return transform(pos, drx,  1, size, 0, 3)
        case  2,  1,  1 : return transform(pos, drx, -1, size, 2, 0)
        case  0,  1, -1j: return transform(pos, drx,  1, size, 1, 1)
        case  1,  3,  1 : return transform(pos, drx, -1, size, 1, 2)
        case  2,  2,  1 : return transform(pos, drx,  2, size, 2, 0)
        case  1,  3,  1j: return transform(pos, drx,  1, size, 0, 3)
        case  0,  4,  1j: return transform(pos, drx,  0, size, 2, 0)
        case  0,  1, -1 : return transform(pos, drx, -1, size, 0, 2)
        case -1,  3, -1 : return transform(pos, drx, -1, size, 1, 0)
        case  2, -1, -1j: return transform(pos, drx,  0, size, 0, 3)
        case  2,  1,  1j: return transform(pos, drx,  1, size, 1, 1)
        case  3,  0,  1 : return transform(pos, drx,  2, size, 1, 2)


def main(text, v, wrap):
    *grid, _, path = text.splitlines()
    grid = {complex(x, y): c for y, l in enumerate(grid)
                             for x, c in enumerate(l) if c in '.#'}
    pos, drx = min(grid, key=lambda pos: (pos.imag, pos.real)), 1
    size = int((len(grid) / 6) ** 0.5)

    for move in re.findall(r'\d+|R|L', path):
        match move:
            case 'L':
                drx *= -1j
            case 'R':
                drx *= +1j
            case _:
                for _ in range(int(move)):
                    p, d = pos + drx, drx
                    if p not in grid:
                        p, d = wrap(p, d, size)
                    if grid[p] == '.':
                        pos, drx = p, d

    return int(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + [1, 1j, -1, -1j].index(drx))


text = open(0).read()

ans1 = main(text, 1, wrap1)
print(ans1)

ans2 = main(text, 2, wrap2)
print(ans2)
