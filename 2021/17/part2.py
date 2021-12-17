import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


def in_target(x, y, target):
    xmin, xmax, ymin, ymax = target

    return x >= xmin and x <= xmax and y >= ymin and y <= ymax


def beyond_target(x, y, target):
    _, xmax, ymin, _ = target

    return x > xmax or y < ymin


def reaches_target(vx_i, vy_i, target) -> bool:

    vx = int(vx_i)
    vy = int(vy_i)

    x = 0
    y = 0

    while not (in_target(x, y, target) or beyond_target(x, y, target)):
        x += vx
        if vx > 0:
            vx -= 1
        y += vy
        vy -= 1

    return in_target(x, y, target)


with open(f"{cur_dir}/input") as f:
    line = f.readline().strip()

xmin = int(line.split()[2].split(",")[0].split("=")[1].split("..")[0])
xmax = int(line.split()[2].split(",")[0].split("=")[1].split("..")[1])
ymin = int(line.split()[3].split("=")[1].split("..")[0])
ymax = int(line.split()[3].split("=")[1].split("..")[1])

target = (xmin, xmax, ymin, ymax)

vymax = abs(ymin) - 1
vymin = ymin
vxmax = xmax
vxmin = 1

count = 0
for vxi in range(vxmin, vxmax + 1):
    for vyi in range(vymin, vymax + 1):
        if reaches_target(vxi, vyi, target):
            print(f"{vxi}, {vyi}")

            count += 1

print(count)
