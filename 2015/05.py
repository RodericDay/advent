import re, collections

with open('05.txt') as fp:
    txt = fp.read()


def is_nice(string):
    yield len(re.findall(r'(a|e|i|o|u)', string)) >= 3
    yield any(a==b for a, b in zip(string, string[1:]))
    yield not any(sub in string for sub in ['ab','cd','pq','xy'])

def is_nice_v2(string):
    yield any(string[i:i+2]==string[j:j+2]
        for i in range(len(string))
        for j in range(i+2, len(string)))
    yield any(a==b for a, b in zip(string, string[2:]))

ans1 = 0
ans2 = 0
for line in txt.split():
    ans1 += all(is_nice(line))
    ans2 += all(is_nice_v2(line))

print(ans1)
print(ans2)
