ns = [int(n) for n in open(0)]
print(sum(b > a for a, b in zip(ns, ns[1:])))
print(sum(sum(w[:-1]) < sum(w[1:]) for w in zip(ns, ns[1:], ns[2:], ns[3:])))
