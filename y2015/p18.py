def condition(x, y, on):
    is_on = (x, y) in on
    neighbours_on = sum(
        (x + dx, y + dy) in on
        for dx in [1, 0, -1] for dy in [1, 0, -1]
        if dx or dy
    )
    return (is_on and neighbours_on in {2, 3}) or neighbours_on == 3


on1 = {
    (x, y)
    for y, ln in enumerate(df.read_text().splitlines())
    for x, ch in enumerate(ln)
    if ch == '#'
}
on2 = set(on1)
grid = {(x, y) for x in range(100) for y in range(100)}
corners = {(0, 0), (0, 99), (99, 0), (99, 99)}
for _ in range(100):
    on1 = {(x, y) for x, y in grid if condition(x, y, on1)}
    on2 = {(x, y) for x, y in grid if condition(x, y, on2)} | corners
ans1 = len(on1)
ans2 = len(on2)
