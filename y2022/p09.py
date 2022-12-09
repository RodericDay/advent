def move(diff):
    dt = 0
    if max(abs(diff.real), abs(diff.imag)) > 1:
        dt += diff.real and diff.real / abs(diff.real)
        dt += diff.imag and (diff.imag / abs(diff.imag)) * 1j
    return dt


moves = dict(zip('LRUD', [-1, 1, -1j, 1j]))
state = {i: 0 for i in range(10)}
history = {i: set() for i in state}
for instruction in open(0).read().splitlines():
    k, v = instruction.split()
    for step in k * int(v):
        for i in state:
            state[i] += move(state[i - 1] - state[i]) if i else moves[k]
            history[i].add(state[i])

print(len(history[0]))
print(len(history[9]))
