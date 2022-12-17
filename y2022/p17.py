from itertools import cycle


SCHEME = '''
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''


def generate_blocks(scheme):
    blocks = []
    for block in scheme.strip().split('\n\n'):
        blocks.append(set())
        lns = block.splitlines()
        for y, row in enumerate(lns[::-1]):
            for x, v in enumerate(row, 2):
                if v == '#':
                    blocks[-1].add(complex(x, y))
    return blocks


def play_tetris(width, gusts, blocks, lim=None):
    top = 0
    solid = {j for j in range(width)}
    contribs = []

    block_cycle = cycle(enumerate(blocks))
    gust_cycle = cycle(enumerate(gusts))
    states = {}

    gust_idx = None
    for block_idx, block in block_cycle:
        # position block 4 up from top
        block = {(p + 1j * top) + 4j for p in block}

        # identify cycle
        if lim is None:
            state = tuple(complex(x, top - dy) in solid for x in range(7) for dy in range(1))
            key = block_idx, gust_idx, state
            if key in states:
                cycle_idx = states.get(key)
                return contribs[:cycle_idx], contribs[cycle_idx:]
            states[key] = len(states)

        # play
        for gust_idx, gust in gust_cycle:
            # move sideways
            dx = {'<': -1, '>': 1}[gust]
            new = {p + dx for p in block}
            if not any(p in solid or p.real in {-1, width} for p in new):
                block = new

            # move down
            dy = -1j
            new = {p + dy for p in block}
            if any(p in solid for p in new):
                solid |= block
                break
            else:
                block = new

        contribs.append(int(max(abs(p.imag) for p in solid)) - top)
        top = sum(contribs)

        if len(contribs) == lim:
            return contribs


def main():
    width = 7
    gusts = open(0).read().strip()
    blocks = generate_blocks(SCHEME)

    contribs = play_tetris(width, gusts, blocks, lim=2022)
    print(sum(contribs))

    head, tail = play_tetris(width, gusts, blocks)
    N = 1_000_000_000_000 - len(head)
    print(sum(head) + sum(tail) * N // len(tail) + sum(tail[:N % len(tail)]))


main()
