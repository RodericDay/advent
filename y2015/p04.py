import sys
from hashlib import md5
from multiprocessing import Pool


def mine(code, i):
    hasher = md5()
    hasher.update(f'{code}{i}'.encode())
    return i, hasher.hexdigest()


if __name__ == '__main__':
    code = sys.stdin.read().strip()
    ans1 = None
    ans2 = None
    with Pool() as pool:
        for i, coin in pool.starmap(mine, [(code, i) for i in range(10**7)]):
            if ans1 is None and coin.startswith('00000'):
                ans1 = i
            if ans2 is None and coin.startswith('000000'):
                ans2 = i
    print(ans1)
    print(ans2)
