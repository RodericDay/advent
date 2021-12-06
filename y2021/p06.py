states = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
for n in text.split(','):
    states[0][int(n)] += 1

for day in range(256):
    states.append(states[-1][1:] + states[-1][:1])
    states[-1][6] += states[-2][0]

ans1 = sum(states[80])
ans2 = sum(states[256])
