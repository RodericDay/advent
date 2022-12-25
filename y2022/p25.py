def decode(string, swap={'1': 1, '=': -2, '-': -1, '0': 0, '2': 2}):
    return sum(5 ** i * swap[c] for i, c in enumerate(string[::-1]))


def base5(n):
    ns = []
    while n:
        ns.append(n % 5)
        n //= 5
    return ns[::-1]


def encode(n, swap={1: '1', -2: '=', -1: '-', 0: '0', 2: '2'}):
    ms = []
    carry = 0
    for n in base5(n)[::-1]:
        n += carry
        if n > 2:
            carry, value = 1, n % 3 - 2
        else:
            carry, value = 0, n
        ms.append(swap[value])
    if carry:
        ms.append(swap[carry])
    return ''.join(ms[::-1])


n = sum(map(decode, open(0).read().splitlines()))
print(encode(n))
