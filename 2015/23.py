d = {
    'inc': 'i += 1; {0} += 1',
    'hlf': 'i += 1; {0} //= 2',
    'tpl': 'i += 1; {0} *= 3',
    'jmp': 'i += {0}',
    'jie': 'i += {1} if {0}%2==0 else 1',
    'jio': 'i += {1} if {0}==1 else 1',
}

def to_python(string):
    ins, args = string.split(' ', 1)
    return d[ins].format(*args.split(', '))

with open('23.txt') as fp:
    instructions = list(map(to_python, fp.read().splitlines()))

i = a = b = 0
# a = 1
while 0 <= i < len(instructions):
    exec(instructions[i])
print(b)
