ans1 = ans2 = 0
for line in text.splitlines():
    seqs = [frozenset(seq) for seq in re.findall(r'\w+', line)]
    _1,_7,_4, *pending,_8 = sorted(set(seqs), key=len)
    sorter = lambda x: [len(x &_8), len(x &_4), len(x &_1)]
    _2,_5,_3,_6,_0,_9 = sorted(pending, key=sorter)
    ns = [_0,_1,_2,_3,_4,_5,_6,_7,_8,_9]
    ans1 += sum(x in {_1, _7, _4, _8} for x in seqs[-4:])
    ans2 += int(''.join(str(ns.index(x)) for x in seqs[-4:]))
