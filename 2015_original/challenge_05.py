'''
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
'''

def nice(string):
    # three vowels
    A = len(string) - len([c for c in string if c not in 'aeiou']) >= 3
    # twice in a row
    B = any(a==b for a, b in zip(string, string[1:]))
    # excludes
    C = not any(pair in string for pair in ['ab','cd','pq','xy'])
    return A and B and C

def real_nice(string):
    A = False
    seen = set()
    last = None
    for pair in zip(string, string[1:]):
        if pair in seen:
            A = True
            break
        if last: seen.add(last)
        last = pair
    B = any(a==b for a, b in zip(string, string[2:]))
    return A and B

ans = 0
ans2 = 0
for line in open('challenge_05.txt'):
    string = line.strip()
    ans += nice(string)
    ans2 += real_nice(string)
print(ans)
print(ans2)
