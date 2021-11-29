import collections
import itertools


happiness = collections.defaultdict(int)
people = set()
for line in df.read_text().splitlines():
    A, verb, N, B = re.findall(r'([A-Z][a-z]+|gain|lose|\d+)', line)
    happiness[A, B] = int(N) if verb == 'gain' else -int(N)
    people.update({A, B})


def calc(seq):
    return sum(happiness[b, a] + happiness[b, c]
        for a, b, c in zip(seq[-1:] + seq[:-1], seq, seq[1:] + seq[:1])
    )


ans1 = max(calc(combo) for combo in itertools.permutations(people))
ans2 = max(calc(combo) for combo in itertools.permutations(people | {'me'}))
