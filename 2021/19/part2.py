# Taken from output of part 1.

scanners = [
    (0, 0, 0),
    (-28, 1245, -161),
    (1163, 26, -170),
    (-1254, 90, -158),
    (-18, 1355, -1280),
    (1146, -1193, -28),
    (-2380, 15, -13),
    (-1078, 63, 1010),
    (-1105, 28, -1236),
    (-12, 2400, -1318),
    (-1075, 1190, -1385),
    (-2348, 173, -1313),
    (-2450, -1024, -26),
    (-3547, 0, -79),
    (-1233, -1211, 1144),
    (-1092, 1288, 1125),
    (-2449, 1277, -1238),
    (-2290, -2266, -141),
    (-4753, 30, -166),
    (-3532, 97, 1132),
    (-1224, 2573, 1061),
    (-2428, 1249, 1069),
    (-2269, -3556, -95),
    (-1131, -2278, -172),
    (-2337, -2411, 1197),
    (-4722, 31, 1198),
    (-6042, 159, -182),
    (-3560, 131, 2245),
    (-2385, -3457, 1117),
    (-2369, -4811, -22),
    (-1144, -3615, -89),
    (-4732, -17, 2315),
    (-5936, -1062, -10),
    (-2339, -3488, 2394),
    (-2334, -4684, 1017),
    (-3472, -3589, 2361),
    (-1256, -3495, 2220),
]

dist = max(
    [
        abs(a[0] - y[0]) + abs(a[1] - y[1]) + abs(a[2] - y[2])
        for a in scanners
        for y in scanners
    ]
)

print(dist)