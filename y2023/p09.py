def historicize(ns):
    tails = [ns[-1]]
    while len(set(ns)) > 1:
        ns = [b - a for a, b in zip(ns, ns[1:])]
        tails.append(ns[-1])
    return sum(tails)


text = open(0).read()
data = [[int(n) for n in line.split()] for line in text.splitlines()]
print(sum(historicize(ns) for ns in data))
print(sum(historicize(ns[::-1]) for ns in data))
