deck = {"2 spades": 2, "3 spades": 3, "4 spades": 4, "5 spades": 5, "6 spades": 6, "7 spades": 7, "8 spades": 8,
 "9 spades": 9, "10 spades": 10, "J spades": 10, "Q spades": 10, "K spades": 10, "A spades": 11,
 "2 hearts": 2, "3 hearts": 3, "4 hearts": 4, "5 hearts": 5, "6 hearts": 6, "7 hearts": 7, "8 hearts": 8,
 "9 hearts": 9, "10 hearts": 10, "J hearts": 10, "Q hearts": 10, "K hearts": 10, "A hearts": 11,
 "2 diamonds": 2, "3 diamonds": 3, "4 diamonds": 4, "5 diamonds": 5, "6 diamonds": 6, "7 diamonds": 7, "8 diamonds": 8,
 "9 diamonds": 9, "10 diamonds": 10, "J diamonds": 10, "Q diamonds": 10, "K diamonds": 10, "A diamonds": 11,
 "2 clubs": 2, "3 clubs": 3, "4 clubs": 4, "5 clubs": 5, "6 clubs": 6, "7 clubs": 7, "8 clubs": 8,
 "9 clubs": 9, "10 clubs": 10, "J clubs": 10, "Q clubs": 10, "K clubs": 10, "A clubs": 11}


player_balance = 100
bet = 0
hand_counter = 0
playing = "Y"

def place_bet():
    while True:
        bet = int(input("How much do you want to bet?\n"))
        if not bet in (25, 50, 100):
            print("You can only bet 25$, 50$ or 100$")
            continue
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

print("Welcome to Python Terminal Blackjack!")
print("This table only accepts 25$, 50$ or 100$ bets")

while playing == "Y" and player_balance > 0:
    hand_counter += 1

    bet = place_bet()

    print("Your bet for this round is {}".format(bet))
    # print("Shuffling the deck")

    player_cards = int(input("Enter the player's card count\n"))

    dealer_cards = int(input("Enter the dealer's card count\n"))

    if player_cards > dealer_cards:
        print("You win!")
        player_balance += bet
        print("Your balance is {}".format(player_balance))
    elif player_cards == dealer_cards:
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


print("You have played a total of {} round/s".format(hand_counter))
