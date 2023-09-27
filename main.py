# Grant, Cody, Thomas, Lauren
# September 6th, 2023
# War Card Game

import random

# Step 1
# Ask user for how many players 
players = eval(input("How many players should this game have? "))

if players == 1:
    print("You can't play by yourself!")
    exit
elif players >= 5:
    print("Too many players, not enough cards.")
    exit

# Variables to make handling values easier
A = 14
K = 13
Q = 12
J = 11


# Initialize the deck with value only.
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, J, J, J, J, Q, Q, Q, Q, K, K, K, K, A, A, A, A]
middle = []
warPile = []
# Create hands for each player -- what if there's only 2 players or 3?
hands = [
    [], [], [], []
]

# random card from deck goes to each player until deck is empty, as evenly as possible
def deal():
    while len(deck) > 0:
        for player in range(players):
            dealt_card = deck.pop(random.randint(0, len(deck)-1))
            hands[player].append(dealt_card)

deal()

def placeCard(hand):
    middle.append(hand.pop(0))

def war(hand):
    for i in range(4):
        middle.extend(warPile)
        warPile.clear()
        warPile.append(hand.pop(0))


'''
for player in range(players):
    print(hands[player])
'''