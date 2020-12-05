import sys


def unzip_len(text, recurse=False):
    ptr = 0
    size = 0
    while ptr < len(text):
        if text[ptr] == '(':
            ptr += 1

            l1 = ptr + text[ptr:].index('x')
            l2 = ptr + text[ptr:].index(')')
            span = int(text[ptr:l1])
            repeat = int(text[l1 + 1:l2])

            l3 = l2 + 1
            l4 = l3 + span
            frag = text[l3:l4]
            length = unzip_len(frag, True) if recurse else len(frag)

            ptr = l4
            size += int(repeat) * length

        else:
            ptr += 1
            size += 1

    return size


text = sys.stdin.read().strip()

# ans1 = unzip_len(text)
# print(ans1)

ans2 = unzip_len(text, recurse=True)
print(ans2)
