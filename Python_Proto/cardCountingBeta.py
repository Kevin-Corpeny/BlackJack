from test01 import Deck
from test01 import Card
from time import sleep

testDeck = Deck()
countDict = {
    2  : 1,
    3  : 1,
    4  : 1,
    5  : 1,
    6  : 1,
    7  : 0,
    8  : 0,
    9  : 0,
    10 : -1,
    11 : -1,
    12 : -1,
    13 : -1,
    1  : -1
    }


def testGame(x: int, numCards: int):
    count: int = 0
    cardsLeft: int = 0
    for card in testDeck.deck:
        if cardsLeft < numCards:
            count += countDict[card.card]
            cardsLeft += 1
            print("***"+str(card)+"***")
        
            sleep(x)
        else:
            return count
        

def calc_count():
    return

print(testGame(1,5))
    
