# I wrote this while the previous part 2 solution was still solving the problem.
# The difference in performance is massive.

def remove(array, even):
    if even:
        mod = 2
    else:
        mod = 1
    return [array[i] for i in range(len(array)) if i % 3 == mod]

num_elves = 3014387

elves = [i + 1 for i in range(num_elves)]

while len(elves) > 1:
    midpoint = int(len(elves) / 2)
    preserved_array = elves[:midpoint]
    to_prune_array = elves[midpoint:]
    pruned_array = remove(to_prune_array, len(elves) % 2 == 0)
    pivot_index = len(to_prune_array) - len(pruned_array)
    elves = preserved_array[pivot_index:] + pruned_array + preserved_array[:pivot_index]

print('The elf with all the presents at the end is elf {}.'.format(elves[0]))
