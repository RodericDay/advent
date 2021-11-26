def pythonize(string):
    op, out = (
        re.sub(r'([a-z]+)', r'\1_', string)
        .replace('AND', '&')
        .replace('OR', '|')
        .replace('NOT ', '~')
        .replace('RSHIFT', '>>')
        .replace('LSHIFT', '<<')
    ).split(' -> ')
    return f'{out} = {op}'


def process(instructions, registers={}):
    while instructions:
        curr, *instructions = instructions
        out = curr.split()[0]
        if out in registers:
            continue
        try:
            exec(curr, None, registers)
        except NameError:
            instructions.append(curr)
    return registers


inp = [pythonize(string) for string in data_file.read_text().splitlines()]
found = process(inp.copy())
ans1 = found['a_']
ans2 = process(inp.copy(), {'b_': ans1})['a_']
