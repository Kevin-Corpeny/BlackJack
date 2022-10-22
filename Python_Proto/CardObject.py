import random

class Card(object):    
    def __init__(self, soot:str , num: int):
        ## soot: suit of the card; either Hearts, Spade, Diamond, or Club
        ## num: numerical value of the card, used in the dict to translate jacks, queens, kings and aces
        ## **suit of the card will determine the color

        ##TODO: come up with better way to init this object, preferably simplify suit arg
        
        self.suit = soot
        self.card = num

        if soot == "Hearts" or soot == "Diamonds":
            self.color = "Red"
        else:
            self.color = "Black"

        self.num_to_card_dict = {
        1:"Ace",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"10",
        11:"Jack",
        12:"Queen",
        13:"King"
    }

    def __str__(self):
        try:
            return self.num_to_card_dict[self.card] + " of " + self.suit + "; "
        except KeyError:
            print("Error; likely a card has been initialized with a non-int num, or out of bounds...\n")
            return ""
    def __gt__(self, other):
        try:
            if self.card <= other.card:
                return False
            else:
                return True
        except:
            print("Error in method '__gt__'...\n")

    def __lt__(self, other):
        try:
            if self.card >= other.card:
                return False
            else:
                return True
        except:
            print("Error in method '__lt__'...\n")        

    def __eq__(self, other):
        try:
            if(self.card == other.card):
                return True
            else:
                return False
        except:
            print("Error in __eq__method")

class Deck(object):
    ##TODO: check if this should inherit from Card

    ##NOTE: IM FUCKING STUPID; FORGOT TO SHUFFLE THE DECK IN INIT
    def __init__(self):
        self.deck = []
        for x in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for y in range(1,14):
                self.deck.append(Card(x,y))
        random.shuffle(self.deck)
    def __str__(self):
        for card in self.deck:
            print(card)        
        return str(len(self.deck)) + " cards remaining" 
            
    def __repr__(self):
        return str(self.deck)

    def fresh_deck(self):
        self.deck = []
        for x in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for y in range(1,14):
                self.deck.append(Card(x,y))
        self.shuffle()

    def shuffle(self):
        for x in range(5):
            random.shuffle(self.deck)

    def draw(self):
        try:
            return self.deck.pop(0)
        except IndexError:
            print("Exception in method 'draw' in class 'Deck'... likely trying to draw from empty deck...\n")
            self.fresh_deck()
            self.shuffle()
            return self.deck.pop(0)

class Player(object):
    def __init__(self, userName: str):
        self.name = userName
        self.hand = []
        self.score = 0

    def __str__(self):
        returnString = ""
        for card in self.hand:
            returnString += str(card)
        return self.name + ": " + returnString

    def draw_hand(self,deck,handSize):
        for x in range(handSize-1):
            self.hand.append(deck.draw())

    def drawCard(self,deck):
        self.hand.append(deck.draw)

class Game(object):
    def __init__(self, mode: str, startSize: int, numPlayers: int):
        ## MODE WILL TELL YOU WHAT GAME YOU ARE PLAYING:
        ## "K" FOR KINGS IN CORNER
        ## "BJ" FOR BLACKJACK
        self.game = mode
        self.drawSize = startSize
        self.players = []
        self.cardpool = [Deck()]*5
        self.currentDeck = self.cardpool[0]
        testName = "tester#"
        for x in range(numPlayers):
            self.players.append(Player(testName+str(x)))

        for x in self.players:
            print(x)

    def deal(self):
        if self.game == "K":
            for player in self.players:
                player.draw_hand(self.currentDeck, self.drawSize)
                print(player)
                
"""
testCard = Card("Hearts", 12)
secondCard = Card("Spade",12)
print(testCard)
print(secondCard)
print(testCard == secondCard)
print(testCard<secondCard)

testDeck = Deck()
print(testDeck)
testDeck.shuffle()
print(testDeck)

testPlayer01 = Player("Test 01")
testPlayer01.draw_hand(testDeck,7)
print(testPlayer01)

testGame = Game("K",7,10)
testGame.deal()
"""
