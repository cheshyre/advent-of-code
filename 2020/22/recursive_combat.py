def check_list_equality(list1, list2):
    if len(list1) != len(list2):
        return False
    for x, y in zip(list1, list2):
        if x != y:
            return False
    return True


def generate_config(deck1, deck2):
    config = ""
    config += ",".join([str(x) for x in deck1])
    config += "v"
    config += ",".join([str(x) for x in deck2])
    return config


class RecursiveCombatGame:
    
    def __init__(self, deck1, deck2):
        self.deck1 = list(deck1)
        self.deck2 = list(deck2)
        self.previous_configs = set()
        
    def check_win_conditions(self):
        if len(self.deck1) == 0:
            return True, 2
        if len(self.deck2) == 0:
            return True, 1
        config = generate_config(self.deck1, self.deck2)
        # for x, y in self.previous_configs:
        #     if check_list_equality(x, self.deck1) and check_list_equality(y, self.deck2):
        #         return True, 1
        if config in self.previous_configs:
            return True, 1
        return False, -1
    
    def play_round(self):
        config = generate_config(self.deck1, self.deck2)
        self.previous_configs.add(config)
        
        card1 = self.deck1[0]
        card2 = self.deck2[0]
        
        self.deck1 = self.deck1[1:]
        self.deck2 = self.deck2[1:]
        
        # Base case
        if len(self.deck1) < card1 or len(self.deck2) < card2:
            if card1 > card2:
                self.deck1.append(card1)
                self.deck1.append(card2)
            else:
                self.deck2.append(card2)
                self.deck2.append(card1)
        # Recursive game case
        else:
            rec_game = RecursiveCombatGame(self.deck1[:card1], self.deck2[:card2])
            winner, _ = rec_game.play_until_completion()
            if winner == 1:
                self.deck1.append(card1)
                self.deck1.append(card2)
            else:
                self.deck2.append(card2)
                self.deck2.append(card1)
                
        return self.check_win_conditions()
    
    def play_until_completion(self):
        won, _ = self.check_win_conditions()
        while not won:
            won, _ = self.play_round()
            
        return self.calculate_score()

    def calculate_score(self):
        won, winner = self.check_win_conditions()
        if not won:
            return -1, 0
        
        if winner == 1:
            winning_deck = self.deck1
        else:
            winning_deck = self.deck2
        
        score = 0
        for i, x in enumerate(reversed(winning_deck), start=1):
            score += i * x
        
        return winner, score
    
    def print_state(self):
        deck1_str = ",".join([str(x) for x in self.deck1])
        deck2_str = ",".join([str(x) for x in self.deck2])
        print(f"P1 deck: {deck1_str}")
        print(f"P2 deck: {deck2_str}")
    