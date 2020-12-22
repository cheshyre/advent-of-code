import os


def parse_line(line):
    ingredients = line.strip().split(" (")[0].split()
    allergens = " ".join(line.strip().split(" (")[1].split(")")[0].split()[1:]).split(", ")
    return ingredients, allergens


cur_dir = os.path.dirname(os.path.abspath(__file__))

ingredients_sets = []
allergen_appearance_dict = {}
possible_allergen_ingredients = set()
with open(f"{cur_dir}/input") as f:
    for i, line in enumerate(f):
        ingredeints, allergens = parse_line(line)
        ingredients_sets.append(set(ingredeints))
        for a in allergens:
            if a in allergen_appearance_dict:
                allergen_appearance_dict[a].append(i)
            else:
                allergen_appearance_dict[a] = [i]
                
full_ingredients = set()
for x in ingredients_sets:
    full_ingredients = full_ingredients.union(x)

allergen_responsibility_dict = {}
for allergen in allergen_appearance_dict:
    locations = allergen_appearance_dict[allergen]
    ingreds_responsible = set(ingredients_sets[locations[0]])
    for loc in locations[1:]:
        ingreds_responsible = ingreds_responsible.intersection(ingredients_sets[loc])
    allergen_responsibility_dict[allergen] = ingreds_responsible
    possible_allergen_ingredients = possible_allergen_ingredients.union(ingreds_responsible)

print(possible_allergen_ingredients)
nonallergen_ingreds = full_ingredients.difference(possible_allergen_ingredients)
print(nonallergen_ingreds)

print(allergen_responsibility_dict)
final_allergen_responsibility_dict = {}
target_size = len(allergen_responsibility_dict)
while len(final_allergen_responsibility_dict) != target_size:
    for allergen in allergen_responsibility_dict:
        if len(allergen_responsibility_dict[allergen]) == 1:
            ingred = allergen_responsibility_dict[allergen].pop()
            final_allergen_responsibility_dict[allergen] = ingred
    
    for allergen in final_allergen_responsibility_dict:
        if allergen in allergen_responsibility_dict:
            del allergen_responsibility_dict[allergen]
    
    for _, ingred in final_allergen_responsibility_dict.items():
        for _, someset in allergen_responsibility_dict.items():
            if ingred in someset:
                someset.remove(ingred)
    
    print(allergen_responsibility_dict)
    print(final_allergen_responsibility_dict)
    
sorted_allergens = sorted([x for x in final_allergen_responsibility_dict])
sorted_ingreds = [final_allergen_responsibility_dict[x] for x in sorted_allergens]
print(",".join(sorted_ingreds))

