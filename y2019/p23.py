import collections
import sys
import threading

from intcode import compute


def communicate(n):
    yield n
    while True:
        while queues[n]:
            yield queues[n].popleft()
        yield -1


def handle(n):
    bot = compute(text, communicate(n))
    for addr, X, Y in zip(bot, bot, bot):
        if addr == 255:
            NAT.append((X, Y))
        else:
            queues[addr].extend((X, Y))


text = sys.stdin.read()

queues = collections.defaultdict(collections.deque)
NAT = []
for n in range(50):
    threading.Thread(target=handle, args=[n], daemon=True).start()

seen = set()
while True:
    activity = sum(len(q) for q in queues.values())
    if not activity and len(NAT):
        X, Y = NAT[-1]

        if len(NAT) == 1:
            print(Y)

        if Y in seen:
            print(Y)
            break

        queues[0] += [X, Y]
        seen.add(Y)
