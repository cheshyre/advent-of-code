import os


cur_dir = os.path.dirname(os.path.abspath(__file__))


def evaluate_x_fold(pts, x_pivot):
    new_pts = []

    for pt in pts:
        x, y = pt
        if x < x_pivot:
            new_pts.append(pt)
        elif x == x_pivot:
            continue
        else:
            new_x = x_pivot - (x - x_pivot)
            new_pts.append((new_x, y))

    return new_pts


def evaluate_y_fold(pts, y_pivot):
    new_pts = []

    for pt in pts:
        x, y = pt
        if y < y_pivot:
            new_pts.append(pt)
        elif y == y_pivot:
            continue
        else:
            new_y = y_pivot - (y - y_pivot)
            new_pts.append((x, new_y))

    return new_pts


def evaluate_fold(pts, fold):
    axis = fold.split("=")[0]
    val = int(fold.split("=")[1])

    if axis == "x":
        return evaluate_x_fold(pts, val)
    elif axis == "y":
        return evaluate_y_fold(pts, val)
    else:
        raise Exception()


pts = []
folds = []
with open(f"{cur_dir}/input") as f:
    line = f.readline()
    phase2 = False
    while line:
        if not phase2:
            if line.strip() != "":
                pts.append(
                    (int(line.strip().split(",")[0]), int(line.strip().split(",")[1]))
                )
            else:
                phase2 = True
        else:
            folds.append(line.strip().split()[-1])
        line = f.readline()

print(pts)
print(folds)

for fold in folds:
    pts = evaluate_fold(pts, fold)
    pts = list(set(pts))


x_max = max([x for x, _ in pts])
y_max = max([y for _, y in pts])

pts = set(pts)

for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (x, y) in pts:
            print("#", end="")
        else:
            print(".", end="")
    print("")
