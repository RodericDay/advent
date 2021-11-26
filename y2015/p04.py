from hashlib import md5
from multiprocessing import Pool


def mine(code, i):
    hasher = md5()
    hasher.update(f'{code}{i}'.encode())
    return i, hasher.hexdigest()


code = data_file.read_text().strip()
ans1 = None
ans2 = None
for i in range(10**7):
    i, coin = mine(code, i)
    if ans1 is None and coin.startswith('00000'):
        ans1 = i
    if ans2 is None and coin.startswith('000000'):
        ans2 = i
        break
