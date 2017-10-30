import re

ans1 = 0
ans2 = 0
with open('02.txt') as fp:
    for line in fp:
        w, h, l = map(int, re.findall(r'\d+', line))
        # 1
        areas = (w*h, h*l, w*l)
        ans1 += 2*sum(areas)+min(areas)
        # 2
        vol = w*h*l
        per = 2*min(w+h, h+l, w+l)
        ans2 += per + vol

print(ans1)
# print(ans2)

def area_present(l, w, h):
    gift_area = 2*l*w + 2*w*h + 2*h*l
    if (l*w < w*h and l*w < h*l):
        gift_area += l*w
    elif (w*h < l*w and w*h < h*l):
        gift_area += w*h
    elif (h*l < l*w and h*l < w*h):
        gift_area += h*l
    else:
        raise Exception(l,w,h)
    return (gift_area)


with open('02.txt') as fp:
    total_paper = 0
    for line in fp:
        words = line.split('x')
        a = int(words[0])
        b = int(words[1])
        c = int(words[2])

        a_gift = area_present(a, b, c)
        total_paper += a_gift

    print (total_paper)
