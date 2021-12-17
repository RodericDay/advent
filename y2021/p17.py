import re


text = open(0).read()
x1, x2, y1, y2 = [int(n) for n in re.findall(r'-?\d+', text)]
peaks = []
for vyi in range(-100, 100):
    for vxi in range(0, 400):
        x, y, vx, vy = 0, 0, vxi, vyi
        for _ in range(200):
            x += vx
            y += vy
            vx -= vx // abs(vx) if vx else 0
            vy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                peaks.append(vyi * (vyi + 1) // 2)
                break
            if x > x2:
                break
print(max(peaks))
print(len(peaks))
