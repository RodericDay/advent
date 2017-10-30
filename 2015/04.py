import itertools
import hashlib

salt = 'yzbqklnj'

for n in itertools.count():
    seed = '{}{}'.format(salt, n).encode()
    digest = hashlib.md5(seed).hexdigest()
    if digest.startswith('00000'):
        print(n, digest)
    if digest.startswith('000000'):
        break
