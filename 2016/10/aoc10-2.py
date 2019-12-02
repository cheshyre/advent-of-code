from sys import argv

if len(argv) >= 2:
    filename = argv[1]
else:
    raise Exception("No input file given.")

bots = {}
outputs = {}

def sorting_key(a):
    return int(a[1:])

def bot_action(bot_id):
    if len(bots[bot_id][1]) != 2:
        raise Exception("Bot {} does not have 2 chips.".format(bot_id))
    if 'b' in bots[bot_id][0][0]:
        bots[bots[bot_id][0][0]][1].append(min(bots[bot_id][1]))
        if len(bots[bots[bot_id][0][0]][1]) >= 2:
            bot_action(bots[bot_id][0][0])
    else:
        outputs[bots[bot_id][0][0]].append(min(bots[bot_id][1]))
    if 'b' in bots[bot_id][0][1]:
        bots[bots[bot_id][0][1]][1].append(max(bots[bot_id][1]))
        if len(bots[bots[bot_id][0][1]][1]) >= 2:
            bot_action(bots[bot_id][0][1])
    else:
        outputs[bots[bot_id][0][1]].append(max(bots[bot_id][1]))
    del bots[bot_id][1][0]
    del bots[bot_id][1][0]

def print_bots():
    for i in bots.keys():
        if len(bots[i][1]) != 0:
            print('{} : {}'.format(i, bots[i]))

def print_outputs(a=None):
    if a is None:
        for i in sorted(outputs.keys(), key=sorting_key):
            print('{} : {}'.format(i, outputs[i]))
    else:
        for i in a:
            print('{} : {}'.format(i, outputs['o{}'.format(i)]))


with open(filename) as f:
    for line in f:
        line = line[:-1]
        if 'gives' in line:
            a = line.replace('bot ', '$b').replace('output ', '$o').split('$')[1:]
            bot_ids = [x.split()[0] for x in a]
            for i in bot_ids:
                if i[0] == 'o':
                    if i not in outputs:
                        outputs[i] = []
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
# print_outputs()

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

# print_bots()
# print_outputs()

print(outputs['o0'][0]*outputs['o1'][0]*outputs['o2'][0])