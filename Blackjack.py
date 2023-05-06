
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
    print(Fore.RED + Style.BRIGHT + "  ==============")
    #Stackoverflow solution to printing multiple-line strings next to each other
    print(*[Fore.YELLOW + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
    
    if title == "  PLAYER'S HAND":
        dealertotal, playertotal = calculateTotal([],cards)
        print(Fore.YELLOW + "  Total: "+ Fore.GREEN +f"{playertotal}\n")
    else:
        dealertotal, playertotal = calculateTotal(cards,[])
        print(Fore.YELLOW + "  Total: "+ Fore.GREEN +f"{dealertotal}")


#Prints dealer cards before player stands
def hiddenCardsToString(dealerCards):
    print(Fore.RED + Style.BRIGHT + "  DEALER'S HAND")
    print (Fore.RED + Style.BRIGHT + "  ==============")
    hiddenCard = """.----------.
|  /\_/\ ( |
| ( ^.^ )_)|
|   \\"/ (  |
| ( | | )  |
|(__d b__) |
|~~~~~~~~~~|
`----------'"""
    strings = [dealerCards[0].cardImage, hiddenCard]
    print(*[Fore.YELLOW + '   '.join(x) if i > 0 else '   ' + Fore.YELLOW + '   '.join(x) for i, x in enumerate(zip(*[[x.ljust(len(max(s.split('\n'), key=len))) for x in s.split('\n')] for s in strings]))], sep='\n   ')
   
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

def checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance):
    if playertotal > 21:
        print(Fore.RED + Style.BRIGHT+"Bust! Dealer wins.")
        playerbalance -= bet
        dealerbalance += bet
    elif playertotal == 21 and dealertotal != 21:
        print (Fore.GREEN + Style.BRIGHT+"Blackjack! You win")
        winnings = bet * 3/2+bet
        playerbalance += winnings
        dealerbalance -= winnings
    elif dealertotal > 21:
        print (Fore.GREEN + Style.BRIGHT+"You win!")
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal == dealertotal:
        print(Fore.RED + Style.BRIGHT+"Push, nobody wins")
    elif playertotal > dealertotal:
        print(Fore.GREEN + Style.BRIGHT+"You win!")
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal < dealertotal:
        print(Fore.RED + Style.BRIGHT+"You lose!")
        playerbalance -= bet
        dealerbalance += bet
    return playerbalance, dealerbalance   
def printBalance():
    print(Fore.YELLOW + f"  Bet:"+ Fore.GREEN +f"{bet}$"+Fore.YELLOW +"   Player's funds:"+ Fore.GREEN +f"{playerbalance}$"+Fore.YELLOW +"    Dealer's funds:"+ Fore.GREEN +f"{dealerbalance}$\n")
playhand = "  PLAYER'S HAND"
dealhand = "  DEALER'S HAND"
#MAIN

titles.printTitle() #Prints intro sequence
while True:
    #Menu
    os.system('cls')
    titles.firstMenu()
    
    command = input(Fore.YELLOW + "          Type number + enter:\n          ")

    #Game always starts with 50 in balance
    playerbalance = 50
    dealerbalance = 50
    if command == "1":#(Play)

        #TODO: Find code to take command as Key press down instead of enter
        #TODO: Fix print statement when game over/game won
        #FIXME: low prio. card strings become scrambled if console size becomes smaller than the size/amount of cards displayed
        #TODO: Check if need to add time.sleep to more places for better flow
        #TODO: refactor hit/stand code, repeats in double?
        #TODO: wait for input before next round instead of sleep.time?
        #TODO: refactor dealerturn 
        
        while command != "q":
            os.system('cls')
            if playerbalance <= 0 or dealerbalance <= 0:
                if playerbalance <= 0:
                    print(titles.gameover)
                    gameoverinput = input()
                    break
                elif dealerbalance <= 0:
                    print(titles.youwin)
                    gameoverinput = input()
                    break
            else:
                print(Fore.YELLOW + "\n\n\n\n\n\n         Player's balance: "+ Fore.GREEN +f"{playerbalance}$"+ Fore.YELLOW +"    Dealer's balance: "+Fore.GREEN +f"{dealerbalance}$")
                while True:
                    try:
                        print(Fore.YELLOW + "         How much do you want to bet?")
                        bet = int(input(Fore.GREEN +"         "))
                        if bet < 1:
                            print("Minimum bet is 1$.")
                        elif bet > playerbalance:
                            print("Cannot bet more than available funds.")
                        else:
                            break
                    except ValueError:
                        print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a valid number.")

                #Initialize deck for the round
                deck = cards.CardDeck()
        
                playerCards = []
                dealerCards = []

                #Deals first hand
                playerCards = dealcard(playerCards, dealerCards, deck, playerCards) 
                playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)

                #Prints the player's hand and the dealer's with a hidden card and the commands menu
                os.system('cls')
                printBalance()
                cardsToString(playerCards, playhand)
                time.sleep(0.5)
                hiddenCardsToString(dealerCards)
                time.sleep(0.5)
                titles.gameMenu()
        
                #Blackjack game commands   
                while True:
                    command = input(Fore.YELLOW +"  Command:")
                
                    #Check if anyone has blackjack from the start
                    dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                    if playertotal > 21 or dealertotal > 21:
                        printBalance()
                        cardsToString(playerCards, playhand)
                        hiddenCardsToString(dealerCards)
                        playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                        time.sleep(4)
                        break


                    elif command == "w": #(hit)" NYI
                        os.system('cls')
                        playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                        printBalance()
                        cardsToString(playerCards, playhand)
                        hiddenCardsToString(dealerCards)
                        titles.gameMenu()
                        #Calculate total
                        dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        if playertotal > 21:
                            playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                            time.sleep(4)
                            break
                        elif playertotal == 21:
                            while dealertotal < 17 or dealertotal < playertotal:
                                dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                                time.sleep(0.5)
                                os.system('cls')
                                printBalance()
                                cardsToString(playerCards, playhand)
                                cardsToString(dealerCards, dealhand)
                                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                            titles.gameMenu()
                            dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                            playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                            time.sleep(4)
                            break
                        else:
                            continue

                    elif command == "s":#(stand):
                        os.system('cls')
                        #Shows dealers hidden card
                        printBalance()
                        cardsToString(playerCards, playhand)
                        cardsToString(dealerCards, dealhand)

                        #If dealer points less than 17, dealer takes card
                        dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        while dealertotal < 17 or dealertotal < playertotal:
                            dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                            time.sleep(0.5)
                            os.system('cls')
                            printBalance()
                            cardsToString(playerCards, playhand)
                            cardsToString(dealerCards, dealhand)
                            dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        
                        titles.gameMenu()
                        dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                    
                        time.sleep(4)
                        break
                    #TODO: cannot double if bet*2 is more than player balance
                    elif command == "d": #double":#NYI: Double the wager, take exactly one more card, and then stand.
                        os.system('cls')
                        bet = bet*2
                        playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                        cardsToString(playerCards, playhand)
                        hiddenCardsToString(dealerCards)
                        titles.gameMenu()
                        time.sleep(0.5)
                        dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        if playertotal >= 21:
                            playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                            time.sleep(4)
                            break
                        else:
                            while dealertotal < 17:
                                dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
                                time.sleep(0.5)
                                os.system('cls')
                                printBalance()
                                cardsToString(playerCards, playhand)
                                cardsToString(dealerCards, dealhand)
                                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                        
                            titles.gameMenu()
                            dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                            playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                    
                            time.sleep(4)
                            break

                    elif command == "save":#NYI
                        ()

                    elif command == "q":#(quit):
                        break

                    else:
                        os.system('cls')
                        cardsToString(playerCards, playhand)
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

