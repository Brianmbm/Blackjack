
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

#Prints cards
def cardsToString(cards, title):
    strings = []
    for i in range(len(cards)):
        strings.append(cards[i].cardImage)
    print(Fore.RED + Style.BRIGHT + title)
    print(Fore.RED + Style.BRIGHT + "==============")
    #Stackoverflow solution to printing multiple-line strings next to each other
    print(*[Fore.YELLOW + Style.BRIGHT + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + Style.BRIGHT + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
    
    if title == "PLAYER'S HAND":
        dealertotal, playertotal = calculateTotal([],cards)
        print(Fore.YELLOW + Style.BRIGHT + f"Total: {playertotal}\n")
    else:
        dealertotal, playertotal = calculateTotal(cards,[])
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

def checkWinner (dealertotal, playertotal, bet, playerfunds, dealerfunds):
    if playertotal > 21:
        print(Fore.RED + Style.BRIGHT+"Bust! Dealer wins.")
        playerfunds -= bet
        dealerfunds += bet
    elif playertotal == 21 and dealertotal != 21:
        print (Fore.GREEN + Style.BRIGHT+"Blackjack! You win")
        playerfunds += bet
        dealerfunds -= bet
    elif dealertotal > 21:
        print (Fore.GREEN + Style.BRIGHT+"You win!")
        playerfunds += bet
        dealerfunds -= bet
    elif playertotal == dealertotal:
        print(Fore.RED + Style.BRIGHT+"Push, nobody wins")
    elif playertotal > dealertotal:
        print(Fore.GREEN + Style.BRIGHT+"You win!")
        playerfunds += bet
        dealerfunds -= bet
    elif playertotal < dealertotal:
        print(Fore.RED + Style.BRIGHT+"You lose!")
        playerfunds -= bet
        dealerfunds += bet
    return playerfunds, dealerfunds   


#MAIN

titles.printTitle() #Prints intro sequence
while True:
    #TODO: Find code to take command as Key press down instead of enter
    #Menu
    os.system('cls')
    titles.firstMenu()
    
    command = input(Fore.YELLOW + "          Type number + enter:\n          ")
    playerfunds = 50
    dealerfunds = 50
    if command == "1":#(Play)
        #TODO: Need to make var for player deposit/dealer deposit so player wins if dealer deposit == 0 
        #and dealer wins if player deposit == 0. Make minimun bet for each round. Implement double and surrender
        #TODO: Fix commands during game
        #FIXME: low prio. card strings become scrambled if console size becomes smaller than the size/amount of cards displayed
        #FIXME: When inputting wrong command funds reset


        while command != "q":
            os.system('cls')
            print(f"Player's funds:{playerfunds}$    Dealer's funds:{dealerfunds}$")
            #TODO: Change text so it doesnt print minimum twice when wrong input
            while True:
                try:
                    bet = int(input(Fore.YELLOW + "Minimum bet is 1$.\nHow much do you want to bet?\n"))
                    if bet < 1 or bet > playerfunds:
                        print("Minimum bet is 1$. Cannot bet more than available funds.")
                    
                    else:
                        break
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a valid number.")

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
            os.system('cls')
            print(Fore.YELLOW + Style.BRIGHT+f"Bet:{bet}$   Player's funds:{playerfunds}$    Dealer's funds:{dealerfunds}$\n")
            cardsToString(playerCards, "PLAYER'S HAND")
            time.sleep(0.5)
            hiddenCardsToString(dealerCards)
            time.sleep(0.5)
            titles.gameMenu()
        
            #TODO: print funds after hitting or standing
            #Blackjack game commands   
            while True:
                command = input(Fore.YELLOW + Style.BRIGHT +"Command:")
                
                #Check if anyone has blackjack from the start
                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                if playertotal > 21 or dealertotal > 21:
                    cardsToString(playerCards, "PLAYER'S HAND")
                    hiddenCardsToString(dealerCards)
                    playerfunds, dealerfunds = checkWinner (dealertotal, playertotal, bet, playerfunds, dealerfunds)
                    time.sleep(4)
                    break

                #TODO: Check if need to add time.sleep to more places for better flow
                elif command == "w": #(hit)" NYI
                    os.system('cls')
                    playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                    cardsToString(playerCards, "PLAYER'S HAND")
                    hiddenCardsToString(dealerCards)
                    titles.gameMenu()
                    #Calculate total
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    if playertotal >= 21:
                        playerfunds, dealerfunds = checkWinner (dealertotal, playertotal, bet, playerfunds, dealerfunds)
                        time.sleep(4)
                        break
                    else:
                        continue

                elif command == "s":#(stand):
                    os.system('cls')
                    #Shows dealers hidden card
                    cardsToString(playerCards, "PLAYER'S HAND")
                    cardsToString(dealerCards, "DEALER'S HAND")

                    #If dealer points less than 17, dealer takes card
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    while dealertotal < 17:
                        dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                        os.system('cls')
                        cardsToString(playerCards, "PLAYER'S HAND")
                        cardsToString(dealerCards, "DEALER'S HAND")
                        dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    titles.gameMenu()
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    playerfunds, dealerfunds = checkWinner (dealertotal, playertotal, bet, playerfunds, dealerfunds)
                    
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
                    cardsToString(playerCards, "PLAYER'S HAND")
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

