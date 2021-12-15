from collections import Counter


def sum_counts(counts):
    """
    >>> sum_counts([('a', 20), ('b', 10), ('a', 30)])
    {'a': 50, 'b': 10}
    """
    final = Counter()
    for k, v in counts:
        final[k] += v
    return final


polymer, eqs = open(0).read().split('\n\n')
mapping = dict(eq.split(' -> ') for eq in eqs.splitlines())
grow = {(a, b): ((a, x), (x, b)) for (a, b), x in mapping.items()}

duos = Counter(duo for duo in zip(polymer, polymer[1:]))
scores = {}
for n in range(40):
    duos = sum_counts((new, N) for old, N in duos.items() for new in grow[old])

    # account for double-counting when scoring, except at edges
    singles = sum_counts((k, N) for ab, N in duos.items() for k in ab)
    singles[polymer[0]] += 1
    singles[polymer[-1]] += 1
    xmax, *_, xmin = [N // 2 for _, N in singles.most_common()]
    scores[n + 1] = xmax - xmin
print(scores[10])
print(scores[40])
