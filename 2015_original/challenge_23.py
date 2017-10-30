lines = open('challenge_23.txt').read().strip().split('\n')

a, b = 1, 0
idx = 0
while True:

    try:
        line = lines[idx]
    except IndexError:
        break

    try:
        instruction, register = line.split(' ')

    except ValueError:
        instruction, data = line.split(' ', 1)
        register, offset = data.split(', ')

    if instruction=='hlf':
        locals()[register] //= 2
        idx += 1

    elif instruction=='jio':
        if locals()[register] == 1:
            idx += int(offset)
        else:
            idx += 1

    elif instruction=='jie':
        if locals()[register] % 2 == 0:
            idx += int(offset)
        else:
            idx += 1

    elif instruction=='inc':
        locals()[register] += 1
        idx += 1

    elif instruction=='tpl':
        locals()[register] *= 3
        idx += 1

    elif instruction=='jmp':
        idx += int(register)

    else:
        raise RuntimeError("Unknown instruction "+instruction)

print(a, b)
