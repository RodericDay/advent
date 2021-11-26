def checks1(string):
    yield len(re.findall(r'([aeiou])', string)) >= 3
    yield len(re.findall(r'(.)\1', string))
    yield len(re.findall(r'(ab|cd|pq|xy)', string)) == 0


def checks2(string):
    yield len(re.findall(r'(.)(.).*\1\2', string)) >= 1
    yield len(re.findall(r'(.).\1', string)) >= 1


ans1 = 0
ans2 = 0
for line in data_file.read_text().splitlines():
    ans1 += all(checks1(line))
    ans2 += all(checks2(line))
