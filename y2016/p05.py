import itertools
import sys

import toolkit


text = sys.stdin.read().strip()
password1 = ['_' for _ in range(8)]
password2 = ['_' for _ in range(8)]
for i in itertools.count():
    digest = toolkit.md5(f'{text}{i}')
    if not digest.startswith('00000'):
        continue
    if '_' in password1:
        password1[password1.index('_')] = digest[5]
    if digest[5] in '01234567' and password2[int(digest[5])] == '_':
        password2[int(digest[5])] = digest[6]
    print(digest, ''.join(password1), ''.join(password2))
    if '_' not in password1 + password2:
        break
