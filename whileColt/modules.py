from random import choice as pick, randint as magic_number_chooser

print(pick(["apple", "banana", "cherry", "durian"]))
print(magic_number_chooser(1,100))
#*_______________________________________________________________________

import math

answer = math.sqrt(15129)
print(answer)
#*_______________________________________________________________________

import keyword

def contains_keyword(*args):
    return any([keyword.iskeyword(i) for i in args])

print(contains_keyword('def', 'haha', 'lol','bolod'))
print(contains_keyword('hi', 'hello', 'bye','bye'))
#*_______________________________________________________________________

import bananas
import apples

print(bananas.peel())
print(bananas.dip_in_chocolate())
print(apples.offer())
print(apples.bake())
#*_______________________________________________________________________

from termcolor import colored

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)
#*_______________________________________________________________________

from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "cyan"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)