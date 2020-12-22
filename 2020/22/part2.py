import os

import recursive_combat


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

game = recursive_combat.RecursiveCombatGame(deck1, deck2)
game.print_state()
won, winner = game.check_win_conditions()
while not won:
    won, winner = game.play_round()
    game.print_state()
    
print(game.calculate_score())
    