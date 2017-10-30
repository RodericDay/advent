import re, collections

with open('23.txt') as fp:
    lines = fp.read().strip().splitlines()

def handle(line):
    ins, *args = line.split(' ')
    if len(args)==1:
        if ins == 'inc':
            new = line.replace(ins, 'dec')
        else:
            new = line.replace(ins, 'inc')
    else:
        if ins == 'jnz':
            new = line.replace(ins, 'cpy')
        else:
            new = line.replace(ins, 'jnz')
    return new


transforms = {
    'cpy': '',
    'inc': 'i +=1; {0} += 1',
    'dec': '',
    'jnz': '',
}

r = {}
r['a'] = 7
for n in range(10000):
    r[str(n)] = n
    r[str(-n)] = -n
i = 0
C = collections.Counter()
while 0 <= i < len(lines):
    C[i] += 1
    ins, *args = lines[i].split(' ')
    if i==None:
        r['a'] = r['b']*r['d']
        r['c'] = 0
        r['d'] = 0
        i = 10
    elif ins=='cpy':
        r[args[1]] = r[args[0]]
        i += 1
    elif ins=='tgl':
        try:
            j = i + r[args[0]]
            lines[j] = handle(lines[j])
            i += 1
        except IndexError:
            i += 1
    elif ins=='dec':
        i +=1
        r[args[0]] -= 1
    elif ins=='inc':
        i += 1
        r[args[0]] += 1
    elif ins=='jnz':
        i += r[args[1]] if r[args[0]]!=0 else 1
    else:
        raise Exception(ins, args)

print(C.most_common())
print('\n'.join(lines))
print(r['a'])
