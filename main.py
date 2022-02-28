import pydealer



class game:
    deck = pydealer.Deck()
    hand_1 = pydealer.Stack()
    hand_2 = pydealer.Stack()
    crib = pydealer.Stack()
    player_1_points = 0
    player_2_points = 0
    # prompts each player for a number then draws a card
    # and they player with the lower card goes first
    # returns 1 for p1 and 2 for p2
    def first_turn(self):
        self.deck.shuffle()

        card1 = self.deck.deal(1).cards
        card2 = self.deck.deal(1).cards

        if( card1 < card2):
            print(card1)
            print(card2)
            print("Player 1 has first crib")
            return 1
        else:
            print(card1)
            print(card2)
            print("player 2 has first crib")
            return 2

    def cards_to_crib(self):
        card1, card2 = [int(x) for x in input("Player 1 Enter two numbers here: ").split()]
        card3, card4 = [int(x) for x in input("Player 2 Enter two numbers here: ").split()]
        self.crib += self.hand_1.cards[card1]




    def deal_hand(self):
        self.deck.shuffle(3)

        self.hand_1 = self.deck.deal(6)
        self.hand_2 = self.deck.deal(6)


    new_ranks = {
        "values": {
            "Ace": 1,
            "King": 10,
            "Queen": 10,
            "Jack": 10,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        },
        "suits": {
            "Spades": 1,
            "Hearts": 1,
            "Clubs": 1,
            "Diamonds": 1
        }
    }

def print_card(card):
    print(card.value,"of", card.suit)


def main():
    start = game()
    start.deal_hand()
    print(start.hand_1,"\n")
    print(start.hand_2,"\n")
    start.cards_to_crib()
    print(start.crib,"\n")
    print(start.hand_1,"\n")

main()