from sys import argv

filename = argv[1]

num_valid = 0
with open(filename) as f:
    while True:
        try:
            s = next(f)
        except:
            break
        numbers = [int(x) for x in s.split()]
        numbers.sort()
        if numbers[0] + numbers[1] > numbers[2]:
            num_valid += 1

print(num_valid)



