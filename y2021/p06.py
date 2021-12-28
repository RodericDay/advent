states = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for n in open(0).read().split(','):
    states[0][int(n)] += 1

for day in range(256):
    states.append(states[-1][1:] + states[-1][:1])
    states[-1][6] += states[-2][0]

print(sum(states[80]))
print(sum(states[256]))
