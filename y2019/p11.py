import collections
import sys
from intcode import compute


def get_panels(ns, start):
    feedback = [start]
    iter_in = iter(feedback)
    robot = compute(ns, iter_in)

    pos, ori = 0, -1j
    panels = collections.defaultdict(int)
    for paint, instruction in zip(robot, robot):
        panels[pos] = paint
        ori *= 1j if instruction else -1j
        pos += ori
        feedback.append(panels[pos])
    return panels


def visualize(panels, brush):
    xmin, *_, xmax = sorted(int(p.real) for p in panels)
    ymin, *_, ymax = sorted(int(p.imag) for p in panels)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(brush[panels[complex(x, y)]], end='')
        print()


text = sys.stdin.read()
print(len(get_panels(text, 0)))
visualize(get_panels(text, 1), brush=' #')
