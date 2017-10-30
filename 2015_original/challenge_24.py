import itertools
import operator
import functools
import json

def quantum_entanglement(group):
    return functools.reduce(operator.mul, group)

def partitions(value, options, options_sorted=False):
    if not options_sorted:
        options = sorted(options, reverse=True)
    for i, option in enumerate(options):
        rem = value-option
        if rem==0:
            yield [option]
        elif rem>0:
            for tail in partitions(rem, options[i+1:]):
                yield [option] + tail

values = {1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113}
# values = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}
weight = sum(values)//4
possible = list(partitions(weight, values))
minimal = min(map(len, possible))
ans = all_min = [c for c in possible if len(c)==minimal]
if len(all_min) > 1:
    ans = [min(all_min, key=quantum_entanglement)]
print(quantum_entanglement(ans[0]))
