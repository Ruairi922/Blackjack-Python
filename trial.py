import random
import math

deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack"]

print("Welcome to blackjack!!")
print("The dealer will deal the cards now.")

player_hand = []
dealer_hand = []
def deal_first_cards():
    money = 50
    print("You have " + str(money) + " currency")
    bet = input("How much would you like to bet: ")
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



    while total <= 21:
        hit_stand = input("Would you like to hit or stand(h/s)? ")
        if hit_stand == "h":
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

        if total > 21:
            print("you have gone bust")
            money -= int(bet)

        elif total <= 21:
            print("Your total is: " + str(total))


        if hit_stand == "s":
            dealer_hand.append(random.choice(deck))
            dealer_hand.append(random.choice(deck))
            print("Dealer has: " + str(dealer_hand))
            dealer_total = 0
            for i in player_hand:
                if i == "King" or i == "Jack" or i == "Queen":
                    dealer_total += 10
                elif i == "Ace":
                    dealer_total+= 11
                else:
                    dealer_total += int(i)
            print("Dealers total is: " + str(dealer_total))

            if dealer_total <= total:
                dealer_hand.append(random.choice(deck))
                for i in player_hand:
                    if i == "King" or i == "Jack" or i == "Queen":
                        dealer_total += 10
                    elif i == "Ace":
                        dealer_total += 11
                    else:
                        dealer_total += int(i)

            if dealer_total > total and dealer_total < 22:
                print("dealer wins")





deal_first_cards()