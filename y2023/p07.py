import collections


def strength(hand, order, J_swap='J'):
    counter = collections.Counter(hand.replace('J', J_swap))
    count = collections.Counter(counter.values())
    return [count[n] for n in [5, 4, 3, 2, 1]] + [order.index(k) for k in hand]


text = open(0).read()
data = [ln.split() for ln in text.splitlines()]

order = '123456789TJQKA'
hands = [(strength(hand, order), hand, score) for hand, score in data]
print(sum(rank * int(score) for rank, (_, hand, score) in enumerate(sorted(hands), 1)))

order = 'J123456789TQKA'
hands = [(max(strength(hand, order, J_swap) for J_swap in order[1:]), hand, score) for hand, score in data]
print(sum(rank * int(score) for rank, (_, hand, score) in enumerate(sorted(hands), 1)))
