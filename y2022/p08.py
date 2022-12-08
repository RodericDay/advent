from itertools import count, takewhile



def heights(t, dt):
    return takewhile(lambda h: h is not None, (grid.get(t + dt * i) for i in count(1)))


def is_visible(t):
    return any(grid[t] > max(heights(t, dt), default=-1) for dt in udlr)


def score(t):
    score = 1
    for dt in udlr:
        count = 0
        for h in heights(t, dt):
            count += 1
            if h >= grid[t]:
                break
        score *= count
    return score


udlr = [-1j, 1j, -1, 1]
text = open(0).read()
grid = {complex(x, y): int(v) for y, line in enumerate(text.splitlines(), 1) for x, v in enumerate(line, 1)}

ans1 = sum(is_visible(t) for t in grid)
print(ans1)

ans2 = max(score(t) for t in grid)
print(ans2)
