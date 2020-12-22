def play_round(deck1, deck2):
    play1 = deck1[-1]
    play2 = deck2[-1]
    if play1 > play2:
        deck1 = [play2, play1] + deck1[:-1]
        deck2 = deck2[:-1]
    else:
        deck2 = [play1, play2] + deck2[:-1]
        deck1 = deck1[:-1]
    
    return deck1, deck2
