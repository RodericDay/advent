from itertools import accumulate as acc


text = data_file.read_text()
dirs = dict(zip('<>^v', [-1, 1, -1j, 1j]))
ans1 = len({*acc(map(dirs.get, text))})
ans2 = len({*acc(map(dirs.get, text[::2])), *acc(map(dirs.get, text[1::2]))})
