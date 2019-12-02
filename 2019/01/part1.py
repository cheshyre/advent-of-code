import fuel_calculator


with open("input") as f:
    module_masses = [int(line.strip()) for line in f]

total_fuel_needed = sum(
    [
        fuel_calculator.get_fuel_needed(module_mass)
        for module_mass in module_masses
    ]
)

print(total_fuel_needed)
