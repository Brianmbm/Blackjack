import os
import time
import colorama
from colorama import Fore, Back, Style


#strings used in initial sequence

heart = """\n\n\n    .-~~~-__-~~~-.
   {              }
    `.          .'
      `.      .'
        `.  .'
          \/\n\n\n\n\n\n\n\n\n\n\n\n
												   .-~~~-__-~~~-.
												  {              }
												   `.          .'
												     `.      .'
												       `.  .'
												         \/"""

spade = """\n\n\n\n 		        /\\
  		      .'  `.
		     '      `.
		  .'          `.
		 {              }
		  ~-...-||-...-~
		        ||
		       '--`\n\n\n\n\n\n
										/\\
							 		      .'  `.
									     '      `.
									  .'          `.
									 {              }
									  ~-...-||-...-~
									        ||
									       '--`"""
diamond = """\n\n\n\n\n\n				    /\\
 				  .'  `.
				 '      `.
			       <          >
 				`.      .'
  				  `.  .'
  				    \/\n\n
								    /\\
				 				  .'  `.
								 '      `.
							       <          >
				 				`.      .'
				 				  `.  .'
				  				    \/"""
clubs = """\n\n\n\n\n\n\n 					      .-~~-.
 					     {      }
				          .-~-.    .-~-.
				         {              }
 					  `.__.'||`.__.'
				                ||
 					       '--`\n
						      .-~~-.
	    					     {      }
	   				          .-~-.    .-~-.
	   				         {              }
	    					  `.__.'||`.__.'
	   				                ||
	    					       '--`"""
maintitle = """		    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
		    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
		    ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
		    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
		    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
		    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝@Brianmbm"""
maintitle2 = Fore.YELLOW + Style.NORMAL +"""\n\n	██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
	██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
	██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
	██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
	██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
	╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝"""
spaces = "\n\n\n\n\n\n\n\n\n\n"

gameover = Fore.RED + Style.DIM + """\n\n\n\n\n\n\n\n		..######......###....##.....##.########.....#######..##.....##.########.########.
		.##....##....##.##...###...###.##..........##.....##.##.....##.##.......##.....##
		.##.........##...##..####.####.##..........##.....##.##.....##.##.......##.....##
		.##...####.##.....##.##.###.##.######......##.....##.##.....##.######...########.
		.##....##..#########.##.....##.##..........##.....##..##...##..##.......##...##..
		.##....##..##.....##.##.....##.##..........##.....##...##.##...##.......##....##.
		..######...##.....##.##.....##.########.....#######.....###....########.##.....##"""
youwin = Fore.YELLOW + Style.BRIGHT + """\n\n\n\n	
	   $$\          $$\     $$\                                       $$\           $$\          $$\    
	 $$$$$$\        \$$\   $$  |                                      \__|          $$ |       $$$$$$\  
	$$  __$$\        \$$\ $$  /$$$$$$\  $$\   $$\       $$\  $$\  $$\ $$\ $$$$$$$\  $$ |      $$  __$$\ 
	$$ /  \__|        \$$$$  /$$  __$$\ $$ |  $$ |      $$ | $$ | $$ |$$ |$$  __$$\ $$ |      $$ /  \__|
	\$$$$$$\           \$$  / $$ /  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ |$$ |  $$ |\__|      \$$$$$$\  
	 \___ $$\           $$ |  $$ |  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ |$$ |  $$ |           \___ $$\ 
	$$\  \$$ |          $$ |  \$$$$$$  |\$$$$$$  |      \$$$$$\$$$$  |$$ |$$ |  $$ |$$\       $$\  \$$ |
	\$$$$$$  |          \__|   \______/  \______/        \_____\____/ \__|\__|  \__|\__|      \$$$$$$  |
	 \_$$  _/                                                                                  \_$$  _/ 
	  \ _/                                                                                      \ _/   
	                                                                                                    
"""
#Initial sequence when starting game
def printTitle():
	print(Fore.RED + heart)
	time.sleep(0.5)
	os.system('cls')
	print(Fore.YELLOW + spade)
	time.sleep(0.4)
	os.system('cls')
	print(Fore.MAGENTA + diamond)
	time.sleep(0.4)
	os.system('cls')
	print(Fore.GREEN + clubs)
	time.sleep(0.4)
	os.system('cls')
	print(Fore.YELLOW + spaces + maintitle)
	time.sleep(1.5)

def firstMenu():
	print(maintitle2)
	print(Fore.YELLOW +"     =============================================================================\n\n\n\n")
	print(Fore.YELLOW + "     Commands:\n      1. Play\n       2. Load\n        3. Rules\n         4. Quit\n")

def gameMenu():
	print(Fore.YELLOW + "  w =hit       s = stand\n  d = double    q = quit")

def gameRules():
	print("""Rules of Blackjack
===================

The hand with the highest total wins as long as it doesn't exceed 21. 
A hand with a higher total than 21 is said to bust.
Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10. 
An ace's value is 11 unless this would cause the player to bust, in which case it is worth 1.
The goal of each player is to beat the dealer by having the higher, unbusted hand. 
Note that if the player busts he loses, even if the dealer also busts (therefore Blackjack favors the dealer).
If both the player and the dealer have the same point value, neither win the hand.
The dealer gives two cards to each player, including himself.
One of the dealer's two cards is face-up, and the other is face down.
The play goes as follows:
If the dealer has blackjack and the player doesn't, the player automatically loses.
If the player has blackjack and the dealer doesn't, the player automatically wins.
If both the player and dealer have blackjack then it's a push.
If neither side has blackjack, then the player plays out his hand.
When the player has finished the dealer plays his hand.
The player's options are:
 - Hit: Take another card.
 - Stand: Take no more cards.
 - Double down: Double the wager, take exactly one more card, and then stand.
The player's turn is over after deciding to stand, doubling down to take a single card, or busting.
If the player busts, he or she loses the bet even if the dealer goes on to bust.
After the player has finished making his or her decisions, 
the dealer then reveals his or her hidden hole card and plays the hand. 
House rules say that the dealer must hit until he or she has at least 17, regardless of what the players have."""
)
	print(Fore.RED + "\nPress enter to go back to menu.")