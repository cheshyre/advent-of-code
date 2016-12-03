from sys import argv

filename = argv[1]

num_valid = 0
with open(filename) as f:
    while True:
        triangles = [[], [], []]
        for i in range(3):
            try:
                s = next(f)
            except:
                print(num_valid)
                exit(0)
            numbers = [int(x) for x in s.split()]
            triangles[0].append(numbers[0])
            triangles[1].append(numbers[1])
            triangles[2].append(numbers[2])
        for x in triangles:
            x.sort()
            if x[0] + x[1] > x[2]:
                num_valid += 1

print(num_valid)



