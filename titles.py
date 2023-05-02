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