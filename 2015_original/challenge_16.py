import re
import operator

ticket = {
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

text = open('challenge_16.txt').read().strip().split('\n')
comparison = {}
comparison['cats'] = comparison['trees'] = operator.gt
comparison['pomeranians'] = comparison['goldfish'] = operator.lt
for line in text:
    aunt, pairs = line.replace(' ', '').split(':', 1)
    data = {k:int(v) for pair in pairs.split(',') for k, v in [pair.split(':')]}
    if all(comparison.get(k, operator.eq)(data[k], ticket[k]) for k in ticket if k in data):
        print(aunt)
