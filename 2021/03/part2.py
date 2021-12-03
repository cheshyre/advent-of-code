import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    numbers = [x.strip() for x in f]
    
count_ones = []
for i in range(len(numbers[0])):
    count = 0
    for x in numbers:
        if x[i] == "1":
            count += 1
    count_ones.append(count)
    
count_zeros = [len(numbers) - x for x in count_ones]

oxygen_numbers = list(numbers)
index = 0
while len(oxygen_numbers) > 1 and index < len(oxygen_numbers[0]):
    print(oxygen_numbers)
    
    count_ones = []
    for i in range(len(oxygen_numbers[0])):
        count = 0
        for x in oxygen_numbers:
            if x[i] == "1":
                count += 1
        count_ones.append(count)
        
    count_zeros = [len(oxygen_numbers) - x for x in count_ones]
    
    if count_ones[index] >= count_zeros[index]:
        oxygen_numbers = [x for x in oxygen_numbers if x[index] == "1"]
    else:
        oxygen_numbers = [x for x in oxygen_numbers if x[index] == "0"]
    index += 1
print(oxygen_numbers)
    
count_ones = []
for i in range(len(numbers[0])):
    count = 0
    for x in numbers:
        if x[i] == "1":
            count += 1
    count_ones.append(count)
    
count_zeros = [len(numbers) - x for x in count_ones]

co2_numbers = list(numbers)
index = 0
while len(co2_numbers) > 1 and index < len(co2_numbers[0]):
    print(co2_numbers)
    
    count_ones = []
    for i in range(len(co2_numbers[0])):
        count = 0
        for x in co2_numbers:
            if x[i] == "1":
                count += 1
        count_ones.append(count)
        
    count_zeros = [len(co2_numbers) - x for x in count_ones]
    
    if count_ones[index] < count_zeros[index]:
        co2_numbers = [x for x in co2_numbers if x[index] == "1"]
    else:
        co2_numbers = [x for x in co2_numbers if x[index] == "0"]
    index += 1

print(co2_numbers)
    
print(oxygen_numbers[0])
print(co2_numbers[0])

print(int(oxygen_numbers[0], 2) * int(co2_numbers[0], 2))
