import random
import time
import sys

deck = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack"]

print("Welcome to BlackJack!!")
time.sleep(1)
print("The dealer will deal the cards now.")
time.sleep(1)

player_hand = []
dealer_hand = []
def deal_first_cards():
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    print(player_hand)
    time.sleep(1)
    total = 0

    for i in player_hand:
        if i == "King" or i == "Jack" or i == "Queen":
            total += 10
        elif i == "Ace":
            total += 11
        else:
            total += int(i)

    print("Your total is: " + str(total))
    time.sleep(1)



    while total < 21:
        hit_stand = input("Would you like to hit or stand(h/s)? ")
        time.sleep(1)
        if hit_stand == "h":
            player_hand.append(random.choice(deck))
            print(player_hand)

        newtotal = 0
        for i in player_hand:
            if i == "King" or i == "Jack" or i == "Queen":
                newtotal += 10
            elif i == "Ace":
                newtotal += 11
            else:
                newtotal += int(i)

        if newtotal > 21:
            print("Your total is now " + str(newtotal))
            time.sleep(1)
            print("You have gone bust")
            break

        elif newtotal <= 21:
            print("Your total is: " + str(newtotal))
            time.sleep(1)

#------------------------------------------------------------------------------------------------------------------


        if hit_stand == "s":
            dealer_hand.append(random.choice(deck))
            dealer_hand.append(random.choice(deck))
            print("Dealer has: " + str(dealer_hand))
            time.sleep(1)
            dealer_total = 0
            for i in dealer_hand:
                if i == "King" or i == "Jack" or i == "Queen":
                    dealer_total += 10
                elif i == "Ace":
                    dealer_total+= 11
                else:
                    dealer_total += int(i)
            print("Dealers total is: " + str(dealer_total))
            time.sleep(1)

            if dealer_total <= newtotal:
                dealer_hand.append(random.choice(deck))
                newdealer_total = 0
                print("Dealer pulls another card " + str(dealer_hand))
                time.sleep(1)
                for i in dealer_hand:
                    if i == "King" or i == "Jack" or i == "Queen":
                        newdealer_total += 10
                    elif i == "Ace":
                        newdealer_total += 11
                    else:
                        newdealer_total += int(i)
                print("Dealer now has " + str(newdealer_total))
                time.sleep(1)



                if newdealer_total > newtotal and newdealer_total < 22:
                    print("Dealer wins")
                    time.sleep(1)
                    sys.exit()

                elif newdealer_total == 21:
                    print("Dealer wins")


                elif newdealer_total >= 22:
                    print("YOU WIN!!")
                    time.sleep(1)
                    sys.exit()
                break



deal_first_cards()
