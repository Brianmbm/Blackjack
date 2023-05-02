
import cards
import time
import os
import titles
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)#Resets color for every string printed

#Deal one card to player
def dealcardPlayer(playerCards, dealerCards, deck):
    while True:
            index = random.randint(0, 51)
            if deck.deck[index] not in playerCards or dealerCards:
                playerCards.append(deck.deck[index])
                break
    return playerCards
#Deal one card to dealer
def dealcardDealer(playerCards, dealerCards, deck):
    while True:
            index = random.randint(0, 51)
            if deck.deck[index] not in playerCards or dealerCards:
                dealerCards.append(deck.deck[index])
                break
    return dealerCards
#Prints player cards
def playerCardsToString(playerCards):
    strings = []
    for i in range(len(playerCards)):
        strings.append(playerCards[i].cardImage)
    #Stackoverflow solution to printing multiple line strings next to each other
    print(Fore.RED + Style.BRIGHT +"PLAYER'S HAND")
    print (Fore.RED + Style.BRIGHT + "==============")
    print(*[Fore.YELLOW + Style.BRIGHT + ''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')
    checktotal = 0
    for card in playerCards:
        checktotal = checktotal + card.cardValue
    print(Fore.YELLOW + Style.BRIGHT + f"Total: {checktotal}\n\n")

#Prints dealer cards
def dealerCardsToString(dealerCards):
    strings = []
    for i in range(len(dealerCards)):
        strings.append(dealerCards[i].cardImage)
    #Stackoverflow solution to printing multiple line strings next to each other
    print(Fore.RED + Style.BRIGHT +"DEALER'S HAND")
    print (Fore.RED + Style.BRIGHT + "==============")
    print(*[Fore.YELLOW + Style.BRIGHT +''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')
    checktotal = 0
    for card in dealerCards:
        checktotal = checktotal + card.cardValue
    print(Fore.YELLOW + Style.BRIGHT + f"Total: {checktotal}")

titles.printTitle() #Prints intro sequence

while True:
    os.system('cls')
    
    #Main Menu
    print(Fore.YELLOW + Style.DIM+titles.maintitle2)
    print(Fore.YELLOW + Style.DIM+"============================================================================\n\n\n\n\n\n\n")
    print("     Commands:\n      1. Play\n       2. Load\n        3. Rules\n         4. Quit")
    
    command = input("Type number + enter:\n")
    
    if command == "1":#(Play)
        #TODO: See if cards can be printed in center of console
        #TODO: See if dealcardPlayer and dealcardDealer need to be 2 separate functions
        #TODO: Need to make var for player deposit/dealer deposit so player wins if dealer deposit == 0 
        #and dealer wins if player deposit == 0. Make minimun bet for each round. Implement double and surrender
        os.system('cls')
        
        #Initialize deck for the round
        deck = cards.CardDeck() 
        playerCards = []
        dealerCards = []

        #First hand
        playerCards = dealcardPlayer(playerCards, dealerCards, deck)
        playerCards = dealcardPlayer(playerCards, dealerCards, deck)
        dealerCards = dealcardDealer(playerCards, dealerCards, deck)
        dealerCards = dealcardDealer(playerCards, dealerCards, deck)
        playerCardsToString(playerCards)
        print(Fore.RED + Style.BRIGHT + "DEALER'S HAND")
        print (Fore.RED + Style.BRIGHT + "==============")
        hiddenCard = """.----------.
|  /\_/\ ( |
| ( ^.^ )_)|
|   \\"/ (  |
| ( | | )  |
|(__d b__) |
|          |
`----------'"""
        strings = [dealerCards[0].cardImage, hiddenCard]
        print(*[Fore.YELLOW + Style.BRIGHT +''.join(x) for x in zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings])], sep='\n')
   
        
        total = 0
        #Check if anyone has blackjack 
        #TODO: If anyone has blackjack need to stop game
        if dealerCards[0].cardValue + dealerCards[1].cardValue == 21 and playerCards[0].cardValue + playerCards[1].cardValue == 21:
            print("You both have blackjack, it's a push")
        elif dealerCards[0].cardValue + dealerCards[1].cardValue == 21:
            print ("Dealer has blackjack, you lose")
        elif playerCards[0].cardValue + playerCards[1].cardValue == 21:
            print ("Blackjack! You win")
        
        #Blackjack game commands   
        #TODO: write code so that Ace value == 1 if total more than 21 
        while True:
            command = input()
            if command == "hit":#NYI
                os.system('cls')
                playerCards = dealcardPlayer(playerCards, dealerCards, deck)
                playerCardsToString(playerCards)
                dealerCardsToString(dealerCards)
                #Calculate total
                

            elif command == "stand":
                os.system('cls')
                #Shows dealers hidden card
                playerCardsToString(playerCards)
                dealerCardsToString(dealerCards)
                #If dealer points less than 17, dealer takes card
                checktotal = 0
                while checktotal < 17:
                    checktotal = 0
                    for card in dealerCards:
                        checktotal = checktotal + card.cardValue
                    if checktotal < 17:
                        dealerCards = dealcardDealer(playerCards, dealerCards, deck)
                        os.system('cls')
                        playerCardsToString(playerCards)
                        dealerCardsToString(dealerCards)
                



            elif command == "double":#NYI
                ()
            elif command == "surrender":#NYI
                ()
            elif command == "save":#NYI
                ()
            elif command == "exit":
                break

    
    elif command == "2":#NYI (Load)
        ()
    elif command == "3":#NYI (Rules)
       ()  
    elif command == "4":#(Quit)
        break
    else: 
        print ("input correct command")

