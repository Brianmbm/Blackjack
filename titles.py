import os
import time
import colorama
from colorama import Fore, Back, Style

#strings used in initial sequence

heart = """\n\n .-~~~-__-~~~-.
{              }
 `.          .'
   `.      .'
     `.  .'
       \/"""

spade = """\n\n\n		       /\\
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
  				    \/"""
clubs = """\n\n\n\n\n\n\n\n\n 					    .-~~-.
 					   {      }
				        .-~-.    .-~-.
				       {              }
 					`.__.'||`.__.'
				              ||
 					     '--`"""
maintitle = """			██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
			██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
			██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
			██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
			██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
			╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝"""
maintitle2 = """\n\n	██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
	██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
	██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
	██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
	██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
	╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝"""
spaces = "\n\n\n\n\n\n\n\n\n\n"

#Initial sequence when starting game
def printTitle():
	print(Fore.RED + heart)
	time.sleep(0.5)
	os.system('cls')
	print(Fore.YELLOW + spade)
	time.sleep(0.5)
	os.system('cls')
	print(Fore.MAGENTA + diamond)
	time.sleep(0.5)
	os.system('cls')
	print(Fore.GREEN + clubs)
	time.sleep(0.5)
	os.system('cls')
	print(Fore.YELLOW + spaces + maintitle)
	time.sleep(1)

def firstMenu():
	print(Fore.YELLOW + maintitle2)
	print(Fore.YELLOW +"     =============================================================================\n\n\n\n")
	print(Fore.YELLOW + "     Commands:\n      1. Play\n       2. Load\n        3. Rules\n         4. Quit\n")

def gameMenu():
	print(Fore.YELLOW + Style.BRIGHT + "Commands:\nw = hit       s = stand        a = surrender\nd = double    q = quit\n")
