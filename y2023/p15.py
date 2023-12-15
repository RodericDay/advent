import re


def hush(string):
    cv = 0
    for c in string:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv


text = open(0).read()
ans1 = sum(hush(step) for step in text.replace('\n', '').split(','))
print(ans1)


cases = [[] for _ in range(256)]
for label, op, val in re.findall(r'(\w+)(=|-)(\d*)', text):
    box = cases[hush(label)]
    old = [idx for idx, it in enumerate(box) if it[0] == label]
    match old, op, int(val or 0):
        case [idx], '-', 0: box.pop(idx)
        case [],    '=', n: box.append([label, n])
        case [idx], '=', n: box[idx] = [label, n]
ans2 = sum(i * j * lens[1] for i, slots in enumerate(cases, 1) for j, lens in enumerate(slots, 1))
print(ans2)
