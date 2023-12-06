text = open(0).read()

cards = []
for line in text.splitlines():
    ns, ms = [[int(n) for n in line.strip().split()] for line in line.split(':')[1].split('|')]
    cards.append(len(set(ns) & set(ms)))
print(sum(2 ** (n - 1) for n in cards if n))

counter = [1 for _ in cards]
for i, n in enumerate(cards):
    for j in range(i + 1, i + 1 + n):
        counter[j] += counter[i]
print(sum(counter))
