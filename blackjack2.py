import random

player_hand = []
dealer_hand = []


#dealer cards
while len(dealer_hand) != 2:
    dealer_hand.append(random.randint(1, 11))
    if len(dealer_hand) == 2:
        print("Dealer has {} and a hidden card.".format(dealer_hand[0]))

#player cards
while len(player_hand) != 2:
    player_hand.append(random.randint(1, 11))
    if len(player_hand) == 2:
        print("You have", player_hand)

#sum of dealer cards
if sum(dealer_hand) == 21:
    print("Dealer has 21 with", dealer_hand, "and wins.")
elif sum(dealer_hand) > 21:
    print("Dealer has busted")

#sum of player cards
while sum(player_hand) < 21:
    choice1 = input("Will you hit or stay? ")
    if choice1 == "hit":
        player_hand.append(random.randint(1, 11))
        print("You have in total {} with".format(sum(player_hand)), player_hand)
    else:
        print("Dealer has in total {} with".format(sum(dealer_hand)), dealer_hand)
        print("You have in total {} with".format(sum(player_hand)), player_hand)
        if sum(dealer_hand) > sum(player_hand):
            print("Dealer wins.")
        else:
            print("You win.")
            break

if sum(player_hand) > 21:
    print("Busted. Dealer wins.")
elif sum(player_hand) == 21:
    print("BLACKJACK!!!")
