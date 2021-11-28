from itertools import permutations


places = set()
mapping = {}
for line in df.read_text().splitlines():
    A, _, B, _, val = line.split()
    places.update({A, B})
    mapping[A, B] = mapping[B, A] = int(val)


length = lambda combo: sum(mapping[pair] for pair in zip(combo, combo[1:]))
lengths = [length(combo) for combo in permutations(places)]
ans1 = min(lengths)
ans2 = max(lengths)
