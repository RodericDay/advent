import json, re

with open('12.txt') as fp:
    obj = json.load(fp)

ans = 0
while obj:
    sub = obj.pop()
    if isinstance(sub, dict):
        # if 'red' in sub.values(): continue
        obj.extend(sub.values())
    elif isinstance(sub, list):
        obj.extend(sub)
    elif isinstance(sub, int):
        ans += sub
print(ans)
