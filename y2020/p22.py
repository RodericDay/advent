import sys


def game(stack1, stack2, rec=False, N=1):
    seen = set()
    key = None
    while stack1 and stack2:
        key = (tuple(stack1), tuple(stack2))
        a, b = stack1.pop(), stack2.pop()
        if rec and key in seen:
            return 0
        elif rec and a <= len(stack1) and b <= len(stack2):
            p2won = game(stack1[-a:], stack2[-b:], rec=rec, N=N + 1)
        else:
            p2won = b > a
        seen.add(key)
        winner = stack2 if p2won else stack1
        order = [a, b] if p2won else [b, a]
        winner[:] = order + winner
    return sum(i * n for i, n in enumerate(winner, 1)) if N == 1 else p2won


text = sys.stdin.read()
p1, p2 = text.split('\n\n')
stack1 = [int(n) for n in p1.splitlines()[1:]][::-1]
stack2 = [int(n) for n in p2.splitlines()[1:]][::-1]
print(game(stack1[:], stack2[:]))
print(game(stack1[:], stack2[:], rec=True))
