import random

def shuffle_deck():
    game_deck = []

    for _ in range(4):
        game_deck += deck_list

    print("Shuffling the deck")
    random.shuffle(game_deck)
    return game_deck

def place_bet():
    while True:
        bet = int(input("How much do you want to bet?\n"))
        if not bet in (25, 50, 100):
            print("You can only bet 25$, 50$ or 100$")
            continue
        # control if bet is a string
        # elif bet:
        #     True
        else:
            break
    return bet

def continue_playing():
    if player_balance == 0:
        playing = "N"
        return playing
    while True:
        playing = input("Do you want to play again? Y/N\n").capitalize()
        if not playing in ("Y","N"):
            print("Please enter Y if you wish to continue playing. Enter N if you want to end the game.")
            continue
        else:
            break
    if playing == "N":
        print("Thank you for playing with us!\nYour balance is {}".format(player_balance))
    return playing

deck_dict = {"2 spades": 2, "3 spades": 3, "4 spades": 4, "5 spades": 5, "6 spades": 6, "7 spades": 7, "8 spades": 8,
 "9 spades": 9, "10 spades": 10, "J spades": 10, "Q spades": 10, "K spades": 10, "A spades": 11,
 "2 hearts": 2, "3 hearts": 3, "4 hearts": 4, "5 hearts": 5, "6 hearts": 6, "7 hearts": 7, "8 hearts": 8,
 "9 hearts": 9, "10 hearts": 10, "J hearts": 10, "Q hearts": 10, "K hearts": 10, "A hearts": 11,
 "2 diamonds": 2, "3 diamonds": 3, "4 diamonds": 4, "5 diamonds": 5, "6 diamonds": 6, "7 diamonds": 7, "8 diamonds": 8,
 "9 diamonds": 9, "10 diamonds": 10, "J diamonds": 10, "Q diamonds": 10, "K diamonds": 10, "A diamonds": 11,
 "2 clubs": 2, "3 clubs": 3, "4 clubs": 4, "5 clubs": 5, "6 clubs": 6, "7 clubs": 7, "8 clubs": 8,
 "9 clubs": 9, "10 clubs": 10, "J clubs": 10, "Q clubs": 10, "K clubs": 10, "A clubs": 11}

deck_list = ["2 spades", "3 spades", "4 spades", "5 spades", "6 spades", "7 spades", "8 spades",
 "9 spades", "10 spades", "J spades", "Q spades", "K spades", "A spades",
 "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts", "7 hearts", "8 hearts",
 "9 hearts", "10 hearts", "J hearts", "Q hearts", "K hearts", "A hearts",
 "2 diamonds", "3 diamonds", "4 diamonds", "5 diamonds", "6 diamonds", "7 diamonds", "8 diamonds",
 "9 diamonds", "10 diamonds", "J diamonds", "Q diamonds", "K diamonds", "A diamonds",
 "2 clubs", "3 clubs", "4 clubs", "5 clubs", "6 clubs", "7 clubs", "8 clubs",
 "9 clubs", "10 clubs", "J clubs", "Q clubs", "K clubs", "A clubs"]

player_balance = 100
bet = 0
hand_counter = 0
playing = "Y"

print("Welcome to Python Terminal Blackjack!")
print("This table only accepts 25$, 50$ or 100$ bets")

game_deck = shuffle_deck()

while playing == "Y" and player_balance > 0:
    hand_counter += 1

    bet = place_bet()

    print("Your bet for this round is {}".format(bet))

    player_cards = []
    dealer_cards = []

    player_cards.append(game_deck.pop())
    dealer_cards.append(game_deck.pop())
    player_cards.append(game_deck.pop())
    dealer_cards.append(game_deck.pop())

    player_cards_str = ""
    for i in range(len(player_cards)):
        player_cards_str += player_cards[i] + ", "

    dealer_cards_str = dealer_cards[0] + ", "

    print("Your cards: {}".format(player_cards_str[:-2]))

    print("Dealer cards: {}".format(dealer_cards_str[:-2]))

    player_score = 0
    dealer_score = 0

    for i in range(len(player_cards)):
        player_score += deck_dict[player_cards[i]]

    dealer_score += deck_dict[dealer_cards[0]]

    print("Player score: {}".format(player_score))
    print("Dealer score: {}".format(dealer_score))
    
    player_action = input("Hit or Stand?\n").upper()

    bust = "N"

    while player_action == "HIT":
        
        player_cards.append(game_deck.pop())
        player_cards_str = ""
        for i in range(len(player_cards)):
            player_cards_str += player_cards[i] + ", "
        
        print("Your cards: {}".format(player_cards_str[:-2]))
        
        player_score = 0
        for i in range(len(player_cards)):
            player_score += deck_dict[player_cards[i]]
            if player_score > 21 and "A" in player_cards_str:
                player_score -= 10

        
        
        print("Player score: {}".format(player_score))

        if player_score > 21:
            bust = "Y"
            print("Bust!")
            print("Dealer wins!")
            player_balance -= bet
            break
        elif player_score == 21:
            break

        player_action = input("Hit or Stand?\n").upper()
        
    if player_balance == 0:
        print("We're sorry! Your balance is 0. Thank you for playing with us.")
        break

    if bust == "Y":
        print("Your balance is {}".format(player_balance))
        playing = continue_playing()
        continue
            
    ##### DEALER ####
    dealer_cards_str = ""
    for i in range(len(dealer_cards)):
        dealer_cards_str += dealer_cards[i] + ", "
    print("Dealer cards: {}".format(dealer_cards_str[:-2]))

    dealer_score = 0
    for i in range(len(dealer_cards)):
        dealer_score += deck_dict[dealer_cards[i]]
    
    print("Player score: {}".format(player_score))
    print("Dealer score: {}".format(dealer_score))

    while dealer_score < 17:
        dealer_cards.append(game_deck.pop())
        dealer_cards_str = ""
        for i in range(len(dealer_cards)):
            dealer_cards_str += dealer_cards[i] + ", "
        print("Dealer cards: {}".format(dealer_cards_str[:-2]))

        dealer_score = 0
        for i in range(len(dealer_cards)):
            dealer_score += deck_dict[dealer_cards[i]]
        print("Player score: {}".format(player_score))
        print("Dealer score: {}".format(dealer_score))

    if dealer_score > 21:
        print("Bust!")
        print("Player wins!")
        player_balance += bet
        print("Your balance is {}".format(player_balance))
        playing = continue_playing()
        continue


    #### SCORE COMPARISON ####
    if player_score > dealer_score:
        print("You win!")
        player_balance += bet
        print("Your balance is {}".format(player_balance))
    elif player_score == dealer_score:
        print("Blackjack Push!")
        print("Your balance is {}".format(player_balance))
    else:
        print("Dealer wins!")
        player_balance -= bet
        if player_balance == 0:
            print("We're sorry! Your balance is 0. Thank you for playing with us.")
            break
        else:
            print("Your balance is {}".format(player_balance))

    playing = continue_playing()

    # arreglar para que cada 5 manos baraje
    if hand_counter == 5:
        game_deck = shuffle_deck()

print("You have played a total of {} round/s".format(hand_counter))






