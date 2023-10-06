# Grant, Cody, Thomas, Lauren
# September 6th, 2023
# War Card Game

import math
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

print(hands)
for hand in hands:
    print(len(hand))

def noCardsCheck(hand):
    global players
    for hand in hands:
        if len(hand) == 0:
            hands.remove(hand)
            players -= 1

def placeCard(hand):
    noCardsCheck(hand)
    middle.append(hand.pop(0))

def warPlaceCard(hand):
    noCardsCheck(hand)
    war.append(hand.pop(0))

def doWar(hand):
    for i in range(4):
        warPlaceCard(hand)

    
    

#snip from cody
playAgain = input("would you like to start? (y or n) ")
while playAgain == "y":
    middle = []
    war = []
    #places a crad from each players hand
    for player in range(players):
        placeCard(hands[player])

    print(middle)

    def winCheck():
        global middle, hands, war, players
        if players == 2:

            if middle[0] > middle[1]:
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif middle[1] > middle[0]:
                hands[1].extend(middle)
                print("player 2 won that round!")
            else:
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[1])
                print(war)
                warWinCheck()
            
        elif players == 3:
            if middle[0] > middle[1] and middle[0] > middle[2]:
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif middle[1] > middle [0] and middle[1] > middle[2]:
                hands[1].extend(middle)
                print("player 2 won that round!")
            elif middle[2]>middle[0] and middle[2]>middle[1]:
                hands[2].extend(middle)
                print("player 3 won that round!")
            else:
                print("Its a tie time for War!")
                if middle[0] == middle[1]:
                    doWar(hands[0])
                    doWar(hands[1])
                    print(war)
                    warWinCheck()
                elif middle[0] == middle[2]:
                    doWar(hands[0])
                    doWar(hands[2])
                    print(war)
                    warWinCheck()
                else:
                    doWar(hands[1])
                    doWar(hands[2])
                    print(war)
                    warWinCheck()
        elif players == 4:
            if middle[0] > middle[1] and middle[0] > middle[2] and middle[0] > middle[3]:
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif middle[1] > middle [0] and middle[1] > middle[2] and middle[1] > middle[3]:
                hands[1].extend(middle)
                print("player 2 won that round!")
            elif middle[2]>middle[0] and middle[2]>middle[1] and middle[2]>middle[3]:
                hands[2].extend(middle)
                print("player 3 won that round!")
            elif middle[3]>middle[0] and middle[3]>middle[1] and middle[3]>middle[2]:
                hands[3].extend(middle)
                print("player 4 won that round!")
            else:
                print("Its a tie time for War!")
                if middle[0] == middle[1]:
                    doWar(hands[0])
                    doWar(hands[1])
                    print(war)
                    warWinCheck()
                elif middle[0] == middle[2]:
                    doWar(hands[0])
                    doWar(hands[2])
                    print(war)
                    warWinCheck()
                elif middle[0] == middle[3]:
                    doWar(hands[0])
                    doWar(hands[3])
                    print(war)
                    warWinCheck()
                elif middle[1] == middle[2]:
                    doWar(hands[1])
                    doWar(hands[2])
                    print(war)
                    warWinCheck()
                elif middle[1] == middle[3]:
                    doWar(hands[1])
                    doWar(hands[3])
                    print(war)
                    warWinCheck()
                else:
                    doWar(hands[2])
                    doWar(hands[3])
                    print(war)
                    warWinCheck()
                
    def warWinCheck():
        global middle, hands, war
        if players == 2:

            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 2 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[1])
        if players == 3 and middle[0] == middle[1]:
            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 2 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[1])
        if players == 3 and middle[0] == middle[2]:
            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[2].extend(war)
                hands[2].extend(middle)
                print("player 2 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[2])
        if players == 3 and middle[1] == middle[2]:
            if war[3] > war[7]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[2].extend(war)
                hands[2].extend(middle)
                print("player 2 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[1])
                doWar(hands[2])
        if players == 4 and middle[0] == middle[1]:
            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 2 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[1])
        if players == 4 and middle[0] == middle[2]:
            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[2].extend(war)
                hands[2].extend(middle)
                print("player 3 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[2])
        if players == 4 and middle[0] == middle[3]:
            if war[3] > war[7]:
                hands[0].extend(war)
                hands[0].extend(middle)
                print("player 1 won that round!")
            elif war[7] > war[3]:
                hands[3].extend(war)
                hands[3].extend(middle)
                print("player 4 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[0])
                doWar(hands[3])
        if players == 4 and middle[1] == middle[2]:
            if war[3] > war[7]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 2 won that round!")
            elif war[7] > war[3]:
                hands[2].extend(war)
                hands[2].extend(middle)
                print("player 3 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[1])
                doWar(hands[2])
        if players == 4 and middle[1] == middle[3]:
            if war[3] > war[7]:
                hands[1].extend(war)
                hands[1].extend(middle)
                print("player 2 won that round!")
            elif war[7] > war[3]:
                hands[3].extend(war)
                hands[3].extend(middle)
                print("player 4 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[1])
                doWar(hands[3])
        if players == 4 and middle[2] == middle[3]:
            if war[3] > war[7]:
                hands[2].extend(war)
                hands[2].extend(middle)
                print("player 3 won that round!")
            elif war[7] > war[3]:
                hands[3].extend(war)
                hands[3].extend(middle)
                print("player 4 won that round!")
            else:
                middle.extend(war)
                war = []
                print("Its a tie time for War!")
                doWar(hands[2])
                doWar(hands[3])
        

    winCheck()
    

    for player in range(players):
        print(hands[player])
    playAgain = input("would you like to play the next round (y or n) ")
else:
    if len(hands[0]) > len(hands[1]):
        print("player 1 won!")
    else:
        print("player 2 won!")