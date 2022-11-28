# Collaboration Google Doc
# https://docs.google.com/document/d/18BcuCWor4hgtS_EwAWBTJOp9TZmFc8nn81btmvg1E-Y/edit?usp=sharing

"""
TODO
- B)-|--<
- ^ That's a pretty cool dude
- Thank you his name is Louis
- 3DS / Switch port

INFO
- Carlos (Carlos Sandchez) is a reoccurring friend character for the crab now

MULTIPLE DAYS
- There are two different methods for adding multiple days
MULTIDAYS
- To make a "multiday", just make a folder in the "days/" folder with 1.py, 2.py. etc. inside
- The days will be executed in that order
CHAINDAYS
- To make a "chainday", add the following line to the bottom of an existing day:
		queue.insert(0, "$chainDays.file.py")
- This will insert the file "file.py" located in "days/$chainDays/" to the front of the queue
- If you want to put it in a random position, you can just random.shuffle(queue) after insertion

COLORS
- Informational text is "dim"
- Narrator speech is "green"
- Character's speech is "cyan"
- Other character's speech are "yellow", "blue", and "purple" in that order
- Onomonopoeia and other sounds are "red"
- God and stat level ups are "rainbow"
- Use "rainbow" and "white" very sparingly
"""

# lot of imports
from waterWorks import fprint, choice, clear, pause
import waterWorks as config
from colorama import Fore, Style
import time, random, os, sys, importlib
from days import days as days

# game loop function
def game():
	# generates a queue of days
	queue = config.generateQueue()
	while True:
		pause()
		#
		# please and thanks
		# DON'T TOUCH THIS SHIT ZONE START
		# please and thanks
		#
		dayModule = queue[0]
		if not dayModule.endswith(".py"):
			queue.pop(0)
			for d in reversed(days[dayModule]):
				queue.insert(0, d)
		day = queue.pop(0)
		config.days += 1 # increment days by 1
		clear()
		fprint("DAY " + str(config.days) + "\n", "white", 1, 0) # display beginning of day text
		days[day](queue)
		if len(queue) == 0 and config.state == 0: # if there aren't any days left and you haven't died, set state to win
			config.state = -1
		if config.state != 0:
			# if it's not 0, you're either in win condition or dead
			pause()
			break # break out of game loop
		#
		# please and thanks
		# DON'T TOUCH THIS SHIT ZONE OVER
		# please and thanks
		#
	#clear() #add back at some point
	if config.state == -1:
		# win game here
		clear()
		config.days += 1
		fprint("DAY " + str(config.days) + "\n", "white", 1, 0)
		fprint("Damn, you actually made it.\n", "green", 2)
		fprint("Huh? Where am I?\n", "cyan")
		fprint("You're at the end of the game. You finished all of the trials I put you through.", "green")
		fprint("You may rest now.\n", "green", 2)
		fprint("...", "cyan", 1)
		fprint("I don't want to. I still have so much to do as a crab.\n", "cyan", 1)
		fprint("Really? I've never had this happen to me before... I'll tell you what, kid. You wanna become a narrator?\n", "green")
		answer = choice(["Yes", "No"])
		if answer == 1:
			fprint("I accept.\n", "green")
			fprint("Thank you. I can ascend now. I shall see you again soon.\n", "white", 1)
			fprint("Where are you going?", "green", 2)
			fprint("...", "green", 3)
			fprint("Oh, and thanks for playing through this whole thing as me. You saved me a whole lot back there.", "green", 2)
			fprint("I guess I should be going as well. See ya.\n", "green", 4)
		else:
			fprint("Thanks for the offer, but I refuse.\n", "cyan")
			fprint("I can't blame you.", "green", 1)
			fprint("Goodbye for now. I shall see you again soon.\n", "green", 1)
			fprint("Where are you going?", "cyan", 2)
			fprint("...", "cyan", 3)
			fprint("Oh, and thanks for playing through this whole thing as me. You saved me a whole lot back there.", "cyan", 2)
			fprint("I guess I should be going as well. See ya.\n", "cyan", 4)
		pause()
		clear()
		time.sleep(2)
		fprint("Thanks for playing Crab Simulator (2020)!\n", "yellow", 3)
		fprint("STATS:", "white", 1)
		fprint("Total days : " + str(config.days), "white", 1)
		fprint("Experience : " + str(config.experience), "white", 1)
		fprint("Overall Kindness : " + str(config.personality) + "\n", "white", 1)
		if config.personality > 0: # this is God speaking
			fprint("Those were some pretty nice choices back there. Good job.\n", "rainbow", 3)
		else:
			fprint("Those weren't some pretty nice choices back there. Not cool, dude.\n", "rainbow", 3)
		fprint("Hope you liked our game. Gotta run now, bye.\n", "yellow", 5)
		pause()
		# program end

	else:
		# death screen
		clear()
		fprint("You died.\n", "red", 2, 0)
		fprint("Ending " + config.state[len(config.state) - 2:] + "\n", "green", 1, 0)
		fprint(config.state[:-2] + "\n", "green", 1)
		fprint("Congrats, you made it " + str(config.days) + " " + config.dayPlural() + ".\n", "green", 2)
		pause()
		titleScreen() # return to title screen

# small intro that plays before game starts
def intro():
	clear()
	fprint("Welcome!\n", "green", 1)
	fprint("You've died tragically " + config.randomDeath() + ".\n", "red", 1.5)
	if random.randint(1, 4) == 4:
		fprint("LucKRILLy...", "green", 1)
		fprint("haha did you get it", "dim", 0, 0.02)
	else:
		fprint("Luckily...", "green", 1)
	fprint("You've been reincarnated as a crab!", "green", 1)
	fprint("There's a lot to do as a crab these days, so strap in and enjoy the ride!\n", "green", 2)
	# reset all the variables
	config.days = 0
	config.experience = 0
	config.personality = 0
	config.state = 0
	game() # starts game loop

# credits cutscene(ish)
def credits():
	clear()
	fprint("Made by Jacob Johnson and Roger Cronin\n", "green", 1)
	fprint("Shoutout to RomeroShwarz and their 1300s Peasant Simulator for insipration\n", "green", 1)
	fprint("Shoutout https://en.wikipedia.org/wiki/Crab\n", "green", 1)
	fprint("Crab art by tre\n", "green", 1)
	fprint("A bunch of people who tested and probably don't want their names on this\n", "green", 1)
	fprint("And you, gamer.", "green", 1)
	fprint("*mwha*", "green", 3)
	titleScreen()

# start here
def titleScreen():
	clear()
	print(Fore.LIGHTRED_EX + """
   /\\
  ( /   @ @    ()
   \\  __| |__  /
    -/   "   \\-
   /-|       |-\\
  / /-\\     /-\\ \\
   / /-`---'-\\ \\
    /         \\
  \n""") # print some ascii art
	time.sleep(2)

	fprint("Welcome to Crab Simulator (2020)!\n", "yellow", 1.5)

	fprint(config.randomGreeting(), "green")
	fprint("Select an option pleeeaase\n", "green")

	answer = choice(["New Game", "Credits"])

	fprint(config.randomAgree() + "\n", "green", 2)

	if answer == 1: # new game
		intro()
	else: # credits
		credits()

# if you're in debug, skip the beginning menus
if config.debug:
	game()
else:
	titleScreen()
