import random
import time

rules = "The rules are below if you dont know how to play: type 'y' when you are ready to continue.\nThe aim of the game is to accumulate a higher point total than the dealer,\n but without going over 21. You compute your score by adding the values of\n your individual cards. The cards 2 through 10 have their face value, J, Q,\n and K are worth 10 points each, and the Ace is worth either 1 or 11 points \n(player's choice).Then the player can keep his hand as it is (stand) or take more \ncards from the deck (hit), one at a time, until either the player judges that the hand \nis strong enough to go up against the dealer's hand and stands, or until it goes over 21, \n in which case the player immediately loses (busts).\n type 'y' to continue:  "
type = ["Spade", "Heart", "Clover", "Diamond"]
num = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "king", "Queen"]
first_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
second_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
third_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
fourth_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
fifth_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
sixth_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
seventh_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
eight_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
ninth_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
tenth_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
eleventh_card = str(random.choice(num)) + " of " + random.choice(type) + "s"
users_cards = []
users_cards.append(first_card)
users_cards.append(second_card)
print("The dealer is shuffliing the deck")
time.sleep(1.5)
print("You have been dealt " + str(users_cards))
time.sleep(1.5)
hit_or_stand = input("Would you like to hit or stand(h/s): ")
def dealers_cards():
    cards = []

if hit_or_stand == "h":
    users_cards.append(third_card)
