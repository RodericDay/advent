import os

with open('25.txt') as fp:
    lines = fp.read().strip().splitlines()

transform = {
    'cpy': lambda i,x,y:  f'i += 1; {y} = {x}',
    'inc': lambda i,x:    f'i += 1; {x} += 1',
    'dec': lambda i,x:    f'i += 1; {x} -= 1',
    'jnz': lambda i,x,y:  f'i += {y} if {x}!=0 else 1',
    'out': lambda i,x:    f'i += 1; yield str({x})',
}

def run(a=0,c=0):
    code = f'def program(a={a},c={c}):\n\ti = 0\n\twhile 0 <= i < {len(lines)}:'
    for i, line in enumerate(lines):
        ins, *args = line.split()
        code += f'\n\t\tif i=={i}: ' + transform[ins](i,*args)
    code += '\n\tprint(a)'
    exec(code)
    return locals()['program']

for a in range(200):
    g = run(a)()
    c = ('01'[i%2] for i in range(100))
    for x,y in zip(g,c):
        if x!=y:
            break
    else:
        print(a)
