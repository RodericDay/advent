inp = data_file.read_text().strip()
out = {}
for a in [''] + list(string.ascii_lowercase):
    text = inp.replace(a, '').replace(a.swapcase(), '')
    stack1 = list(text)
    stack2 = []
    while stack1:
        x = stack1.pop()
        if stack2 and x.swapcase() == stack2[-1]:
            y = stack2.pop()
        else:
            stack2.append(x)
    out[a] = len(stack2)
ans1 = out['']
ans2 = min(out.values())
