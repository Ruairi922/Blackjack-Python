import random
import math

deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack"]

print("Welcome to blackjack!!")
print("The dealer will deal the cards now.")

player_hand = []
def deal_first_cards():
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    print(player_hand)
    total = 0

    for i in player_hand:
        if i == "King" or i == "Jack" or i == "Queen":
            total += 10
        elif i == "Ace":
            total += 11
        else:
            total += int(i)

    print("Your total is: " + str(total))


    hit_or_stand = input("Would you like to hit or stand?(h/s) ")
    if hit_or_stand == "h":
        player_hand.append(random.choices(deck))
    print(player_hand)

    print("Your new total is " + str(total))

deal_first_cards()

