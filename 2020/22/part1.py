import os

import combat


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    # Player1
    cur_line = f.readline()
    deck1 = []
    cur_line = f.readline()
    while cur_line.strip() != "":
        deck1.append(int(cur_line.strip()))
        cur_line = f.readline()

    # Player2
    cur_line = f.readline()
    deck2 = []
    cur_line = f.readline()
    while cur_line.strip() != "":
        deck2.append(int(cur_line.strip()))
        cur_line = f.readline()

deck1 = list(reversed(deck1))
deck2 = list(reversed(deck2))

print(deck1)
print(deck2)
while len(deck1) != 0 and len(deck2) != 0:
    deck1, deck2 = combat.play_round(deck1, deck2)
    print(deck1)
    print(deck2)
    
if len(deck1) != 0:
    winning_deck = deck1
else:
    winning_deck = deck2
    
score = 0
for i, x in enumerate(winning_deck, start=1):
    score += i * x
print(score)