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

gamma = ""
eps = ""
for i in range(len(numbers[0])):
    if count_ones[i] > count_zeros[i]:
        gamma += "1"
        eps += "0"
    else:
        eps += "1"
        gamma += "0"
        
eps_int = int(eps, 2)
gamma_int = int(gamma, 2)

print(gamma_int * eps_int)