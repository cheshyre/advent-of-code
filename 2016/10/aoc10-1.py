from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

bots = {}

def bot_action(bot_id):
    if 61 in bots[bot_id][1] and 17 in bots[bot_id][1]:
        print('Found: {}'.format(bot_id))
    if len(bots[bot_id][1]) != 2:
        raise Exception("Bot {} does not have 2 chips.".format(bot_id))
    if 'b' in bots[bot_id][0][0]:
        bots[bots[bot_id][0][0]][1].append(min(bots[bot_id][1]))
        if len(bots[bots[bot_id][0][0]][1]) >= 2:
            bot_action(bots[bot_id][0][0])
    if 'b' in bots[bot_id][0][1]:
        bots[bots[bot_id][0][1]][1].append(max(bots[bot_id][1]))
        if len(bots[bots[bot_id][0][1]][1]) >= 2:
            bot_action(bots[bot_id][0][1])
    del bots[bot_id][1][0]
    del bots[bot_id][1][0]

def print_bots():
    for i in bots.keys():
        if len(bots[i][1]) != 0:
            print('{} : {}'.format(i, bots[i]))


with open(filename) as f:
    for line in f:
        line = line[:-1]
        if 'gives' in line:
            a = line.replace('bot ', '$b').replace('output ', '$o').split('$')[1:]
            bot_ids = [x.split()[0] for x in a]
            if bot_ids[0] not in bots:
                bots[bot_ids[0]] = [(bot_ids[1], bot_ids[2]), []]
            else:
                print("Unexpected bot_id repeat: {}".format(bot_ids[0]))

with open(filename) as f:
    for line in f:
        line = line[:-1]
        if  'goes to' in line:
            bot_id = line.replace('bot ', '$b').split('$')[1]
            bot_val = int(line.split()[1])
            bots[bot_id][1].append(bot_val)

# print_bots()

done = False
while not done:
    count = 0
    done = True
    for bot_id in bots.keys():
        if len(bots[bot_id][1]) >= 2:
            count += 1
            bot_action(bot_id)
            done = False
    # print(count)

print_bots()
