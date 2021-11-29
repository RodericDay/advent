pre, seq = text.strip().split('\n\n')
formulas = re.findall(r'(\w+) => (\w+)', pre)


ans1 = len({
    seq[:match.start()] + seq[match.start():].replace(key, val, 1)
    for key, val in formulas
    for match in re.finditer(key, seq)
})


ops = formulas
ans2 = 0
while seq != 'e':
    ans2 += 1
    for k, v in ops:
        if v in seq:
            seq = seq.replace(v, k, 1)
            break
