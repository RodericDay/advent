ans1 = 0
ans2 = None
for i, char in enumerate(data_file.read_text(), 1):
    ans1 += {'(': 1, ')': -1}[char]
    if ans1 == -1 and ans2 is None:
        ans2 = i
