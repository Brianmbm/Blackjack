
import cards
import time
import os
import titles
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)#Resets color for every string printed

#Deal one card to player
def dealcard(playerCards, dealerCards, deck, addtoHand):
    while True:
        index = random.randint(0, 51)
        if deck.deck[index] not in playerCards or dealerCards:
            addtoHand.append(deck.deck[index])
            break
    return addtoHand

#TODO: CardsToString functions might be refactorable into one
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
    #Stackoverflow solution to printing multiple-line strings next to each other.
    print(*[Fore.YELLOW + Style.BRIGHT + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + Style.BRIGHT + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
    print(Fore.YELLOW + Style.BRIGHT + f"Total: {dealertotal}")

#Prints dealer cards before player stands
def hiddenCardsToString(dealerCards):
    print(Fore.RED + Style.BRIGHT + "DEALER'S HAND")
    print (Fore.RED + Style.BRIGHT + "==============")
    hiddenCard = """.----------.
|  /\_/\ ( |
| ( ^.^ )_)|
|   \\"/ (  |
| ( | | )  |
|(__d b__) |
|~~~~~~~~~~|
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
    #TODO: Find code to take command as Key press down instead of enter
    #Menu
    os.system('cls')
    titles.firstMenu()
    
    command = input(Fore.YELLOW + "          Type number + enter:\n          ")
    
    if command == "1":#(Play)
        #TODO: See if cards can be printed in center of console
        #TODO: See if dealcardPlayer and dealcardDealer need to be 2 separate functions or can it be one?
        #TODO: Need to make var for player deposit/dealer deposit so player wins if dealer deposit == 0 
        #and dealer wins if player deposit == 0. Make minimun bet for each round. Implement double and surrender
        #TODO: Fix commands during game
        #FIXME: low prio. card strings become scrambled if console size becomes smaller than the size/amount of cards displayed
        
        while command != "q":
            os.system('cls')
            #Initialize deck for the round
            deck = cards.CardDeck()
        
            playerCards = []
            dealerCards = []

            #First hand
            playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
            playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
            dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
            dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)

            #Prints the player's hand and the dealer's with a hidden card and the commands menu
            playerCardsToString(playerCards)
            hiddenCardsToString(dealerCards)
            titles.gameMenu()

        
            #Check if anyone has blackjack from the start
            #TODO: If anyone has blackjack need to stop game
        

            #Blackjack game commands   
            while True:
                command = input(Fore.YELLOW + Style.BRIGHT +"Command:")
                
                
                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                if playertotal > 21 or dealertotal > 21:
                    playerCardsToString(playerCards)
                    hiddenCardsToString(dealerCards)
                    checkWinner (dealertotal, playertotal)

                #TODO: Check if need to add time.sleep to more places for better flow
                elif command == "w": #(hit)" NYI
                    os.system('cls')
                    playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                    playerCardsToString(playerCards)
                    hiddenCardsToString(dealerCards)
                    titles.gameMenu()
                    #Calculate total
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    if playertotal >= 21:
                        checkWinner (dealertotal, playertotal)
                        time.sleep(4)
                        break
                    else:
                        continue
                    #TODO: game needs to end once player stands
                elif command == "s":#(stand):
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
                            dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                            os.system('cls')
                            playerCardsToString(playerCards)
                            dealerCardsToString(dealerCards)
                    titles.gameMenu()
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    checkWinner (dealertotal, playertotal)
                    
                    time.sleep(4)
                    break
                



                elif command == "d": #double":#NYI
                    ()
                elif command == "save":#NYI
                    ()
                elif command == "q":#(quit):
                    break
                else:
                    os.system('cls')
                    #Shows dealers hidden card
                    playerCardsToString(playerCards)
                    hiddenCardsToString(dealerCards)
                    titles.gameMenu()
                    print(Fore.RED+"invalid command")

    
    elif command == "2":#NYI (Load)
        ()
    #TODO: shorten rules or create two pages
    #TODO: add rules about bets once deposit implemented
    elif command == "3":#NYI (Rules)
       os.system('cls')
       titles.gameRules() 
       command = input()
    elif command == "4":#(Quit)
        break
    else: 
        print ("input correct command")

