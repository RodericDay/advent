    a = '10011111011011001'
    target = 35651584

    t = str.maketrans('01', '10')
    while True:
        b = a[::-1].translate(t)
        a = a + '0' + b
        if len(a) >= target: break

    a = a[:target]

    def get_checksum(string):
        while len(string) % 2 != 1:
            string = ''.join('1' if a==b else '0' for a,b in zip(string[::2], string[1::2]))
        return string

    print(get_checksum(a))
