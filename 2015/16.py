import re, json

sues = {}
with open('16.txt') as fp:
    for line in fp.read().strip().split('\n'):
        name, data = line.split(': ', 1)
        sues[name] = {k:int(v) for k,v in re.findall(r'(\w+): (\d+)',data)}

goal = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1,
}

def check(data):
    for key in data:
        if key in ['trees','cats']:
            yield data[key] > goal[key]
        elif key in ['pomeranians','goldfish']:
            yield data[key] < goal[key]
        else:
            yield data[key] == goal[key]

for name, data in sues.items():
    if all(check(data)):
        print(name)
