def recurse(pending, opts, chain=tuple()):
    if pending == 0:
        yield chain
    else:
        for i, opt in enumerate(opts):
            yield from recurse(pending - opt, opts[i + 1:], chain + (opt,))


ns = sorted([int(n) for n in df.read_text().splitlines()], reverse=True)
opts = list(recurse(150, ns))
ans1 = len(opts)

min_n = min(map(len, opts))
ans2 = sum(len(opt) == min_n for opt in opts)
