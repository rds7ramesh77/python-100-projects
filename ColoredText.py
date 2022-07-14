#Python Program To print Coloured text

""" For this we need to import colorama module"""


import colorama 

from colorama import Fore,Back,Style 
colorama.init(autoreset=True)
print(Fore.BLUE+Back.YELLOW+"Hello My name is Ramesh Sapkota"+Fore.YELLOW+Back.BLUE+"I am Tyour Python Instructor")

print(Back.CYAN+"My fav Football Player is Cristiano Ronaldo")

print(Fore.RED+Back.BLACK+"Do you watch Football??")