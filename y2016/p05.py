import itertools
import sys

import toolkit


text = sys.stdin.read().strip()
password1 = []
password2 = ['_' for _ in range(8)]
for i in itertools.count():
    strings = [f'{text}{1000 * i + k}' for k in range(1000)]
    for string, digest in toolkit.md5(strings):
        if digest.startswith('00000'):
            print(string, digest)
            password1.append(digest[5])
            if digest[5] in '01234567' and password2[int(digest[5])] == '_':
                password2[int(digest[5])] = digest[6]
    if len(password1) >= 8 and '_' not in password2:
        break
print(''.join(password1[:8]))
print(''.join(password2[:8]))
