def render(grid, brush):
    if isinstance(brush, str):
        brush = {i: c for i, c in enumerate(brush)}
    xmin, *_, xmax = sorted(int(p.real) for p in grid)
    ymin, *_, ymax = sorted(int(p.imag) for p in grid)
    brush[None] = ' '
    rendered = ''
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            rendered += brush[grid.get(complex(x, y))]
        rendered += '\n'
    return rendered


def bsearch(fn, goal, lo, hi):
    while hi - lo > 1:
        mid = lo + (hi - lo) // 2
        if goal < fn(mid):
            lo, hi = lo, mid
        else:
            lo, hi = mid, hi

    # check
    a, b = fn(lo), fn(hi)
    assert a <= goal, 'lower bound too high'
    assert goal <= b, 'higher bound too low'

    return lo
