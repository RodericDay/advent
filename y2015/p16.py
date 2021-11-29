known = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}
for line in df.read_text().splitlines():
    sue, N, *rest = re.findall(r'\w+', line)
    stuff = {k: int(v) for k, v in zip(rest[::2], rest[1::2])}
    if all(known[k] == stuff[k] for k in stuff):
        ans1 = N
    if all(
        known[k] < stuff[k] if k in {'cats', 'trees'}
        else known[k] > stuff[k] if k in {'pomeranians', 'goldfish'}
        else known[k] == stuff[k]
        for k in stuff):
        ans2 = N

