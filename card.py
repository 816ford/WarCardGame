class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

    def ascii_version_of_card(*cards, return_string=True):
   
    # we will use this to prints the appropriate icons for each card
        suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]

        for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
            if card.rank == '10':  # ten is the only one who's rank is 2 char long
                rank = card.rank
                space = ''  # if we write "10" on the card that line will be 1 char to long
            else:
                rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
                space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
            suit = suits_name.index(card.suit)
            suit = suits_symbols[suit]

        # add the individual card on a line by line basis
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))

    # hidden cards do not use string
        if return_string:
            return '\n'.join(result)
        else:
            return result


    def ascii_version_of_hidden_card(*cards):
    
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
        lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
        cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)
        for index, line in enumerate(cards_except_first):
            lines[index].append(line)

    # make each line into a single list
        for index, line in enumerate(lines):
            lines[index] = ''.join(line)

    # convert the list into a single string
        return '\n'.join(lines)

    card1 = Card('Hearts', '10')

    print(ascii_version_of_card(card1))