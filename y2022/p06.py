text = open(0).read()
for N in [4, 14]:
    for i in range(len(text)):
        if len(set(text[i:i + N])) == N:
            break
    print(i + N)
