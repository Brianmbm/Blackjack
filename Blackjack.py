
import cards
import time
import os
import titles
import random
import colorama
from colorama import Fore, Back, Style
import datetime
from datetime import date


colorama.init(autoreset=True)#Resets color for every string printed

#Deal one card to player or dealer
def dealcard(playerCards, dealerCards, deck, addtoHand):
    while True:
        index = random.randint(0, 51)
        if deck.deck[index] not in playerCards and deck.deck[index] not in dealerCards:
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


#Hide one dealer card before player stands
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

#Calculate value of all cards
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

#Checks winner, prints statement, then changes balance
def checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance):
    if playertotal > 21:
        print(Fore.RED + Style.BRIGHT+"  Bust! Dealer wins.")
        playerbalance -= bet
        dealerbalance += bet
    elif playertotal == 21 and dealertotal != 21:
        print (Fore.GREEN + Style.BRIGHT+"  Blackjack! You win")
        #0.5 added so it doesnt round down when betting odd and converting to int
        winnings = bet * 3/2+0.5
        winnings = int(winnings)
        playerbalance += winnings
        dealerbalance -= winnings
    elif dealertotal > 21:
        print (Fore.GREEN + Style.BRIGHT+"  You win!")
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal == dealertotal:
        print(Fore.RED + Style.BRIGHT+"  Push, nobody wins")
    elif playertotal > dealertotal:
        print(Fore.GREEN + Style.BRIGHT+"  You win!")
        playerbalance += bet
        dealerbalance -= bet
    elif playertotal < dealertotal:
        print(Fore.RED + Style.BRIGHT+"  You lose!")
        playerbalance -= bet
        dealerbalance += bet
    waitforresponse = input("  Press enter to continue")
    return playerbalance, dealerbalance  
def printBalance():
    print(Fore.YELLOW + f"  Bet:"+ Fore.GREEN +f"{bet}$"+Fore.YELLOW +"   Player's funds:"+ Fore.GREEN +f"{playerbalance}$"+Fore.YELLOW +"    Dealer's funds:"+ Fore.GREEN +f"{dealerbalance}$\n")
playhand = "  PLAYER'S HAND"
dealhand = "  DEALER'S HAND"

#Dealer pulls card as long as dealer's total less than 17 or less than player
def dealerTurn(playerCards, dealerCards, deck, playerbalance, dealerbalance, bet, playhand, dealhand):
    dealertotal, playertotal = calculateTotal(dealerCards, playerCards)
    while dealertotal < 17:
        dealerCards = dealcard(playerCards, dealerCards, deck, dealerCards)
        time.sleep(0.5)
        os.system('cls')
        printBalance()
        cardsToString(playerCards, playhand)
        cardsToString(dealerCards, dealhand)
        dealertotal, playertotal = calculateTotal(dealerCards, playerCards)
    
    titles.gameMenu()
    dealertotal, playertotal = calculateTotal(dealerCards, playerCards)
    playerbalance, dealerbalance = checkWinner(dealertotal, playertotal, bet, playerbalance, dealerbalance)
    return playerbalance, dealerbalance
def loadGame():
    fhand = open('saves.txt', 'r')
    saves = fhand.read()
    fhand.close()
    saveline = saves.split('\n')
    savename = []
    playertotlist = []
    dealertotlist = []
    index = 0
    os.system('cls')
    print("\n\n\n\n\n")
    for line in saveline:
        nameandtotals = line.split(' ')
        savename.append(nameandtotals[0])
        playertotlist.append(int(nameandtotals[1]))
        dealertotlist.append(int(nameandtotals[2]))
        print(Fore.YELLOW + f"          {index+1}. {savename[index]} (Player: {playertotlist[index]}, Dealer: {dealertotlist[index]})")
        index = index + 1
    while True:
        loadsave = input("          Write number and press enter:")
        try:
            loadsave = int(loadsave)
            playerbalance = playertotlist[loadsave-1]
            dealerbalance = dealertotlist[loadsave-1]
            break
        except:
            print(Fore.RED + "Invalid input! Please enter a valid number.")
    return playerbalance, dealerbalance
def saveGame(playerbalance, dealerbalance):
        print(Fore.YELLOW + "         Save name: ")
        saveName = input("         ")
        saveName = saveName.strip()
        saveName = saveName.replace(" ","_")
        today = date.today()
        filehand = open('saves.txt', 'a')
        filehand.write("\n")
        filehand.write(str(today)+"_"+saveName + " " + str(playerbalance) + " " + str(dealerbalance))
        filehand.close()
        print("         Game saved successfully.")
        time.sleep(2)
        exitaftersave = True
        return exitaftersave
def checkBet():
    wantsave = False
    while True:
        try:
            #Bet 
            print(Fore.YELLOW + "\n\n\n\n\n\n         Player's balance: "+ Fore.GREEN +f"{playerbalance}$"+ Fore.YELLOW +"    Dealer's balance: "+Fore.GREEN +f"{dealerbalance}$")
            print(Fore.YELLOW + "         How much do you want to bet? Write 0 to save and exit.")
            bet = int(input(Fore.GREEN +"         "))
            if bet < 0:
                print(Fore.RED +"         Minimum bet is 1$.")
                time.sleep(1)
                os.system('cls')
            elif bet > playerbalance:
                print(Fore.RED +"         Cannot bet more than available funds.")
                time.sleep(1)
                os.system('cls')
            elif bet > dealerbalance:
                print(Fore.RED +"         Cannot bet more than dealer's available funds.")
                time.sleep(1.5)
                os.system('cls')
            elif bet == 0:
                wantsave = True
                break
            else:
                break
        except ValueError:
            print(Fore.RED + "         Invalid input! Please enter a valid number.")
            time.sleep(1)
            os.system('cls')
    return wantsave, bet


#MAIN
  #TODO: Find code to take command as Key press down instead of enter. 
  #keyboard module an option, but refreshes too much, makes game glitchy
  #TODO: low prio. card strings become scrambled if console size becomes smaller
  # than the size/amount of cards displayed. Check for module to start terminal at specific size

titles.printTitle() #Prints intro sequence
while True:
    #Menu
    os.system('cls')
    titles.firstMenu()
    
    command = input(Fore.YELLOW + "          Type number + enter:\n          ")

    #Game always starts with för player 50 and 100 for dealer in balance
    playerbalance = 50
    dealerbalance = 100

    if command == "1" or command == "2":
        
        #(Load)
        if command == "2":
            playerbalance, dealerbalance = loadGame()
            
        #(Play)
        elif command == "1":
            pass 
        exitaftersave = False
        while command != "q" and exitaftersave == False:
            
            os.system('cls')
            #Game over
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
                
                #Bet amount
                wantsave, bet = checkBet()

                #Save 
                if wantsave == True:
                    exitaftersave = saveGame(playerbalance, dealerbalance)


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
                if exitaftersave == False:
                    os.system('cls')
                    printBalance()
                    cardsToString(playerCards, playhand)
                    time.sleep(0.5)
                    hiddenCardsToString(dealerCards)
                    time.sleep(0.5)
                    titles.gameMenu()
        
                #Check if anyone has blackjack from the start
                dealertotal, playertotal = calculateTotal (dealerCards, playerCards) 
                while True and exitaftersave == False:
                    if playertotal == 21 or dealertotal == 21:
                        os.system('cls')
                        printBalance()
                        cardsToString(playerCards, playhand)
                        cardsToString(dealerCards, dealhand)
                        playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                        break
                   #Blackjack game commands  
                    else:
                        command = input(Fore.YELLOW +"  Command:")

                        if command == "w": #hit
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
                                break
                            elif playertotal == 21:
                                playerbalance, dealerbalance = dealerTurn(playerCards, dealerCards, deck, playerbalance, dealerbalance, bet, playhand, dealhand)
                                break
                            else:
                                continue

                        elif command == "s":#stand:
                            os.system('cls')
                            #Shows dealers hidden card
                            printBalance()
                            cardsToString(playerCards, playhand)
                            cardsToString(dealerCards, dealhand)
                            playerbalance, dealerbalance = dealerTurn(playerCards, dealerCards, deck, playerbalance, dealerbalance, bet, playhand, dealhand)
                            break

                        
                        elif command == "d":#double
                            if bet*2 > playerbalance:
                                print(Fore.RED + "  Not enough in balance to double!")
                                time.sleep(1)
                                os.system('cls')
                                printBalance()
                                cardsToString(playerCards, playhand)
                                hiddenCardsToString(dealerCards)
                                titles.gameMenu()

                            else:
                                os.system('cls')
                                bet = bet*2
                                playerCards = dealcard(playerCards, dealerCards, deck, playerCards)
                                cardsToString(playerCards, playhand)
                                hiddenCardsToString(dealerCards)
                                titles.gameMenu()
                                time.sleep(0.5)
                                dealertotal, playertotal = calculateTotal (dealerCards, playerCards)
                                if playertotal > 21:
                                    playerbalance, dealerbalance = checkWinner (dealertotal, playertotal, bet, playerbalance, dealerbalance)
                                    break
                                else:
                                    playerbalance, dealerbalance = dealerTurn(playerCards, dealerCards, deck, playerbalance, dealerbalance, bet, playhand, dealhand)
                                    break
                        elif command == "q":#(quit):
                            break

                        else:
                            os.system('cls')
                            printBalance()
                            cardsToString(playerCards, playhand)
                            hiddenCardsToString(dealerCards)
                            titles.gameMenu()
                            print(Fore.RED+"  Invalid command!")

    elif command == "3":#(Rules)
        os.system('cls')
        titles.gameRules() 
        command = input()
    elif command == "4":#(Quit)
        os.system('cls')
        print("Game exited")
        break
    else: 
        print (Fore.RED + "          Invalid command!")
        time.sleep(1)

