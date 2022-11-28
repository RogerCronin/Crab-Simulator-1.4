# print("If you're seeing this, then some modules didn't load.\nThis is unfortunately a bug with Repl.it, and we cannot do anything to fix it.\n")

# utilities haha, get it? funny bc water works
# also water haha, get it? funny bc crabs live in that

# imports a lot of things
from colorama import Fore, Style
from itertools import cycle
import textwrap as textWrap
import time, sys, random, os

""" LIST OF DEATHS
01 - depression.py Crab suicide
02 - burnWitch.py Burnt to a crisp
03 - oldGuyDrugs.2.py Oyster-piod overdose
04 - $chainDays.cringeNarrator.py Cringed to death
05 - oldGuyDrugs.2.py M'shark-er fume overdose
06 - robberyTime.3.py Buff crab beat up
07 - oldGuyDrugs.2.py Apartment flooding
08 - $chainDays.crabExamDeath.py Not licensed to crab
09 - cookingCompetition.py Automobile gakked you
10 - $chainDays.presidentStay.py Assassination
11 - fisherman.py Cooked and eaten
12 - quarantineVibes.1.py Going outside
13 - prisonersDilemma.py Prison time
"""

# variables
debug = False # true when you want to skip menus
days = 0 # number of days
experience = 0 # exp level
personality = 0 # positive = good, negative = bad
state = 0 # 0 = alive, -1 = win, string = death message
message = 0 # used to communicate short term between days, typically used in multidays

# if not in debug mode, sleep function. otherwise, nothing function.
sleep = lambda t : time.sleep(t)
if debug:
    sleep = lambda t : True

# contains references to colorama colors
colorObj = {
  "dim": Style.RESET_ALL + Style.DIM,
  "red": Fore.LIGHTRED_EX,
  "yellow": Fore.LIGHTYELLOW_EX,
  "green": Fore.LIGHTGREEN_EX,
  "blue": Fore.LIGHTBLUE_EX,
  "cyan": Fore.CYAN,
  "purple": Fore.LIGHTMAGENTA_EX,
  "white": Style.RESET_ALL
}

# wait is how long to wait before next instruction, default 0.5
# text speed is how long normal letters take, default 0.04
# slow text speed is recommended to be 0.06
# fast text speed is recommended to be 0.02
def fprint(string, color, wait = 0.5, textSpeed = 0.04):
  string = textWrap(string) # word wrap
  if color == "rainbow": # separate function for rainbow print
    rainbowPrint(string, textSpeed)
  else:
    for char in string: # print character by character
      print(colorObj.get(color) + char, end = "") # prints...
      sys.stdout.flush() # and display it on the screen
      if textSpeed != 0: # if not instant, wait a bit
        if char in (".", "!", "?", ";"):
          sleep(.5)
        elif char in (",", ":"):
          sleep(.25)
        else:
          sleep(textSpeed)
  if not debug:
    sleep(wait) # final end of print wait
  print(Style.RESET_ALL) # quick reset of colorama just in case somethng messes up

# wraps text according to terminal size
def textWrap(string):
  width = int(os.get_terminal_size()[0] * .8) # width is a little bit less than terminal size
  currWidth = 1
  finalString = ""
  array = string.split(" ") # split string into an array
  for word in array: # loops for every word
    currWidth += len(word) # currWidth increases by length of current word
    if currWidth > width: # if its bigger than the width...
      finalString += "\n" + word + " " # start a new line
      currWidth = 2 + len(word)
    else: # otherwise, just add word to the final string
      finalString += word + " "
  return finalString # and now you're done!

# rainbow print function
def rainbowPrint(string, textSpeed = 0.04):
	rainbowList = [Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, 	Fore.LIGHTMAGENTA_EX]
	rainbowInt = random.randint(0, 4) # begins at random color
	for char in string:
		print(rainbowList[rainbowInt] + char, end = "") # prints color according to rainbowInt
		sys.stdout.flush()
		rainbowInt += 1 # increment
		if rainbowInt == 5: # if you're at the end, reset to 0
			rainbowInt = 0
		if char in (".", "!", "?", ";"):
			sleep(.5)
		elif char in (",", ":"):
			sleep(.25)
		else:
			sleep(textSpeed)

clear = lambda : os.system("cls") # clears terminal

# does a little wait for input
def pause():
	fprint("Press ENTER", "dim", 0, 0)
	input()

# custom input function
def choice(array):
  for i in range(len(array)): # lists the options
    print(Fore.CYAN + "[" + str(i + 1) + "] " + array[i])
  print("")
  while True:
    try:
      answer = int(input(">> ")) # get the answer
    except:
      answer = 0 # if invalid, default to 0
    if answer in range(1, len(array) + 1):
      print(Style.RESET_ALL)
      return answer # returns answer
    else: # if the number isn't in the options range, invalid input
      fprint("Invalid input...", "red", 0, 0)
      print(Fore.CYAN, end = "")
      continue # try again

# returns random item from list
def randomAgree():
	randomAgreeList = ["Aight bro.", "Good choice.", "kk", "Alrighty.", "Okey dokey!!"]
	return random.choice(randomAgreeList)

# returns random item from list
def randomDeath():
	randomDeathList = ["as a crab", "from carbon monoxide poisoning", "from really bad Chinese food", "from CoVID-19", "from fall damage", "in the trenches", "in a compromising position", "trying to commit suicide", "through reading this message", "in an online game of Chess", "in your favorite battle royale videogame", "in a TLS handshake", "in an automobile accident", "as a Kurdish freedom fighter", "from a gluten overdose", "in a candle factory fire", "trying to pursue the American Dream", "caught up in the grimy criminal underworld of urban Wyoming", "as an ant", "from an angry weasel", "in a \"suicide\"", "from good, clean, fun"]
	return random.choice(randomDeathList)

# returns random item from list
def randomGreeting():
	randomGreetList = ["Lets get into it, yeah?", "You ready?", "Check me out on Bandcamp!", "Now with extra days!", "*snip snap snip snap snip snap*", "My claws are clicking \"fuck you\" in morse code.", "Let's get Kraken!"]
	return random.choice(randomGreetList)

# returns day or days depending on day count
def dayPlural():
	if days == 1:
		return "day"
	else:
		return "days"

# creates the queue
def generateQueue():
    queueList = ["oldGuyDrugs",
        "presidentialCampaign",
        "robberyTime",
        "soccerPractice",
        "burnWitch.py",
        "cookingCompetition.py",
        "crabExam.py",
        "depression.py",
        "firstContact.py",
        "fisherman.py",
        "forwardScuttle.py",
        "gameShow.py",
        "oldMan.py",
        "paneraBreadGiftcard.py",
        "peerPressure.py",
        "pirates.py",
        "prawnShop.py",
        "prisonersDilemma.py",
        "purchaseSomeGoods.py",
        "randomHotCrab.py",
        "tasteTesting.py",
        "wrongSecretAgent.py"
    ]
    random.shuffle(queueList)
    return queueList

""" Legacy code
# creates the queue
def generateQueue():
	queueList = []
	for i in os.listdir("days"): # loop through days
		if i[0] == "_": # skip __pycache__
			continue
		if i[0] == "$": # skip $chainDays
			continue
		queueList.append(i) # append to queue
	random.shuffle(queueList) # shuffle babey!!
	return queueList # return
"""
