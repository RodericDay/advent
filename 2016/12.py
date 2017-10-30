with open('12.txt') as fp:
    lines = fp.read().strip().splitlines()

transforms = {
    'cpy': 'i +=1; {1} = {0}',
    'inc': 'i +=1; {0} += 1',
    'dec': 'i +=1; {0} -= 1',
    'jnz': 'i += {1} if {0}!=0 else 1; continue',
}

N = len(lines)
program = ['i=a=b=c=d=0']
program += ['c=1']
program += ['while 0 <= i < {N}:'.format_map(locals())]
for i, line in enumerate(lines):
    ins, *args = line.split(' ')
    code = transforms[ins].format(*args)
    program += ['\tif i=={i}: {code};'.format(i=i, code=code)]
program = '\n'.join(program+['print(a)'])

exec(program)
