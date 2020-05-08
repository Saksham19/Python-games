#Blackjack

#Step1: import the random moduel and set up global variables

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing=True #this is a boolean used to control while loops (this a common practice used to control the flow of the game)


#Step 2: Create a card class

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self): #str definition so that whenever asked to print a card, we get this:
        return self.rank + " of " + self.suit

#Step 3: Create a deck class

class Deck:

#Storing the 52 card objects in a list that can later be shuffled.
    
    def __init__(self):
        self.deck=[] #start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=""
        for card in self.deck:
            deck_comp+="\n" + card.__str__()
        return "The deck has: " +deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card

#Step 4: Create a hand class
# hand class: to hold card objects dealt from the deck and to calculate the value of those cards using value dictionary defined above

class Hand:
    def __init__(self):
        self.cards=[] #start with an empty list
        self.value=0
        self.aces=0

    def add_card(self,card):
        #card passed will be from Deck.dead(single_card))
        self.cards.append(card)
        self.value+=values[card.rank]

        #track aces
        if card.rank=="Ace":
            self.aces+=1

    def adjust_for_ace(self):
        #if total value>21 and i still have an ace
        #then change my ace to be a 1 instead of 11
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1

#Step 5: Create a chips class

class Chips:

    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

#Step 6: Write a function for taking bets

def take_bet(chips):

    while True:

        try:
            chips.bet=int(input("How many chips would you like to bet?: "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet>chips.total:
                print("Sorry, your bet cant exceed", chips.total)
            else:
                break

#Step 7: Write a function for taking hits

#Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Step 8 : Write a function prompting the player to hit or stand

def hit_or_stand(deck,hand):
    global playing #to control an upcoming while loop

    while True:
        x=input("Hit or stand? enter h or s: ")

        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("player stands dealer's turn")
            playing=False

        else:
            print("Sorry, please enter h or s only")
            continue
        break

#Step 9: Write functions to display cards

def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print("<card hidden>")
    print("",dealer.cards[1])
    print("\nPlayer's hand: ",*player.cards,sep='\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#Step 10: write functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("bust player")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("player wins! dealer busted")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("dealer wins!")
    chips.lose_bet()
    
def push():
    print("dealer and player tie! push")

#Final game:
while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK")
    
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips=Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
            
        while dealer_hand.value< player_hand.value:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    # Inform Player of their chips total 
    print("\n Player total chips are at: {}".format(player_chips.total))
        
    # Ask to play again
    new_game=input("would you like to play again? y/n ")
        
    if new_game[0].lower()=="y":
        playing=True
    else:
        print("Thank you for playing")
        break
    
