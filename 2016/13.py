import re, hashlib, collections

# salt = 'abc'
salt = 'zpqevtbw'

found = set()
track = collections.defaultdict(list)
for n in range(23000):
    seed = '{}{}'.format(salt, n).encode()
    digest = hashlib.md5(seed).hexdigest()
    for _ in range(2016): digest = hashlib.md5(digest.encode()).hexdigest()
    try:
        f = re.search(r'([abcdef0-9])\1{4}', digest).group(1)
        for m in track[f]:
            if 0<(n-m)<=1000:
                found.add(m)
    except AttributeError:
        pass

    try:
        t = re.search(r'([abcdef0-9])\1{2}', digest).group(1)
        track[t].append(n)
    except AttributeError:
        pass

print(sorted(found)[63])
