import sys


def shuffle(text, L, P):
    cards = list(range(L))
    for line in text.splitlines():
        inst, n = line.rsplit(' ', 1)
        if inst == 'deal with increment':
            n = int(n)
            invmod = pow(n, -1, L)  # pow(n, L - 2, L)
            source = lambda i: i * invmod % L  # noqa
        elif inst == 'cut':
            n = int(n)
            source = lambda i: (i + n) % L  # noqa
        elif inst == 'deal into new':
            source = lambda i: (L - 1 - i) % L  # noqa
        cards = [cards[source(i)] for i in range(L)]
    return cards.index(P)


text = sys.stdin.read()
print(shuffle(text, 10007, 2019))
