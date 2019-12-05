import sys


text = sys.stdin.read()
ns = [int(s) for s in text.splitlines()]


def handle(n):
    m = n // 3 - 2
    return [m] + handle(m) if m > 0 else []


if __name__ == '__main__':
    print(sum(handle(n)[0] for n in ns))
    print(sum(sum(handle(n)) for n in ns))
