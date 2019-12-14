import collections
import sys

from intcode import compute

from toolkit import render


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


text = sys.stdin.read()
print(len(get_panels(text, 0)))
print(render(get_panels(text, 1), brush=' #'))
