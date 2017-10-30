import itertools as it

def solve(password):
    '''
    Passwords must include one increasing straight of at least three letters,
        like abc, bcd, cde, and so on, up to xyz.
        They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can
        be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two pairs of letters, like aa, bb, or zz.
    '''
    as_bytes = [n-ord('a') for n in password.encode()]
    while True:
        as_bytes[-1] += 1
        for i in range(len(as_bytes)-1, -1, -1):
            if as_bytes[i] > 25:
                as_bytes[i] = 0
                as_bytes[i-1] += 1
        check = any(a+1==b and a+2==c and bytes([a, b ,c]).decode() != 'abd' for a, b, c in zip(as_bytes, as_bytes[1:], as_bytes[2:]))
        if not check:
            continue
        as_string = ''.join(chr(n+ord('a')) for n in as_bytes)
        if 'i' in as_string or 'o' in as_string or 'l' in as_string:
            continue
        pairs = list(i for i, (a, b) in enumerate(zip(as_string, as_string[1:])) if a==b)
        check = any(a+1!=b for a, b in zip(pairs, pairs[1:]))
        if not check:
            continue
        return as_string


ans = solve('cqjxjnds')
print(ans)

# finished #70
