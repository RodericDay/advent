import re, itertools, collections

time = 2503
reindeer = {}
regexp = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds'
with open('14.txt') as fp:
    txt = fp.read()
    for name, *other in re.findall(regexp, txt):
        speed, t_flight, t_rest = map(int, other)
        reindeer[name] = itertools.cycle([speed for _ in range(t_flight)]+[0 for _ in range(t_rest)])

position = collections.Counter()
point_system = collections.Counter()
for _ in range(time):

    for name in reindeer:
        position[name] += next(reindeer[name])

    for name in reindeer:
        if max(position.values())==position[name]:
            point_system[name] += 1

print(max(position.values()))
print(max(point_system.values()))
