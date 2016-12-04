import re

def down(string):
    '''
    >>> down('""')
    (2, 0)
    >>> down('"abc"')
    (5, 3)
    >>> down('"aaa\\\\"aaa"')
    (10, 7)
    >>> down('"\\\\x27"')
    (6, 1)
    '''
    return len(string), len(eval(string))

def up(string):
    '''
    >>> up('""')
    (2, 6)
    >>> up('"abc"')
    (5, 9)
    >>> up('"aaa\\\\"aaa"')
    (10, 16)
    >>> up('"\\\\x27"')
    (6, 11)
    '''
    new_string = '"'+(string
        .replace('\\', '\\\\')
        .replace('"', '\\"')
    )+'"'
    return len(string), len(new_string)


ans1, ans2 = 0, 0
with open('08.txt') as fp:
    for line in fp.read().strip().split('\n'):
        a, b = down(line)
        ans1 += a - b

        c, d = up(line)
        ans2 += d - c

print(ans1)
print(ans2)
