import itertools


az = string.ascii_lowercase
trip = re.compile('|'.join(''.join(abc) for abc in zip(az, az[1:], az[2:])))
iol = re.compile(r'i|o|l')
dup = re.compile(r'(.)\1.*(.)\2')


def is_valid(code):
    return trip.search(code) and not iol.search(code) and dup.search(code)


def as_int(S):
    return sum((ord(c) - 97) % 26 * 26 ** i for i, c in enumerate(S[::-1]))


def as_str(N):
    return ''.join(chr(N // 26 ** i % 26 + 97) for i in range(8))[::-1]


code, = df.read_text().splitlines()
n = as_int(code)
generator = filter(is_valid, (as_str(n + i) for i in itertools.count()))
ans1 = next(generator)
ans2 = next(generator)
