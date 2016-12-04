import itertools
import hashlib

key = 'yzbqklnj'

for n in itertools.count():
    seed = '{}{}'.format(key, n).encode()
    md5 = hashlib.md5()
    md5.update(seed)
    string = ''.join('{:0>2x}'.format(c) for c in md5.digest())
    if string.startswith('00000'):
        print(n, string)
    if string.startswith('000000'):
        print(n, string)
        break
