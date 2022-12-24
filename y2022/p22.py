import re


def render(grid):
    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)
    res = int(size % 9)
    for y in range(ymin, ymax + 1, res):
        for x in range(xmin, xmax + 1, res):
            print(grid.get(complex(x, y), ' '), end='')
        print()


def move_50_1(grid, pos, drx, size=50):
    pos += drx
    if grid.get(pos) is None:
        match pos.imag // size, pos.real // size, drx:
            case -1,  1, -1j: return pos + size *  3j, drx
            case -1,  2, -1j: return pos + size *  1j, drx
            case  0,  0, -1 : return pos + size *  2 , drx
            case  0,  3,  1 : return pos + size * -2 , drx
            case  1,  0, -1 : return pos + size *  1 , drx
            case  1,  0, -1j: return pos + size *  2j, drx
            case  1,  2,  1 : return pos + size * -1 , drx
            case  1,  2,  1j: return pos + size * -1j, drx
            case  2, -1, -1 : return pos + size *  2 , drx
            case  2,  2,  1 : return pos + size * -2 , drx
            case  3, -1, -1 : return pos + size *  1 , drx
            case  3,  1,  1 : return pos + size * -1 , drx
            case  3,  1,  1j: return pos + size * -3j, drx
            case  4,  0,  1j: return pos + size * -2j, drx
            case default: print('x', default)
    return pos, drx


def solve(inst, grid, teleport):
    pos = min(grid, key=lambda p: (p.real == 0, p.imag))
    drx = 1
    grid = grid.copy()
    for step in re.findall(r'(R|L|\d+)', inst):
        if step.isdigit():
            for _ in range(int(step)):
                grid[pos] = {1j: 'v', -1j: '^', -1: '<', 1: '>'}[drx]
                new, dr2 = teleport(grid, pos, drx)
                match grid[new]:
                    case '#':
                        break
                    case _:
                        pos, drx = new, dr2
        else:
            drx *= {'R': 1j, 'L': -1j}[step]
    render(grid)
    return 4 * int(pos.real + 1) + 1000 * int(pos.imag + 1) + {1: 0, 1j: 1, -1: 2, -1j: 3}[drx]


def main():
    global size
    text = open(0).read()
    src, inst = text.split('\n\n')
    grid = {complex(x, y): c for y, l in enumerate(src.splitlines())
                             for x, c in enumerate(l) if c in '.#'}
    size = (len(grid) // 6) ** 0.5
    print(solve(inst, grid, eval(f'move_{int(size)}_1')))
    # print(solve(inst, grid, eval(f'move_{int(size)}_2')))


main()
