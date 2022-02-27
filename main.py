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




    def deal_hand(self):
        self.hand_1.deal(6)
        self.hand_2.deal(6)

def print_card(card):
    print(card.value,"of", card.suit)


def main():
    start = game()
    start.deal_hand()
    start.first_turn()
    start