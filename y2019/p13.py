import collections
import sys

from intcode import compute


def arkanoid(text):
    grid = {}
    joy = []
    bot = compute(text, iter(joy))
    paddle_x = 0
    score = 0
    for x, y, tile_id in zip(bot, bot, bot):
        if [x, y] == [-1, 0]:
            score = tile_id
        else:
            grid[complex(x, y)] = tile_id
            if tile_id == 3:
                paddle_x = x
            if tile_id == 4:
                if x > paddle_x:
                    joy.append(1)
                elif x < paddle_x:
                    joy.append(-1)
                else:
                    joy.append(0)
    return grid, score


text = sys.stdin.read()
grid, _ = arkanoid(text)
print(collections.Counter(grid.values())[2])

_, score = arkanoid('2' + text[1:])
print(score)
