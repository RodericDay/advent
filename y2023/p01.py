import re


def solve(text, digits):
    tot = 0
    rgx = '(' + '|'.join(digits) + ')'
    rgx = f'(?={rgx})'  # allow overlapping matches
    for ln in text.splitlines():
        ns = [digits.get(s, s) for s in re.findall(rgx, ln)]
        tot += 10 * ns[0] + ns[-1]
    print(tot)


text = open(0).read()
xs = {v: k for k, v in enumerate('0123456789')}
ys = {v: k for k, v in enumerate('zero one two three four five six seven eight nine'.split())}
solve(text, xs)
solve(text, xs | ys)
