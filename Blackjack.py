
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
    print(*[Fore.YELLOW + Style.BRIGHT + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + Style.BRIGHT + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
    print(Fore.YELLOW + Style.BRIGHT + f"Total: {playertotal}\n\n")

#Prints dealer cards
def dealerCardsToString(dealerCards):
    strings = []
    for i in range(len(dealerCards)):
        strings.append(dealerCards[i].cardImage)
    print(Fore.RED + Style.BRIGHT +"DEALER'S HAND")
    print (Fore.RED + Style.BRIGHT + "==============")
    #Stackoverflow solution to printing multiple line strings next to each other
    print(*[Fore.YELLOW + Style.BRIGHT + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + Style.BRIGHT + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
    print(Fore.YELLOW + Style.BRIGHT + f"Total: {dealertotal}")

#Prints dealer cards before player stands
def hidedealerCard(dealerCards):
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
    print(*[Fore.YELLOW + Style.BRIGHT + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + Style.BRIGHT + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
   
def calculateTotal(dealerCards, playerCards):
    dealertotal = 0
    dealeraces = 0
    for card in dealerCards:
        if card.cardValue == 11:
            dealeraces += 1
        dealertotal += card.cardValue
    while dealeraces > 0 and dealertotal > 21:
        dealertotal -= 10
        dealeraces -= 1
    
    playertotal = 0
    playeraces = 0
    for card in playerCards:
        if card.cardValue == 11:
            playeraces += 1
        playertotal += card.cardValue
    while playeraces > 0 and playertotal > 21:
        playertotal -= 10
        playeraces -= 1
    return dealertotal, playertotal

def checkWinner (dealertotal, playertotal):
    if playertotal > 21:
        print(Fore.RED + Style.BRIGHT+"Bust! Dealer wins.")
    elif playertotal == 21 and dealertotal != 21:
        print (Fore.YELLOW + Style.NORMAL+"Blackjack! You win")
    elif dealertotal > 21:
        print (Fore.YELLOW + Style.NORMAL+"You win!")
    elif playertotal == dealertotal:
        print(Fore.RED + Style.BRIGHT+"Push, nobody wins")
    elif playertotal > dealertotal:
        print(Fore.YELLOW + Style.NORMAL+"You win!")
    elif playertotal < dealertotal:
        print(Fore.RED + Style.BRIGHT+"You lose!")





#MAIN
titles.printTitle() #Prints intro sequence
while True:
    os.system('cls')
    
    #Menu
    print(Fore.YELLOW + titles.maintitle2)
    print(Fore.YELLOW +"     =============================================================================\n\n\n\n")
    print(Fore.YELLOW + "     Commands:\n      1. Play\n       2. Load\n        3. Rules\n         4. Quit\n")
    
    command = input(Fore.YELLOW + "          Type number + enter:\n          ")
    
    if command == "1":#(Play)
        #TODO: See if cards can be printed in center of console
        #TODO: See if dealcardPlayer and dealcardDealer need to be 2 separate functions or can it be one?
        #TODO: Need to make var for player deposit/dealer deposit so player wins if dealer deposit == 0 
        #and dealer wins if player deposit == 0. Make minimun bet for each round. Implement double and surrender
        #TODO: Fix commands during game
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
        hidedealerCard(dealerCards)
        
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
        while True:
            command = input()
            if command == "hit":#NYI
                os.system('cls')
                playerCards = dealcardPlayer(playerCards, dealerCards, deck)
                playerCardsToString(playerCards)
                hidedealerCard(dealerCards)
                #Calculate total
                
                #TODO: game needs to reset once player stands
            elif command == "stand":
                os.system('cls')
                #Shows dealers hidden card
                playerCardsToString(playerCards)
                dealerCardsToString(dealerCards)
                #If dealer points less than 17, dealer takes card
                ##TODO: See if calculateTotal def can be used here
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
                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                checkWinner (dealertotal, playertotal)




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

