# Grant, Cody, Thomas, Lauren
# September 6th, 2023
# War Card Game

import math
import random

# Step 1
# Ask user for how many players 
players = 2


# Variables to make handling values easier
A = 14
K = 13
Q = 12
J = 11


# Initialize the deck with value only.
deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, J, J, J, J, Q, Q, Q, Q, K, K, K, K, A, A, A, A]

middle = []

war = []

# Create hands for each player -- what if there's only 2 players or 3?
hands = []

# random card from deck goes to each player until deck is empty, as evenly as possible
def deal():
    global deck
    currentHand = []
    cardsPerHand = math.floor(len(deck) / players)
    cardsToIssueInHand = cardsPerHand
    for i in range(players):
        cardsToIssueInHand = cardsPerHand
        while cardsToIssueInHand > 0:
            currentHand.append(deck.pop(random.randint(0, len(deck) - 1)))
            cardsToIssueInHand -= 1
        hands.append(currentHand)
        currentHand = []
    extraCardsCurrentHand = 0
    while len(deck) > 0:
        hands[extraCardsCurrentHand % players].append(deck.pop(random.randint(0, len(deck) - 1)))
        extraCardsCurrentHand += 1
        if len(deck) == 0:
            break

deal()
print("Each player has", len(hands[0]), "cards.")

def placeCard(hand):
    global players
    if len(hand) == 0:
        noCards()
    middle.append(hand.pop(0))

def warPlaceCard(hand):
    for i in range(4):
        war.append(hand.pop(0))

def doWar(hand):
    if len(hand) < 4:
        war.extend(hand)
    warPlaceCard(hand)

    
def noCards():
    global players
    if len(hands[0]) == 0:
        print("Player 1 has no more cards!  Player 2 wins!")

    elif len(hands[1]) == 0:
        print("Player 2 has no more cards!  Player 1 wins!")

#snip from cody
playAgain = input("would you like to start? (y or n) ")
while playAgain == "y":
    middle = []
    war = []
    #places a crad from each players hand
    for player in range(players):
        placeCard(hands[player])

    print("\nPlayer 1 played: ", middle[0])
    print("Player 2 played: ", middle[1])

    def winCheck():
        global middle, hands, war, players
            
        if middle[0] > middle[1]:
            hands[0].extend(middle)
            print("player 1 won the round!")
        elif middle[1] > middle[0]:
            hands[1].extend(middle)
            print("player 2 won the round!")
        else:
            print("Its a tie time for War!")
            doWar(hands[0])
            doWar(hands[1])
            print(war)
            warWinCheck()
            
                
    def warWinCheck():
        global middle, hands, war
        if war[3] > war[len(war) - 1]:
            hands[0].extend(war)
            hands[0].extend(middle)
            print("player 1 won that war with a(n)", war[3], "!")
            noCards()
        elif war[len(war)-1] > war[3]:
            hands[1].extend(war)
            hands[1].extend(middle)
            print("player 2 won that war with a(n)", war[len(war)-1], "!")
            noCards()
        else:
            middle.extend(war)
            war = []
            print("Its a tie time for War!")
            doWar(hands[0])
            doWar(hands[1])
            noCards()
       
        

    winCheck()
    

    for player in range(players):
        print("Player", player+1, "has", len(hands[player]), "cards left.")
    playAgain = input("would you like to play the next round (y or n) ")
else:
    if len(hands[0]) > len(hands[1]):
        print("player 1 won the Game!")
    else:
        print("player 2 won the Game!")