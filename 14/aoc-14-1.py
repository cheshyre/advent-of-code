from hashlib import md5

def generate_hash(salt, input):
    return md5('{}{}'.format(salt, input).encode('utf-8')).hexdigest()

def get_first_triple(hash_str):
    for i in range(len(hash_str) - 2):
        if hash_str[i:i+3] == 3 * hash_str[i]:
            return hash_str[i]
    return None

def get_fives(hash_str):
    found_c = []
    for i in range(len(hash_str) - 4):
        if hash_str[i:i+5] == 5 * hash_str[i]:
            found_c.append(hash_str[i])
    return found_c

def finalize_hashes(char, potential_hashes, confirmed_hashes):
    for i in range(len(potential_hashes) - 1, -1, -1):
        if potential_hashes[i][0] == char:
            confirmed_hashes.append(potential_hashes[i][1])
            del potential_hashes[i]

potential_hashes = []
confirmed_hashes = []
hashstore = {}
index = 0
rollover_count = 0

salt = 'ngcjuoqr'

while len(confirmed_hashes) < 64 or rollover_count < 1000:
    if len(confirmed_hashes) >= 64:
        rollover_count += 1
    if index % 1000 == 0:
        print('Index: {} - Found hashes: {}'.format(index, len(confirmed_hashes)))
    new_hash = generate_hash(salt, index)
    hashstore[index] = new_hash
    c_triple = get_first_triple(new_hash)
    c_fives = get_fives(new_hash)
    for c in c_fives:
        finalize_hashes(c, potential_hashes, confirmed_hashes)
    if c_triple != None:
        potential_hashes.append([c_triple, index])
    potential_hashes = [x for x in potential_hashes if x[1] + 1000 > index]
    index += 1

print('The index producing the 64th key is {}.'.format(sorted(confirmed_hashes)[63]))
