import doctest
import itertools
import sys


def swap(text, a1, a2):
    if str(a1).isdigit():
        a1 = text[int(a1)]
    if str(a2).isdigit():
        a2 = text[int(a2)]
    return text.translate(str.maketrans(a1 + a2, a2 + a1))


def reverse(text, a1, a2):
    a1, a2 = int(a1), int(a2) + 1
    return text[:a1] + text[a1:a2][::-1] + text[a2:]


def rotate_left(text, n):
    return text[n:] + text[:n]


def rotate_right(text, n):
    return rotate_left(text, -n)


def rotate_based(text, c):
    n = text.index(c)
    if n >= 4:
        n += 1
    n += 1
    n %= len(text)
    return text[-n:] + text[:-n]


def move(text, a1, a2):
    c = text[a1]
    text = text[:a1] + text[a1 + 1:]
    return text[:a2] + c + text[a2:]


def scramble(text):
    '''
    >>> swap('abcde', 4, 0)
    'ebcda'
    >>> swap(_, 'd', 'b')
    'edcba'
    >>> reverse(_, 0, 4)
    'abcde'
    >>> rotate_left(_, 1)
    'bcdea'
    >>> move(_, 1, 4)
    'bdeac'
    >>> move(_, 3, 0)
    'abdec'
    >>> rotate_based(_, 'b')
    'ecabd'
    >>> rotate_based(_, 'd')
    'decab'
    '''
    for line in instructions:
        fn, *args = line.replace('rotate ', 'rotate_').split(' ')
        args = [int(c) if c.isdigit() else c for c in args if len(c) == 1]
        text = eval(fn)(text, *args)
    return text


instructions = sys.stdin.read().splitlines()
doctest.testmod()
print(scramble('abcdefgh'))

for perm in [''.join(seq) for seq in itertools.permutations('abcdefgh')]:
    if scramble(perm) == 'fbgdceah':
        print(perm)
