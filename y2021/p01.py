ns = [int(n) for n in text.splitlines()]
ans1 = sum(b > a for a, b in zip(ns, ns[1:]))
ans2 = sum(sum(w[:-1]) < sum(w[1:]) for w in zip(ns, ns[1:], ns[2:], ns[3:]))
