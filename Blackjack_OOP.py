"""
Project start date 2/1/24
Design a game of Blackjack using Object Oriented methods.

Classes Needed:
    1)Dealer
        -will have unlimited money (god damn casinos)
    2)Player(s)
        -Money in their "account"
    3)Cards
        -suits
        -interger values
    4)Deck (make with 64 cards?)
        -Holds all the card objects and their respective values
    5)Wager system/value?

How the game works:
Objective of game is to beat the dealer by getting 21 or as close to it as possible. If dealer's card values are higher than yours, you lose.
Player 1 places a wager
Dealer deals 1 card to players face up
Dealer gives 1 card face down to himself
Dealer gives 1 more card to all players (all players will have 2 cards)
Dealer gives 1 card face up to himself (1 Card face up 1 Card face down)
If player card total is equal to 21 they hit "blackJack" and wins 2.5x their wager (end of Round)
Player or players will decide whether they want to "Hit" "Stay" or "Double"
Hit-
    Player has choice to hit until their total card value is over 21 they "Bust" and the dealer wins.
    Once player is done hitting and their card value is not 21, the dealer will flip his face down card
    if the dealers card values are less than 17 
    dealer will draw cards from deck until either he has a card value greater than or equal to 17 but less than 21
    if the dealer goes over 21, he "busts" end of round, player wins
    if the dealers cards values are under or equal to 21 and greater than the players card values, Player loses
    if the players card values are under or equal to 21 and greater than the dealers card values, Player wins
Stay-
    Player has choice to stay right when they are dealt their cards
    dealer then flips his card
    if the dealers card values are less than 17 
    dealer will draw cards from deck until either he has a card value greater than or equal to 17 but less than 21
    if the dealer goes over 21, he "busts" end of round, player wins
    if the dealers cards values are under or equal to 21 and greater than the players card values, Player loses
    if the players card values are under or equal to 21 and greater than the dealers card values, Player wins
Double (Maybe dont incorporate yet due to complexity)-
    Player has choice to double their wager
    Can only be done when the player has 2 cards
    If player doubles, 1 card from deck will be added to players card.
    If card value is over 21, they bust.
    if card value is 21 or under dealer will flip his cards
    if the dealers card value is under 17 dealer will draw cards
    if the dealer goes over 21, he "busts" end of round, player wins
    if the dealers cards values are under or equal to 21 and greater than the players card values, Player loses
    if the players card values are under or equal to 21 and greater than the dealers card values, Player wins
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return str(self.value)
    
class Deck:
    def __init__(self):
        self.allCards = []
        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit,rank)
                self.allCards.append(createdCard)
        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit,rank)
                self.allCards.append(createdCard)
    def shuffle(self):
        random.shuffle(self.allCards)
    def deal_one(self):
        return self.allCards.pop()

class player:
    def __init__(self, name):
        self.name = name
        self.allCards = []
    def remove_one(self):
        return self.allCards.pop(0)
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.allCards.extend(new_cards)
        else:
            self.allCards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.allCards)} cards.'
    # def hit(self):
    #     return 

    

#GAME LOGIC
game_on = True
new_deck = Deck()
new_deck.shuffle()
while game_on:


    if len(new_deck.allCards) < 3:
        print("Out of Cards")
        play_again = input("Press y to play again?: ")
        if play_again == "y" or play_again ==  "Y":
            new_deck = Deck()
            new_deck.shuffle()
        else:
            break

    Dealer_1 = player("Dealer")
    Player_1 = player("Player")

#Deal 2 cards to Player and Dealer
    for x in range(2):
        Dealer_1.add_cards(new_deck.deal_one())
        Player_1.add_cards(new_deck.deal_one())

#Choice to Stay or Hit here
    dealer_hand = []
    for x in range (2):
        dealer_hand.append(Dealer_1.remove_one())
    print("Dealer shows:", dealer_hand[0].value)

    player_hand = []
    for x in range (2):
        player_hand.append(Player_1.remove_one())
    print(f"{Player_1.name} shows:", player_hand[0].value + player_hand[1].value)

    if player_hand[0].value + player_hand[1].value < 21:
        user_Choice = input("Press ""H"" to hit or ""S"" to stay: ")
        times_hit = 0
# if user stays on initial cards dealt
        if user_Choice == "s" or user_Choice == "S":
            print("Dealer shows:", dealer_hand[0].value + dealer_hand[1].value)
            print(f"{Player_1.name} shows:", player_hand[0].value + player_hand[1].value)
            if dealer_hand[0].value + dealer_hand[1].value < 17 and dealer_hand[0].value + dealer_hand[1].value <22:
                Dealer_1.add_cards(new_deck.deal_one())
                dealer_hand.append(Dealer_1.remove_one())          
                print(f"{Dealer_1.name} shows:", dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value)
                if dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value > 21:
                    print("DEALER BUST PLAYER WINS")
                if player_hand[0].value + player_hand[1].value > dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value and dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value >= 17:
                        print("Player WINS")
                if player_hand[0].value + player_hand[1].value < dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value and dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value < 22 and dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value >= 17:
                        print("Dealer Wins")
                if dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value < 17 and dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value < 21:
                    Dealer_1.add_cards(new_deck.deal_one())
                    dealer_hand.append(Dealer_1.remove_one())
                    print(f"{Dealer_1.name} shows:", dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value + dealer_hand[3].value)
                    print()
                    if player_hand[0].value + player_hand[1].value > dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value + dealer_hand[3].value:
                        print("Player WINS")
                    if player_hand[0].value + player_hand[1].value < dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value + dealer_hand[3].value and dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value + dealer_hand[3].value < 21:
                        print("Dealer Wins")
                    if dealer_hand[0].value + dealer_hand[1].value + dealer_hand[2].value + dealer_hand[3].value > 21:
                        print("DEALER BUST PLAYER WINS")

            elif player_hand[0].value + player_hand[1].value > dealer_hand[0].value + dealer_hand[1].value:
                print(f"{Player_1.name} WINS")
            elif player_hand[0].value + player_hand[1].value < dealer_hand[0].value + dealer_hand[1].value:
                print(f"{Dealer_1.name} WINS")
            else:
                print("TIE GAME NO WINNNER")
#if user hits on initial cards dealt
        if user_Choice == "h" or user_Choice == "H" and times_hit == 0:
             times_hit+=1
             Player_1.add_cards(new_deck.deal_one())
             player_hand.append(Player_1.remove_one())
             print("Player shows:", player_hand[0].value + player_hand[1].value + player_hand[2].value)
             if player_hand[0].value + player_hand[1].value + player_hand[2].value > 21:
                 print("BUST DEALER WINS")
             elif player_hand[0].value + player_hand[1].value + player_hand[2].value < 21:
                 user_Choice = input("Press ""H"" to hit or ""S"" to stay: ")
                 if user_Choice == "s" or user_Choice == "S":
                    print("Dealer shows:", dealer_hand[0].value + dealer_hand[1].value)
                    print(f"{Player_1.name} shows:", player_hand[0].value + player_hand[1].value + player_hand[2].value)
                    if dealer_hand[0].value + dealer_hand[1].value < 17:
                        Dealer_1.add_cards(new_deck.deal_one())
                        dealer_hand.append(Player_1.remove_one())                      
                 if user_Choice == "h" or user_Choice == "H":
                    Player_1.add_cards(new_deck.deal_one())
                    player_hand.append(Player_1.remove_one())
        


    # if player_hand[0].value + player_hand[1].value + player_hand[2].value <21:
    #     user_Choice = input("Press ""H"" to hit or ""S"" to stay: ")
    #     if user_Choice == 'h' or user_Choice == "h" and times_hit == 1:
    #         times_hit+=1
    #         Player_1.add_cards(new_deck.deal_one())
    #         player_hand.append(Player_1.remove_one())
    #         print("Player shows:", player_hand[0].value + player_hand[1].value + player_hand[2].value + player_hand[3].value)
    #     else:
    #         break
             

    if player_hand[0].value + player_hand[1].value == 21 and dealer_hand[0].value + dealer_hand[1].value < 21:
        print("Blackjack! Player wins")
        



"""la
TESTING
"""
