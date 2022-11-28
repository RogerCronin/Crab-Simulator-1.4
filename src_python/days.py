from waterWorks import fprint, choice, clear, pause
import waterWorks as config
from colorama import Fore, Style
import time, random, os, sys, importlib

def c_broomHospital(queue):

    fprint("You wound up in the hospital following your tragic magical getaway.\n", "dim")
    fprint("I'm sorry, but I can't submit \"flying broom stick accident\" to insurance claims.", "yellow")
    fprint("Says the doctor in your hospital room.\n", "dim", 1)
    fprint("I'm afraid you'll have to pay the full amount of 15 dollars.\n", "yellow", 1)

    answer = choice(["Pay up", "Bribe the doctor"])

    if answer == 1:
        fprint("Fine, but you're no fun.\n", "cyan")
        fprint("Or so I've heard.\n", "yellow")
        fprint("You're now 15 bucks short. I guess. That's cool.\n", "dim", 1)

        fprint("15 bucks - 1", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality += 1
        config.experience += 1
    else:
        fprint("Could my good friend Mr. Andrew Jackson here change your mind?", "cyan")
        fprint("You say to the doctor.\n", "dim", 1)
        fprint("Is that a 20 dollar bill?\n", "yellow")
        fprint("Do you accept my bribe?\n", "cyan")
        fprint("I... yes.", "yellow")
        fprint("The doctor responds.\n", "dim", 1)

        fprint("20 bucks - 1", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality -= 1
        config.experience += 1

    return queue

def c_crabExamDeath(queue):
    fprint("At 4 in the morning, you are awoken by loud knocking at your door.\n", "dim", 1)
    fprint("Yeah, what is it?\n", "cyan", 1)
    fprint("A crab with really cool sunglasses steps into your apartment, holds up a gun, and pulls the trigger.\n", "dim", 2)
    config.state = "You didn't renew your license at the A-Sea-Ts yesterday, so a government official was dispatched to ensure you didn't remain a crab any longer. Think longer about your education next time, alright?08"
    return queue

def c_cringeNarrator(queue):
    fprint("Hey, man. I know it's only been " + str(config.days) + " " + config.dayPlural() + ", but I feel like we've gotten pretty close, you know?\n", "green")

    answer = choice(["Uh, what?", "Oh shit bro, totally, fuck I thought I was the only one"])

    if answer == 1:
        fprint("Uh, what?\n", "cyan")
        fprint("Oh lmao wrong number thought this was someone else so sorry.\n", "green")
        fprint("Mm, ok.\n", "cyan")
        fprint("No really my friend took my phone it was just a joke.\n", "green")
        fprint("Oh, alright.\n", "cyan")
        fprint("Wow, you thought I liked you? That's pretty funny... unless? Jk.\n", "green")
        fprint("Cool.\n", "cyan", 2)
        config.state = "God, that was awkward. You died so hard on the inside that your body followed your mind.04"

    else:
        fprint("Dude, I thought I was the only one...\n", "cyan")
        fprint("Oh wait really? No cap?\n", "green")
        fprint("Yeah bro we really got a connection.\n", "cyan")
        fprint("Oh dip that's pretty epic.\n", "green")
        fprint("And then you woke up.\n", "dim", 1)

        fprint("Predictability + 5", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1

    return queue

def c_hotCrabSecondMeeting(queue):
    fprint("After a long day at the offish, you decide to let off some steam at the local pub.\n", "green")
    fprint("One fish-key neat, thanks.\n", "cyan")
    fprint("Coming right up. Hey, you look a little down, you good?\n", "yellow")
    fprint("Yeah, I'm fine, just a little lonely lately.\n", "cyan")
    fprint("Hey, I get it. Why don't you talk to her?\n", "yellow")
    fprint("He points to a crab across the bar, her face concealed by a tall seaquila sunrise\n", "dim")

    fprint("Sure, what do I have to lose?\n", "cyan")
    fprint("The bartender goes over and gestures to you.\n", "dim")
    fprint("You can't tell what he's saying from a distance, but you can tell the crab is the most beautiful you've ever seen.\n", "green")
    fprint("The bartender walks over.\n", "dim", 0.1)
    fprint("Hey, she's gonna come over. Get ready!\n", "cyan")
    fprint("Oh god.\n", "cyan", 0)
    fprint("Oh shit.\n", "cyan", 0)
    fprint("Okay.\n", "cyan")
    fprint("She walks over.\n", "dim")
    fprint("Uhh, hey.\n", "cyan")
    fprint("She looks at you, surprised.\n", "dim")
    fprint("Oh, hi? Excuse me\n", "blue")
    fprint("She walks past you to a younger, much more attractive crab behind you.\n", "dim")
    fprint("What?\n", "cyan")
    fprint("Oh, you thought I was talking to you?\n", "yellow")
    fprint("Yeah, kind of??\n", "cyan")
    fprint("Nahh.\n", "yellow")
    fprint("Again? Wtf that makes no sense...\n", "cyan")
    fprint("Idk dude, I think we need some better writers.\n", "yellow")
    fprint("Honestly, this shit sucks.\n", "cyan")
    fprint("Yeah bro for real.\n", "green")
    fprint("Idk, I think it's kind of charming\n", "rainbow", 0)
    fprint("FUCK you, go back to doing stats, Stat boy.\n", "green")
    fprint("*sniff* fine, experience + 1\n", "rainbow")

def c_presidentResign(queue):
    fprint("In the early hours of the next day, you resign as President. This inconveniences a lot of people.\n", "dim", 1)
    fprint("Great, mission accomplished.\n", "cyan", 1)
    fprint("Knowledge of how the government works - 1", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def c_presidentStay(queue):
    fprint("A news anchor sits before the camera, ready to begin tonight's news coverage.\n", "dim", 1)
    fprint("Just hours after the official granting of the title \"President\", our new president was stabbed 23 times in the back. No legal action will be taken, however, because everyone has universally agreed he was a really shitty president.\n", "yellow", 2)
    config.state = "You flew to close to the sun, my dear Icarus. You were blinded by your own hubris so much so that you forgot you don't have a clue how the government functions. Should've quit while you were ahead, bruv.10"
    return queue

def c_supermarketPirate(queue):

    fprint("You're in the check-out line at Walmart when you encounter a ... familiar looking crab.\n", "green")
    fprint("ARRR, WHAT DO YE MEAN ME COUPON'S EXPIRED!?!?\n", "yellow")
    fprint("I'm sorry sir, but this coupon is-\n", "blue", 0)
    fprint("FUCK YE SELF, I NEED ME VITAMIN-SEA SUPPLEY-MENTS! (ARRG)\n", "yellow")
    fprint("Whoa, looks like that pirate's gonna get scurvy if you don't do anything. What do you do?\n", "green")

    answer = choice(["Stand up for the pirate", "Let him get what he deserves"])

    if answer == 1:
        fprint("You've decided to yell at the poor service worker who probably gets paid minimum wage.\n", "dim")
        fprint("Hey man, this pirate's just trying to stay healthy. Just let him use the coupon.\n", "cyan")
        fprint("ARrgh?\n", "yellow")
        fprint("The pirate has never encountered compassion before today.\n", "dim")
        fprint("You know what, fine, I don't care.", "blue")
        fprint("Says the cashier.\n", "dim", 1)
        resonseList = ["SHIVER ME TIMBERS LADDIE, YE DID IT!", "YO HO HO AND A BOTTLE OF RUM, YE DID IT!", "SINK ME, MATEY, YE DID IT!", "SPLICE THE MAINBRACE, YE DID IT!"]
        fprint(random.choice(resonseList), "yellow")
        fprint("Forget what I said yesterday, matey. A crab like ye would be a fine addition te any respectable pirate crew.\n", "yellow")
        fprint("Disdain for pirates - 10", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality += 1
    elif answer == 2:
        fprint("Sir, this \"coupon\" is actually a Panera bread gift card. We can't accept this.", "blue")
        fprint("The cashier says.\n", "dim", 1)
        fprint("The pirate is visibily distressed.\n", "dim", 1)
        fprint("Aye, it seems the only beast this old pirate can't conquer is the monster of monopolistic corporate America. (arrg)\n", "yellow")
        fprint("He instantly evaporates into a puff of citrus-scented smoke.\n", "dim", 1)
        fprint("Emotional scarring associated with Walmart + 4", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality -= 1

    return queue

def m_oldGuyDrugs_1(queue):

    fprint("It's a sunny afternoon, and you're walking through a shady part of town when you notice an old crab leaning against a wall.\n", "dim", 1)

    geezerResponses = ["scram why don'tcha.", "whadda lookin at, eh?", "you look a little red for this part of town."]
    fprint("Oi, kid, " + random.choice(geezerResponses) + "\n", "yellow", 0.5, 0.06)

    fprint("All of a sudden, the crab collapses onto the ground.\n", "dim")

    fprint("Ow FUCK, a heart attack!\n", "yellow", 0.5, 0.06)
    fprint("You run up to the crab and say", "dim", 0)
    fprint("Oh shit, you good dude?\n", "cyan")

    fprint("I'm dying, kid. Please, continue on my legacy of selling drugs.\n", "yellow", 0.4, 0.06)
    fprint("Wha-\n", "cyan", 0.1)
    fprint("My forefathers started selling ketamine in the early 1700s after arriving fresh off the boat from Ireland. My grandfather taught my own father how to produce his own meth. And hi-\n", "yellow", 1.5, 0.06)
    fprint("Oof he died.\n", "dim", 1)
    fprint("Well fuck, looks like you gotta do it now.\n", "green", 1)

    fprint("After a bit of searching through the contents of his satchel, you find his stash of oyster-piods and decide to start your new fledgling business tomorrow.\n", "dim")

    fprint("Look at you go, you little entrepreneur!\n", "green", 1)

    fprint("Drugs + 9", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1

    return queue

def m_oldGuyDrugs_2(queue):

    fprint("Ok, so, oyster-piods, who even buys these?\n", "cyan")
    fprint("The oyster-piods are sitting on your table, dripping with a quiet menace.", "dim", 1.5)
    fprint("You take a small white pill out of the brown paper bag.\n", "dim")
    fprint("Such a small little thing... what's the big fuss about?\n", "cyan")
    fprint("Idk man, they seem pretty popular tho.\n", "green")

    answer = choice(["Pop some oyster-piods","Start making some snazzy posters for your new business", "Ignore the dying crab's wishes and do nothing"])

    if answer == 1:
        fprint("Mmm tasty.\n", "cyan", 2)
        fprint("But after 5 suspenseful minutes, nothing seems to happen.\n", "dim")
        fprint("Bro these oyster-piods ain't shit.\n", "cyan")
        fprint("You get up to throw the bag away, when suddenly...\n", "dim")
        fprint("O h  s h i t\n", "rainbow")
        fprint("bRoo w         t f \n", "rainbow", 0.7)
        fprint("ḇ̸̢̛r̵̭͘ö̴̡̡͍͇̦́̄͠\n", "rainbow", 3)
        config.state = "Turns out the recommended dosage of oyster-piods for a first time user is only 200 milli-clams, better luck next time.03"
    elif answer == 2:
        fprint("Shucks, I'm getting ahead of myself, I better start advertising if I hope to sell this stuff.\n", "cyan")
        fprint("---1 trip to Staples later---\n", "dim", 2, 0)
        fprint("Okay, I think I have everything.\n", "cyan")
        fprint("What to use?\n", "green")
        answer = choice(["M'shark-er - +1 Brightness, +3 Huffability", "Cray-on - +1 Brightness, -2 Dignity"])
        if answer == 1:
            fprint("M'shark-ers, good choice.\n", "green")
            fprint("You uncap the suckers and start to go to town.\n", "dim")
            fprint("Ah shit, what's happening??\n", "cyan", 0)
            fprint("Is what you say as your apartment fills with noxious m'shark-er fumes.\n", "dim", 2)
            config.state = "Have comfort in knowing your last few moments were spent in the pure ecstasy derived from shitty m'shark-er gas.05"
        elif answer == 2:
            fprint("Cray-ons? What are you, five?\n", "green")
            fprint("Fuck you it's an inside joke you wouldn't get it.\n", "cyan")
            fprint("Ok, ok.\n", "green")
            fprint("You spend the rest of the day on your floor with cray-ons and poster board.\n", "dim")
            fprint("Oh boy, all the other drug dealers are gonna be sooo jealous of my posters!", "cyan", 0)
            fprint("You think as you drift off to sleep.\n", "dim")
    elif answer == 3:
        fprint("No, no, I shouldn't do this.\n","cyan")
        fprint("You grab the paper bag and flush the pills down the toilet.\n", "dim")
        fprint("Ah, underwater plumbing, what an invention.\n", "cyan")
        fprint("Oh, right, you're a crab, this is all underwater.\n", "green")
        fprint("Yeah, so?\n", "cyan")
        fprint("Fuck you, underwater toilets don't make any sense.\n", "green")
        fprint("What?\n", "cyan")
        fprint("Suddenly, the toilet starts to overflow.\n", "dim")
        fprint("For fucks sake, where's the plunger?\n", "cyan")
        fprint("The water level in your apartment has reached your knees.\n", "dim", 0.3)
        fprint("Oh god, oh fuck...\n", "cyan", 0.1)
        fprint("The mixture of oyster-piods and water have slowed your movements.\n", "dim")
        fprint("God-clam-it.\n", "cyan", 0)
        fprint("Is the last thing you muster out before your head is swept underwater.\n", "dim", 2)
        config.state = "It would seem that crabs would prefer to have their dying wishes carried out. Keep that in mind.07"

    return queue

def m_oldGuyDrugs_3(queue):
    fprint("You wake up bright and early, excited to hang up your awesome posters.\n", "dim")
    fprint("Your hang up your posters haphazardly along the way to the alley, where you set up shop.", "dim", 1)
    fprint("A shady red crab shuffles in soon after.\n", "dim")
    fprint("H-h-h-hey man I saw your posters, p-pretty cool.\n", "yellow")
    fprint("Hey, that's awesome. Thanks dude.\n", "cyan")
    fprint("N-n-no problem. So, you s-still selling for the price on the p-posters?\n", "yellow")
    fprint("Yes sir, two pills a sheckle!\n", "cyan")
    fprint("A-a-alright man I'll take all of 'em!\n", "yellow")
    fprint("At this point a line of equally shady crabs have formed a sort of queue stretching out from the alley and onto the sidewalk.\n", "dim")
    fprint("All of them? Sure thing! Man, that sure was easy.\n", "cyan")
    fprint("As you walk out, you hear the ghost of the old crab trying to tell you the going rate for oyster-piods is 20 sheckles for 2 pills, but you're way too excited to notice.\n")
    fprint("Oyster-piods - 9", "rainbow", 1)
    fprint("Half a sheckle + 9", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    config.personality += 1
    return queue

def m_presidentialCampaign_1(queue):
    fprint("No, I didn't ask for that, Carlos.\n", "cyan", 1)
    fprint("You're driving down the highway talking to your buddy Carlos on your shellphone.\n", "dim", 1)
    fprint("She did NOT!", "cyan", 1)
    fprint("Oh my God, WHO?", "cyan", 1)
    fprint("I can't believe that could- OH SHIT\n", "cyan", 0)
    fprint("CRAAAAAAAAASSSSSHHHHhhhhh\n", "red", 3)
    fprint("You were airlifted to a hospital where a team of highly skilled crabs performed a life saving operation on you.\n", "dim", 2)
    fprint("Thanks, doc, for saving my life. I owe you one.\n", "cyan", 1)
    fprint("No need as long as you pay your bill of 250,000 pesos, my friend.\n", "yellow", 1)
    fprint("When you were reincarnated " + str(config.days) + " " + config.dayPlural() + " ago, you forgot to buy health insurance.\n", "dim", 1)
    fprint("Quick, what's the fastest way to get quick cash as a crab?\n", "green", 2)
    fprint("...", "cyan")
    fprint("I got it. I'll win the presidential race and use my new fangled powers to embezzle money from The National Mint and pay off my debt!\n", "cyan", 2)
    fprint("You sign up for the elections on your way home and heat up some can soup for dinner.\n", "dim", 1)
    fprint("Debt + 250000 plus interest", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    return queue

def m_presidentialCampaign_2(queue):
    fprint("You wake up to a bright, sunny day full of opportunities.\n", "dim", 1)
    fprint("Right, now how will you start your campaigning?\n", "green")
    answer = choice(["Call up your parents and ask them to vote for you", "Go outside with a sign", "@everyone on your Discord server telling them to vote"])
    if answer == 1:
        fprint("You whip out your phone and dial your parents' home phone.\n", "dim", 1)
        fprint("Riiiing. Riiiiiiiiing. Riiiiiiiiiiiiiiiiiing.\n", "red")
        fprint("Hello?\n", "yellow", 1)
        fprint("Hi Mom, I'm running for president. Do you think you could vote for me?\n", "cyan")
        fprint("Sure thing sweetie. I'm so proud of you!\n", "yellow")
        fprint("Aww, doesn't that just put a smile on your face?\n", "green", 1)
        fprint("Voters + 2\n", "rainbow", 2)
    elif answer == 2:
        fprint("You whip out your pen-seal.. sorry, was that pun too much of a stretch? Anyway, you whip out your pencil and craft up a pretty spicy sign design.\n", "dim", 1)
        fprint("Ay, fellas, vote for me! I'm running for president!", "cyan", 0)
        fprint("You call out to people passing by in your city.\n", "dim", 1)
        fprint("Hey, what are your policies?", "yellow", 0)
        fprint("Some fish asks you.\n", "dim", 1)
        answer = choice(["Crab care reform", "Increased minimum wage", "Seizing the means of production"])
        if answer == 1:
            fprint("I'm all about crab care reform.\n", "cyan", 1)
        elif answer == 2:
            fprint("I'm all about increasing minimum wage.\n", "cyan", 1)
        else:
            fprint("I'm all about seizing the means of production.\n", "cyan", 1)
        fprint("Oh, dope. You got my vote.\n", "yellow", 2)
        fprint("You expain your policies to a couple more aquatic animals. A handful seem pretty interested in your platform.\n", "dim", 1)
        fprint("Voters + 45\n", "rainbow", 2)
    else:
        fprint("You whip out your phone and type a real quick message to informing them of your decision to campaign.\n", "dim", 1 )
        fprint("[CrabbyMan#8644] : @everyone, Im running for president so yall should vote for me thanks", "white", 5, 0)
        fprint("[OldBayStan#5277] : ok buddy", "white", 2, 0)
        fprint("[JohnnyFisher#2012] : aight\n", "white", 2, 0)
        fprint("Looks like you convinced a few people to vote for you.\n", "dim", 1)
        fprint("Voters + 14\n", "rainbow", 2)
    config.days += 7 # time skip of 1 week
    return queue

def m_presidentialCampaign_3(queue):
    fprint("---1 Week of Campaigning Later---\n", "dim", 2, 0)
    fprint("Look alive! Today is voting day, where all of the animals under the sea gather to vote on a new leader.\n", "dim", 2)
    fprint("You managed to gather over 500 guys to vote for you. Not like it matters tho, cause you're running unopposed. Turns out the last guy got murdered by the Monarchy cause they don't like democratic institutions or something?\n", "green", 2)
    fprint("I hereby grant you the title of President, my good sir!", "yellow", 0)
    fprint("Some dude on a stage says to you.\n", "dim", 1)
    fprint("As the crowd cheers, you start thinking about how you'll go through with your plan.\n", "dim", 1)
    fprint("Hello? Is this The National Mint?", "cyan", 0)
    fprint("You speak into your phone.\n", "dim", 1)
    fprint("Yes, hello Mr. President. What would you like?\n", "yellow")
    fprint("Could you route 250,000 pesos into my personal bank account for me?\n", "cyan", 1)
    fprint("Isn't that ille-\n", "yellow", 0)
    fprint("Did I stutter?\n", "cyan", 2)
    fprint("Uh, sure thing Mr. President.\n", "yellow", 2)
    fprint("This whole President thing has a lot of power... Do I really want to resign immediately after this?\n", "cyan")
    answer = choice(["Resign", "Stay"])
    if answer == 1:
        fprint("But alas, I don't give two fucks about this job.\n", "cyan", 1)
        fprint("Debt - 250000 pesos plus interest\n", "rainbow", 2)
        queue.insert(0, "c_presidentResign.py")
    else:
        fprint("Heh. Hahahah. HahahahHAHAhahaHAha.\n", "cyan", 1)
        fprint("Power tripping + 56\n", "rainbow", 2)
        queue.insert(0, "c_presidentStay.py")
    return queue

def m_robberyTime_1(queue):

    fprint("You spot your favorite hot dog stand, The Wacky Dawg, just across the street.\n", "dim", 1)
    fprint("Oh hey, I guess I could go for a bite to e-\n", "cyan", 0)
    fprint("YO KID, OVER HERE.", "yellow")
    fprint("A weasel calls from near the stand.\n", "dim", 2)
    fprint("Huh? Me?\n", "cyan", 0)
    fprint("AY, YEAH YOU, OVER HERE.\n", "yellow", 1)
    fprint("You walk over to the weasel.\n", "dim", 1)
    fprint("Yeah man?\n", "cyan")
    fprint("You wanna rob that bank over there? I gotta have a \"partner in crime\" or I'll never make it in the criminal underworld of this beachside resort.\n", "yellow")

    answer = choice(["Yeah lets go", "Nah man, I ain't about that shit anymore"])

    if answer == 1:
        fprint("You got it.\n", "cyan")
        fprint("The two of you walk into the bank.\n", "dim", 1)
        fprint("HANDS IN THE AIR!\n", "yellow")
        fprint("Everyone's hands shoot up. The weasel walks over to the bank teller while you stand by the front door.\n", "dim", 2)
        fprint("Weeee woooo. Weeee woooooooo. Weeeeeeeee wooo.\n", "red", 1)
        fprint("Shit! The cops are here. Take this and scram.\n", "yellow")
        fprint("The weasel hands you four bags with dollar bill signs on them.", "dim", 2)
        fprint("You hightail it out of there with the money in hand until you end back up at your apartment.\n", "dim")
        fprint("Whew. That was a close one, yeah?\n", "cyan", 1)
        fprint("Money + 1600525", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality -= 1
        config.message = "y"
    else:
        fprint("Nah, I'm not lookin to do some illegal stuff today.", "cyan")
        fprint("Thanks tho.\n", "cyan", 1)
        fprint("Oh well, that's a shame. I'll just list you as an accomplice tomorrow when I'm arrested.\n", "yellow")
        fprint("Bullshit. I'd like to see you try.\n", "cyan")
        fprint("Aight bro.", "yellow")
        fprint("The weasel says entering the bank, AR-15 in hand.\n", "dim")
        fprint("You walk home and reheat some curry from last night for dinner.\n", "dim", 1)
        fprint("Sense of foreboding + 4", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality += 1
        config.message = "n"
    return queue

def m_robberyTime_2(queue):
    fprint("You wake up to a group of policecrabs shouting orders through a megaphone.\n", "dim", 1)
    fprint("YOU'RE WANTED FOR THE BANK ROBBERY YESTERDAY! COMPLY AND WE WON'T USE FORCE!\n", "yellow", 1)
    if config.message == "y": # gakked
        fprint("Goddamnit. They caught me.\n", "cyan")
        fprint("Well what are you gonna do?\n", "green")
    else: # innocent
        fprint("That weasel fucker actually convinced the cops!", "cyan")
        fprint("You think to yourself.\n", "dim", 1)
        fprint("Shit. What do you do?\n", "green")

    answer = choice(["Go outside with your claws up", "Peck shots through your window"])

    if answer == 1:
        fprint("YO! I'm coming outside with both of my claws up, unarmed.", "cyan")
        fprint("You call out through your window.\n", "dim")
        fprint("Oh sweet bb. Thanks.\n", "yellow", 2)
    else:
        config.message = "y"
        fprint("Yeah, fuck those guys.\n", "cyan", 1)
        fprint("You peek over the window with a slingshot, launching rocks at the policecrabs down below.\n", "dim", 1)
        fprint("A slingshot?\n", "green")
        fprint("It's the only thing I have on hand, shut up.\n", "cyan", 1)
        fprint("POUND POUND POUND.", "red")
        fprint("FBI OPEN UP!\n", "yellow")
        fprint("Oh fuck.\n", "cyan")
        fprint("A stream of at least 10 crabs race into your bedroom and arrest you.", "dim", 2)

    fprint("Later...\n", "dim")
    fprint("Aight, you're definitely guilty. See ya later.", "blue")
    fprint("The judge says as he dips out of the courtroom.\n", "dim")
    fprint("Have fun in jail, kiddo!\n", "yellow", 2)

    if config.message == "y":
        fprint("Regret + 7", "rainbow", 1)
    else:
        fprint("Belief in the legal system - 14", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        config.personality += 1
    fprint("Experience + 1\n", "rainbow", 1)
    config.experience += 1
    return queue

def m_robberyTime_3(queue):
    fprint("Damn, is this really your cell? It's real shitty.\n", "green", 1)
    fprint("You see two bunk beds, a table, and a sink atop a grimy floor. Two other crabs are in your cell. One appears to be playing a harmonica, but on closer inspection it's actually just a few plastic straws taped together.\n", "dim", 1)
    fprint("Ay, you see that buff crab lifting weights by the table? It'd be real cool to assert your dominance and rough him up a bit.\n", "green")

    answer = choice(["Show him a bit of da pincers", "Let him be"])

    if answer == 1:
        fprint("Hey, dude with the weights. You wanna tussle?", "cyan", 0)
        fprint("You ask the buff crab.\n", "dim")
        fprint("Sure, punk.\n", "yellow", 2)
        config.state = "He smashed you up real good. Like, reeeaaal good. Probably should've paid attention when I called him a \"buff crab lifting weights\".06"
    else:
        fprint("You called him a \"buff crab lifting weights\", so I think I'll pass.\n", "cyan")
        fprint("Pshhh you're no fun.", "green", 1)
        fprint("Alright, grow accustomed to your new prison life. You'll be here for a few days.\n", "green")
        fprint("Will do chief.\n", "cyan", 1)
        fprint("School smarts - 1", "rainbow", 1)
        fprint("Street smarts + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
    return queue

def m_robberyTime_4(queue):

    fprint("It's Saturday movie night at the prison ward, and it's your turn to pick! What will you be watching?\n", "dim", 1)

    answer = choice(["The Shape of Water", "Shark Tale", "Ponyo"])

    if answer == 1:
        fprint("The fuck is this shit?", "yellow", 0)
        fprint("Several inmates call out when you announce your decision.\n", "dim", 1.5)

        fprint("The group of crabs are thoroughly uncomfortable by the time the film ends.\n", "dim", 1)
        fprint("Good job ig.\n", "green", 1)
        fprint("Taste in movies ± 1 depending on if you actually like that movie", "rainbow", 1)
    elif answer == 2:
        fprint("Boooo!", "yellow", 0)
        fprint("Some crab calls out when you announce your decision.\n", "dim", 1.5)
        fprint("---1 movie later---\n", "dim", 2, 0)
        fprint("I guess that wasn't bad...", "cyan", 0)
        fprint("You try to convince yourself. It's not working very well.\n", "dim", 2)
        fprint("Taste in movies - 1", "rainbow", 1)
    else:
        fprint("Really? A kids movie?", "yellow")
        fprint("Someone calls out.\n", "dim", 1)
        fprint("It seems some crabs are unhappy with your decision.\n", "dim", 1.5)
        fprint("By the end of the movie, all of the crabs are sobbing.\n", "dim", 1)
        fprint("Huh, that was kinda quirky.", "green")
        fprint("The narrator says, trying to stay composed through the tears.\n", "dim", 1)
        fprint("Taste in movies + 2", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def m_robberyTime_5(queue):
    gangList = ["red", "blue"]
    good = random.choice(gangList)
    if good == "red":
        bad = "blue"
    else:
        bad = "red"
    fprint("Hey, kid. Come close. I gotta ask you something important.", good, 0)
    fprint("Some " + good + " crab says to you during lunch.\n", "dim", 1)
    fprint("What's up?\n", "cyan")
    fprint("You new here?\n", good)
    answer = choice(["Yes", "No"])
    fprint("Well, I-\n", "cyan", 0)
    fprint("Shut up, I don't care. You see those dirty " + bad + " crabs over there? We're in a bit of a gang war right now. One little thing could throw off the-\n", good, 0)
    fprint("HEY " + bad.upper() + " CRABS OVER THERE! THIS " + good.upper() + " CRAB THINKS YOU'RE DIRTY!", "cyan", 0)
    fprint("You call out through the now silent cafeteria.\n", "dim", 2)
    fprint("...", bad, 2)
    fprint("Sorry. I've been going through a lot right now with my family and just don't have the motivation these days.\n", bad, 1)
    fprint("Oh shit dude. I'm so sorry. I didn't know you were going through all of that.\n", good)
    fprint("The " + good + " crab along with some of the " + bad + " crabs go to comfort the gang leader.\n", "dim", 1)
    fprint("Do you want to talk-\n", good, 0)
    fprint("STAB!\n", bad, 1.5)
    fprint("FUCK!\n", good, 1)
    fprint("The " + good + " crab staggers away from the " + bad + " crab, revealing a stab wound in his shell.\n", "dim")
    fprint("Look, man. Nothing personal, yeah?", bad, 0)
    fprint("The " + bad + " crab says to the dying " + good + ", twirling her prison shank between her pincers.\n", "dim", 1)
    fprint("Murmurs erupt throughout the cafeteria.\n", "dim", 1.5)
    fprint("STAB!", good, .4)
    fprint("STAB!\n", good, .7)
    fprint("Two " + bad + " crabs are taken down by a pair of " + good + " crabs.\n", "dim")
    fprint("FUCK YOU! THIS IS WAR NOW!\n", bad)
    fprint("The cafeteria erupts in chaos between the " + good + "s and " + bad + "s.\n", "dim", 1)
    fprint("Dude, what the fuck did you just cause?\n", "green")
    fprint("You curl up in a corner and cry until a warden with a gun motions you out of the bloodbath that the cafeteria now is.\n", "dim", 1)

    fprint("Will to remain alive - 60", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def m_robberyTime_6(queue):
    fprint("Aight bro you're free to go.", "yellow", 0)
    fprint("The crab behind the glass window says to you.\n", "dim", 1)
    fprint("The chain-link gate opens as an alarm sounds in the background, but you don't care. All you want to do is breathe in the fresh air.\n", "dim")
    if config.message == "y":
        fprint("Dude, no more prison time. Not cool.\n", "green")
    else:
        fprint("Let's hope that doesn't happen again.\n", "green")
    fprint("Will to remain alive + 59", "rainbow", 1)
    if config.message == "y":
        fprint("Experience + 1 (but only if you learned your lesson)\n", "rainbow", 2)
    else:
        fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def m_soccerPractice_1(queue):

    fprint("It's 7 o'clock in the afternoon, and you've just finished soccer practice.\n", "dim", 1)

    fprint("Wow, that sure was a fun practice!", "cyan")
    fprint("You say to your teammates.\n", "dim", 1)

    fprint("Yeah! I sure am glad we are crabs, which allows us to play these sports!", "yellow")
    fprint("A friend says back.\n", "dim", 1)

    fprint("Now I just gotta wait for Mom to come pick me up.", "cyan", 3)

    fprint("...", "cyan", 3)

    fprint("Mom?\n", "cyan", 2)
    return queue

def m_soccerPractice_2(queue):

    fprint("You ended up sleeping on the ground.\n", "dim", 1)

    fprint("I wonder when Mom will show up.", "cyan")
    fprint("You think to yourself.\n", "dim", 2)

    fprint("The weather sure is lovely...\n", "cyan", 2)

    fprint("It starts to rain.\n", "dim", 2)

    fprint("Oh, well at least it can't ge-\n", "cyan", 0)

    fprint("It starts to rain really hard.\n", "dim", 2, 0.02)

    fprint("Oh.\n", "cyan", 2)
    return queue

def m_soccerPractice_3(queue):
    fprint("I can't believe it's already 2 pm in the afternoon and Mom still hasn't come back.", "cyan")
    fprint("You think idly.\n", "dim", 1)

    fprint("Wait a minute, I was reincarnated, like, " + str(config.days) + " " + config.dayPlural() + " ago. I don't even have a Mom.\n", "cyan", 1)

    fprint("You decide to walk back to your apartment.\n", "dim", 1)

    fprint("Rookie mistake, kid. You gotta remember these things if you're gonna survive in the crab world.\n", "green", 2)

    fprint("Loneliness + 4", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def d_burnWitch(queue):
    fprint("Unfortunately, it seems like the townspeople of your weird little crab society have accused you of being a witch.\n", "dim")
    fprint("Wait, what the fuck? People still believe in witches?\n", "cyan")
    fprint("Yeah ik, super weird. Anyways they'll be at your house in like 2 minutes, better make sure you're prepared.\n", "green")

    answer = choice(["Grab a broom", "Use your claws", "Get some oil", "Do nothing"])

    if answer == 1:
        fprint("Aight, broom it is.", "cyan")
        fprint("You say as you pick up your broom.\n", "dim")

        fprint("Dude, what the fuck? They're gonna think that's your magic witchy getaway vehicle.\n", "green")

        fprint("Suddenly, the broom starts to vibrate intensely, floating off the ground.\n", "dim")

        fprint("See ya later!\n", "cyan", 1)
        fprint("You fly out of your apartment complex on the broom, laughing at the mob formed outside of your house. And promptly get into a broom crash.\n", "dim")

        fprint("Did you ever get your broom license? That's what I thought.\n", "green", 1)

        fprint("Bodily injuries + 23", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1

        queue.insert(0, "c_broomHospital.py")

    elif answer == 2:
        fprint("Well fuckers, it's show time.\n", "cyan")

        fprint("The door to your house is broken down and crabs storm in like that one FBI meme that was going around a while ago.\n", "dim", 1)

        fprint("WHAM!", "red")
        fprint("Says the big letters appearing whenever your hit someone.\n", "dim")

        fprint("BAM!\n", "red")
        fprint("How is that happening?\n", "green")

        fprint("POW!\n", "red", 2)

        fprint("You stare at the utter carnage surrounding you. You evil, evil crab. You killed a baby. What the fuck, dude?\n", "dim", 1)

        fprint("Disrespect for the infantile + 8", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality -= 1

    elif answer == 3:
        fprint("Time to make like the 2010 Gulf of Mexico oil spill!\n", "cyan")
        fprint("You start pouring oil out of your apartment window like a madman. Holy shit, dude.\n", "dim")

        fprint("Who's the witch now, fuckers?", "cyan")
        fprint("You yell as you continue to slaughter innocent crabs.\n", "dim", 2)

        fprint("Eventually the mob runs away, your entire street now covered in oil.\n", "dim")

        fprint("Yeah, that was not cool dude.\n", "green", 1)

        fprint("Oil stocks - 2", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality -= 1

    else:

        fprint("I can't really be bothered to do anything about this.\n", "cyan")
        fprint("Dude come on...\n", "green", 2)
        config.state = "The mob dragged you from your computer and convicted you of being a witch. As much as you tried, your non-existent magical powers couldn't save you from burning at the stake.02"
    return queue

def d_cookingCompetition(queue):
    fprint("Yo, you cook, right?", "yellow", 0)
    fprint("Your friend Carlos asks you while playing on his Nintendo SeaDS.\n", "dim", 1)
    fprint("I mean I can make a mean Cup O' Noodle every now and then...\n", "cyan")
    fprint("Well you gotta check this out man.\n", "yellow", 1)
    fprint("He holds up a newspaper, pointing to the article titled \"$250,000 Cooking Competition\".\n", "dim")
    fprint("Hmm, sure.\n", "cyan", 1.5)
    fprint("After spending a radical 50 minutes practicing, you head out to the competition site.\n", "dim", 1)
    fprint("I'm here to sign up for the cooking competition!", "cyan", 0)
    fprint("You say to the person manning the ticket stand in front of the stadium.\n", "dim", 1)
    fprint("Bud, imma need identification please.\n", "yellow")

    answer = choice(["Show him your passport", "Show him your Olive Garden Rewards Club card"])

    if answer == 1:
        fprint("Here's my passport.\n", "cyan")
    else:
        fprint("Here's my Olive Garden Rewards Club card.\n", "cyan")

    fprint("Huh? No, I mean your National Cooking Association member card.\n", "yellow")
    fprint("Oh shit, um, nevermind.\n", "cyan", 1)
    fprint("Okay, you're definitely breaking into this thing. What should you try?\n", "green")

    answer = choice(["Scale the building and climb in through the roof", "Pretend to be a plumber fixing a problem"])

    if answer == 1:
        fprint("I'm sure this won't end horribly!\n", "cyan", 1)
        fprint("As it turns out, it did not end horribly.", "dim", 1)
        fprint("You reach the top and break off the cover for a vent duct. After crawling around for a while, you pop out inside the main competitor's hallway.\n", "dim", 1)
    else:
        fprint("You put on your trusty denim jumpsuit and stroll in through the front gate.\n", "dim", 1)
        fprint("Ay, what do you think you're doing?", "blue", 0)
        fprint("A security crab asks you.\n", "dim", 2)
        fprint("I'm a plumber, I'm fixing the bathroom problems.\n", "cyan", 2)
        fprint("This stadium doesn't have any bathrooms.\n", "blue", 2)
        fprint("That's the problem I'm fixing.\n", "cyan", 2)
        fprint("Oh, carry on then.\n", "blue")
        fprint("Jeez that was a close one.\n", "green")
        fprint("You continue walking until you reach the main competitor's hallway, where you then change back into normal clothes.\n", "dim", 1)

    fprint("Attention all competitors, to your cooking stations in the next 5 minutes!", "yellow", 0)
    fprint("A crab calls out from over the intercom.\n", "dim")
    fprint("Aight you should probably enter the main area now.\n", "green", 1)
    fprint("You follow the crowd of aquatic animals through a large entryway, emerging onto the floor of the stadium. Around you animals of all shapes and sizes are cheering their favorite chefs on as they emerge, a deafening roar that drowns out any chit-chat from your competition. They all assume position at their designated tables, atop which a variety of cooking utensils and equipment lay. You decide to situate yourself next to a rather scary looking shrimp.\n", "dim", 1)
    fprint("CHEFS! 5!\n", "yellow", 0)
    fprint("SHIT\n", "cyan")
    fprint("4!\n", "yellow", 0)
    fprint("FUCK\n", "green")
    fprint("3!\n", "yellow", 0)
    fprint("WHATDOIDO\n", "cyan")
    fprint("2!\n", "yellow", 0)
    fprint("IDFKMAN\n", "green")
    fprint("1!", "yellow")
    fprint("Start!\n", "yellow", 1)

    answer = choice(["Make your grandma's famous meatloaf", "Steal a recipe from your neighbor", "Crack out the Cup Noodles"])

    if answer == 1:
        fprint("You whip open the minifrige underneath the table, determined to make some goddamn meatloaf. Pulling out a package of ground beef, some veggies, and a bottle of chili sauce, you go to town.\n", "dim", 1)
        fprint("45 minutes left!\n", "yellow", 1)
        fprint("Slapping the ingredients into a pan, you crank your oven up to 500 and throw that shit in there.\n", "dim", 1)
        fprint("10 minutes left!\n", "yellow", 1)
        fprint("You pull it out of the oven.\n", "dim", 1)
        fprint("5 minutes left!\n", "yellow", 1)
        fprint("You whip it onto a plate and garnish with a sprig of some kind of herb you found in the ingredients drawer.\n", "dim", 1)
        fprint("1 minute left!\n", "yellow", 1)
        fprint("FUCKIFORGOTTHESALT\n", "cyan", 0)
        fprint("Time's up! Chefs, bring your creations up to the judging platform.\n", "yellow", 2)
        fprint("After 20 long minutes, it's finally your turn to go.\n", "dim", 1)
        fprint("Here's my, uh, meatloaf.\n", "cyan")
        fprint("The judge nodded, pulled out her fork and knife, and took a large bite. The entire crowd went silent. The tension in the air was palpable. Her eyes opened. It was impossible to tell what she was thinking. What seemed like a hush fell over the already silent venue. Finally, the judge opened her mouth and said", "dim", 0)
        fprint("Needs more salt. 6/10.\n", "blue", 2)
    elif answer == 2:
        fprint("You sneak over to your opponent's table. He doesn't appear to notice you due to the loud roar of the crowd. Taking a paper off the table, you swiftly return to your own table, successfully completing the mission.\n", "dim", 1)
        fprint("Hey, punk.", "blue", 0)
        fprint("Says the shrimp, now right behind you.\n", "dim", 2)
        config.state = "The shrimp told the judges and you got kicked out of the stadium. And then you got hit by a car walking home. Pay more attention, yeah?09"
        return queue
    else:
        fprint("You open the ingredients draw and pull out a styrofoam cup of ramen to heat up in the microwave. After a couple of minutes of preparation, your meal is done.\n", "dim", 1)
        fprint("Uh, guess I gotta wait until time's up?\n", "cyan")
        fprint("You decide to take a piss.\n", "dim", 1)
        fprint("---One really long piss later---\n", "dim", 2)
        fprint("Time's up! Chefs, bring your creations up to the judging platform.\n", "yellow", 2)
        fprint("After 20 long minutes, it's finally your turn to go.\n", "dim", 1)
        fprint("Here's my, uh, cup ramen.\n", "cyan", 2)
        fprint("...", "blue", 2)
        fprint("Get the fuck out of my face.\n", "blue", 2)
    fprint("Hey man, 25th out of... oh. Well, they were professional chefs, you didn't stand a chance.\n", "green")
    fprint("Thanks, that's really nice of you to say, narrator.\n", "cyan", 1)
    fprint("Resentment for restaurants + 1", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1

    return queue

def d_crabExam(queue):
    fprint("Ah fuck. Today's the day I take my A-Sea-T exam, right?\n", "cyan", 1)
    fprint("For those who aren't in the know-how under the sea, the A-Sea-T is an exam all crabs must take every 6 years to keep their crab license.\n", "dim", 1)
    fprint("Well, I guess I should take off to the testing location.\n", "cyan")
    fprint("You walk towards the office building, trying to scheme your way into cheating through the exam.\n", "dim")
    fprint("Think! What can I do?\n", "cyan")

    answer = choice(["Memorize some study material right now", "Pay off the crab next to you for the answers", "Do nothing and hope for the best", "Just skip the exam"])

    if answer == 1:
        fprint("You furiously whip out your handy index cards and memorize everything you can about crabs for a couple of minutes.\n", "dim")
        fprint("Great! Looks like I'm all prepared.\n", "cyan")
        fprint("You walk into the building with a false sense of confidence.\n", "dim", 2)
        fprint("---One Exam Later---\n", "dim", 2, 0)
        fprint("94%, not bad!\n", "cyan")
        fprint("...That was really fucking lucky and you know it.\n", "green", 1)
        fprint("Knowledge on crabs + 381", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 1)
        config.experience += 1
    elif answer == 2:
        fprint("This'll be a piece of cake.", "cyan", 0)
        fprint("You say while walking into the building.\n", "dim", 1)
        fprint("During the test, your peer over and ask the crab sitting next to you","dim", 0)
        fprint("Hey buddy, I got a fiver for you if you gimmie the answers.\n", "cyan")
        fprint("Yeah man, sure.\n", "yellow")
        fprint("You hand him the bill.\n", "dim")
        fprint("Right, so number 1 is A, number 2 is C, ...\n", "yellow", 2)
        fprint("---One Exam Later---\n", "dim", 2, 0)
        fprint("78%, could've been better.\n", "cyan")
        fprint("Cheating is NEVER the answer smh.\n", "green", 1)
        fprint("Integrity - 3", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 1)
        config.experience += 1
    elif answer == 3:
        fprint("Ah well, what can I do.\n", "cyan", 1)
        fprint("---One Exam Later---\n", "dim", 2, 0)
        fprint("Yikes, 1 percent point away from failing.\n", "cyan")
        fprint("If ONLY there was some way to have prevented that...\n", "green", 1)
        fprint("Anxiety + 9", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 1)
        config.experience += 1
    else:
        fprint("Can't be bothered. I'm outta heeeerrreee.\n", "cyan")
        fprint("Oh boy.\n", "green", 1)
        fprint("Learning your lesson + 0", "rainbow", 1)
        fprint("No experience for you\n", "rainbow", 2)
        queue.insert(0, "c_crabExamDeath.py")

    return queue

def d_depression(queue):
    fprint("Fuck. Being a crab sucks. Everything is made out of sand, the only thing to eat is seafood, and everything smells like ocean water.", "cyan", 1)
    fprint("If I got here by dying, then maybe that's how I can get out!\n", "cyan")

    fprint("I mean, sure. Crab suicide?\n", "green")

    answer = choice(["Yeah", "Nah"])

    if answer == 1:
        fprint("Let's do this thing.\n", "cyan", 2)
        config.state = "I mean, you died. You committed suicide after you couldn't deal with your new crab life. Good job?01"
    else:
        fprint("Actually nevermind. I don't feel like it.\n", "cyan")
        fprint("Cool cool. Glad you didn't?\n", "green")
        fprint("Depression - 5", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
        config.personality += 1
    return queue

def d_firstContact(queue):
    fprint("BANG!\n", "red", 1.5)
    fprint("The fuck was that?", "cyan", 0)
    fprint("You say, waking up with a jolt.\n", "dim", 1)
    fprint("You wanna go investigate?\n", "green", 1)
    answer = choice(["Nah, it's like 3 in the morning", "Those raccoons are getting in my garbage again"])
    if answer == 1:
        fprint("Bro it's way too early for this shit.\n", "cyan", 1)
        fprint("smh\n", "green", 1)
        fprint("Disappointment from the game devs + 1", "rainbow", 1)
        fprint("Fuck you no experience\n", "rainbow", 2)
    else:
        fprint("Something tells me it's not a raccoon...\n", "green", 1)
        fprint("You scuttle down the stairs to the front of your apartment complex to find yourself face-to-face with a UFO just chilling on the street.\n", "dim", 1)
        fprint("Huh? Is this a joke?\n", "cyan", 1)
        fprint("The door to the UFO slowly opens, revealing a silhouette of an unknown figure.\n", "dim")
        fprint("Oh shit, do you man your ground or submit to your new overlords?\n", "green")
        answer = choice(["Grow a pair", "I, for one, accept our new aquatic overlords"])
        if answer == 1:
            fprint("Screw you, alien fuckers. You ain't messing with this crab right here.\n", "cyan", 1)
        else:
            fprint("You fall to your knees and loudly call out", "dim", 0)
            fprint("Please don't hurt me! I beg for forgiveness!\n", "cyan", 1)
        fprint("The figure steps forwards, revealing a neon-green crab.\n", "dim", 1)
        fprint("⎓𝙹ꖎꖎ𝙹∴ ᒲ|| ℸ ̣∴╎ℸ ̣ℸ ̣ᒷ∷\n", "yellow", 1)
        fprint("The alien lets out a long string of expletives and closes the door. With a puff of steam, the UFO takes flight and cruises past your sight.\n", "dim", 1.5)
        fprint("Oh.\n", "cyan", 1)
        fprint("Fear of aliens - 2", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
    return queue

def d_fisherman(queue):
    fprint("You're walking in the park when you notice a strange open-air building with a bunch of crabs inside off to your right.\n", "dim", 1)
    fprint("Hey what's this thing all about?", "cyan", 0)
    fprint("You ask the crabs inside.\n", "dim", 1)
    fprint("Idk man, it's some funky metal thingy. Come inside.\n", "yellow")
    fprint("Neat.\n", "cyan", 1)
    fprint("You walk inside the building and start talking with some of the other crabs there, when suddenly the entire place starts rising into the air!\n", "dim", 1)
    fprint("You dumbass, that's a crab trap. You're gonna get fucking eaten by some addict Maryland fisherman.\n", "green")
    fprint("Oh shit man.\n", "cyan", 2)
    fprint("The cage surfaces, and a scruffy looking fisherman pulls it up. He dumps you into a large metal bucket.\n", "dim", 1)
    fprint("Mmm old bay.. the- crab, crab meat, mm gotta.. gotta catch crab, crabs..\n", "blue", 1)
    fprint("This fisherman's so far gone he isn't even speaking coherent English. A sad case that happens far too often along the banks of the Chesapeake.\n", "green", 1)
    fprint("Well fuck, how am I gonna get outta here?\n", "cyan")
    answer = choice(["Climb up the sides", "Teach the crabs about metaphorical analogies"])
    if answer == 1:
        fprint("You try climbing up the sides of the bucket to no avail; the other crabs just pull you right down.\n", "dim", 1)
        fprint("You idiots, how are we gonna escape if you just keep pulling me down?\n", "cyan")
        fprint("Fuck that, I'm escaping for myself.\n", "yellow")
        fprint("The crab tries to escape, but you just pull him down.\n", "dim")
        fprint("Hey fuck you buddy.\n", "yellow", 1)
        fprint("Whenever a crab tries to escape, the other crabs prevent them from doing anything, guaranteeing the deaths of all involved. The fisherman drives his boat back to his house and cooks everyone up.\n", "dim", 2)
        config.state = "Didn't you ever learn about Crab Mentality in school? \"While any one crab [trapped in a bucket] could easily escape, its efforts will be undermined by by others, ensuring the group's collective demise.\" Thanks Wikipedia.11"
    else:
        fprint("Wait, haven't any of you heard about Crab Mentality?\n", "cyan", 1.5)
        fprint("No, fuck off nerd.\n", "yellow")
        fprint("When crabs are trapped in a bucket, one crab could easily escape, but as a group, we make it impossible. So basically stop being dicks so we can escape.\n", "cyan", 1.5)
        fprint("Ok buddy.\n", "yellow", 1)
        fprint("You and several other crabs escape and tip over the bucket, flooding the bottom of the boat with crabs.\n", "dim", 1)
        fprint("FUCK! Crabs.. they, the- crabs? Crabs have, there's.. Oh no.\n", "blue", 1)
        fprint("The poor sap jumped overboard in his confusion. You and the rest of the gang jump off and return home.\n", "dim", 1)
        fprint("Philosophical concepts + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
    return queue

def d_forwardScuttle(queue):
    fprint("Yo, you wanna learn how to walk?", "yellow", 0)
    fprint("Some lobster calls out from across the street.\n", "dim", 1)
    fprint("I'm walking right now. I don't know what you mean.\n", "cyan")
    fprint("No, I mean like actually walking. You're just scuttling sideways.\n", "yellow")
    fprint("This dude seems lowkey sketchy. You wanna do this?\n", "green")

    answer = choice(["Let's go", "Let's no"])

    if answer == 1:
        fprint("Yeah, let's do this!\n", "cyan", 1.5)
        fprint("---2 fruitless hours later---\n", "dim", 2, 0)
        fprint("Dude, come on. We've been at this for a couple hours now. You haven't shown even a little improvement.\n", "yellow")
        fprint("I'm a crab, I just can't do it. I've let you down.\n", "cyan")
        fprint("You sure did, buddy.\n", "yellow", 1)
        fprint("Disappointment distilled in that lobster + 7", "rainbow", 1)
    else:
        fprint("Nah, you seem kinda sketchy man.\n", "cyan")
        fprint("Oh, is it because I'm a cape lobster? You racist fuck.\n", "yellow")
        fprint("No! I didn't mean it at all like that! It's just-\n", "cyan", 0)
        fprint("Just what, exactly? Am I scary? Are you afraid of lobsters?\n", "yellow", 1)
        fprint("You don't know what to say.", "dim", 1)
        fprint("The lobster walks off in a huff, all thanks to you. Good going.\n", "dim", 1)
        fprint("Racism + 3", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def d_gameShow(queue):
    money = 0
    fprint("You notice an unusually large envelope in your mailbox one breezy morning.\n", "dim", 1)
    fprint("Hmm, I wonder what this could be?\n", "cyan", 1)
    fprint("You pick up the envelope and open it. Inside there is a letter that reads the following:\n", "dim", 1)
    fprint("Hello from the representatives of MSNBSea's entertainment branch. \n  Congratulations! You have been selected as one of five participants for MSNBSea's venture into online broadcasted game shows. In the game show \"Seafront Feud\", you answer trivia questions about the great blue and win money! Will you accept our offer?\n", "yellow", 1)

    answer = choice(["Yes", "Yes, but farther down on your screen"])

    fprint("You follow the instructions printed on the letter by pricking your claw and soaking the paper in blood, chanting \"stultus locustam marinam\", and announcing your mother's maiden name out loud.\n", "dim", 2)
    fprint("Hey you feeling okay..?\n", "green", 2)
    pause()
    time.sleep(2)
    fprint("Holy shit dude, I thought you died.\n", "green", 1)
    fprint("You wake up in a foreign TV studio surrounded by crabs wearing business suits.\n", "dim")
    fprint("2 minutes everybody!", "yellow", 0)
    fprint("A crab in a stylish hat calls out, presumably the host.\n", "dim", 1)

    fprint("The lights in the studio dim as you get in a chair next to the host.\n", "dim", 1)

    fprint("Welcome to Seafront Feud!\n", "yellow")
    fprint("A fake applause sound effect echos throughout the studio.\n", "dim", 1)

    fprint("I'm here with my good friend who's about to win some money!\n", "yellow")
    fprint("The same sound effect thunders through the otherwise silent room.\n", "dim", 1)

    res = gameShow_question("Now, for the first question: Which zodiac sign represents the crab?", ["Pisces", "Cancer", "Libra", "Gemini"], 2, money)
    money = res[1]
    res = gameShow_question("Second question: How did you get into this studio?", ["Blood rite with The Devil", "Envelope laced with chloroform", "Fast travel", "Determination"], 2, money)
    money = res[1]
    if not res[0]:
        fprint("Okay that was a stupid question.\n", "cyan")
        fprint("Shh sh sh, you're not the host.\n", "yellow")
    else:
        fprint("Uh... Alright then.\n", "cyan")
    res = gameShow_question("Third question: What's my favorite color?", ["Red", "Light red", "Yellow", "Orange"], 4, money)
    money = res[1]
    if not res[0]:
        fprint("Really? That was worth money?\n", "cyan")
    else:
        fprint("Are these real questions?\n", "cyan")
        fprint("Yes, I can assure you that these are all real.\n", "yellow")
    fprint("Fourth question: What's my SECOND favorite col-\n", "yellow", 0)
    fprint("Yeah no I'm not finishing this.\n", "cyan", 1)

    fprint("Money + " + str(money), "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 1)
    config.experience += 1

    return queue

def gameShow_question(text, choices, answer, money):
    failResponses = ["Oof. Nope.", "Oh I'm sorry. That's not correct.", "Nope! You dummy!", "You utter fool, that's wrong!", "Nah dude, not even close.", "Was that a guess? Not a good one.", "Bad answer!", "Dummy.", "Idiot.", "Fool.", "Really? That's the answer you went with?"]
    fprint(text + "\n", "yellow")
    response = choice(choices)
    if response == answer:
        fprint("Correct! That's an extra 1 dollar towards your score!\n", "yellow")
        money += 1
        fprint("You now have " + str(money) + " " + gameShow_dollarPlural(money) + ".\n", "dim", 1)
        return (True, money)
    else:
        fprint(random.choice(failResponses) + " The correct answer was number " + str(answer) + ". You don't win anything this round.\n", "yellow")
        fprint("You still have " + str(money) + " " + gameShow_dollarPlural(money) + ".\n", "dim", 1)
        return (False, money)

def gameShow_dollarPlural(money):
    if money == 1:
        return "dollar"
    else:
        return "dollars"

def d_oldMan(queue):
    fprint("A visibly old male crab approaches you out of the shadows.\n", "dim", 1)
    fprint("Ey, you, kid.", "yellow", 0.5, 0.06)
    fprint("You new here or somethin?\n", "yellow", 0.5, 0.06)

    answer = choice(["Yes", "No"])

    if answer == 1:
        fprint("Uh yeah, actually. I was reincarnated here " + str(config.days) + " " + config.dayPlural() + " ago.\n", "cyan")
        fprint("Oh, dip. Well I hope I see ya around, kid. Good luck out there.\n", "yellow", 0.5, 0.06)
        fprint("Honesty be kinda quirky tho. Lowkey cool ig.\n", "green")
        fprint("Coolness + 1", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality += 1
        config.experience += 1
    else:
        fprint("Nah, I've been here a while now.\n", "cyan")
        fprint("Oh, word. Well I hope I see ya around, kid. Good luck out there.\n", "yellow", 0.5, 0.06)
        fprint("Woah, lies and deciet? That's pretty cool.\n", "green")
        fprint("Coolness + 1000", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality -= 1
        config.experience += 1

    queue.insert(0, "c_cringeNarrator.py")
    random.shuffle(queue)
    return queue

def d_paneraBreadGiftcard(queue):
    fprint("What the hell? Why do you need to be over 25 to purchase a Panera Bread giftcard?\n", "cyan")
    fprint("You do? That's fucking wack, man.\n", "green")
    fprint("I better do the only logical next step: get a fake ID!\n", "cyan", 1)
    fprint("Uh, sure buddy.\n", "green", 1)

    fprint("You meet up with your friend Carlos behind the Chili's near the post office.\n", "dim", 1)

    fprint("Hey man, you got the \"goods\"?", "cyan")
    fprint("You say really suspiciously.\n", "dim", 1)

    fprint("Um. Yeah. Do you still want it?\n", "yellow")

    answer = choice(["Ye", "Nope"])

    if answer == 1:
        fprint("Yea man, gimmie.\n", "cyan")
        fprint("Alright bro, take care.\n", "yellow")
        fprint("You exchange your goodbyes and start walking towards Panera Bread.\n", "dim", 1)
        fprint("Do I reeeaally wanna do this?\n", "cyan")

        answer = choice(["I demand bread", "Too dangerous"])

        if answer == 1:
            fprint("Let's go then!", "cyan")
            fprint("You say while walking into the restaurant.\n", "dim", 1)
            fprint("I would like to purchase a giftcard at this fine establishment, please.\n", "cyan")
            fprint("Can I see an ID?", "yellow")
            fprint("The waiter says.\n", "dim")
            fprint("You show your fake ID to the waiter.\n", "dim", 1)
            fprint("What kind of fool do you take me as? I'm calling the cops you sick fuck.\n", "yellow")
            fprint("Uh oh.\n", "green", 1)

            fprint("Days spent in the slammer + 2", "rainbow", 1)
            fprint("Badness + 1", "rainbow", 1)
            fprint("Experience + 1\n", "rainbow", 2)

            config.personality -= 1
            config.experience += 1
            config.days += 1 # jail time simulator

        else:
            fprint("Yeah on second thought maybe not.\n", "cyan")
            fprint("Fuckin pussy smh.\n", "green", 1)
            fprint("Goodness + 1", "rainbow", 1)
            fprint("Experience + 1\n", "rainbow", 2)
            config.personality += 1
            config.experience += 1
    else:
        fprint("Nah nevermind.\n", "cyan")
        fprint("So you're not gonna pay me?\n", "yellow")
        fprint("No thanks.\n", "cyan")
        fprint("Oh. Ok.", "yellow")
        fprint("He says as he walks away, glumly.\n", "dim")

        fprint("Fake ID + 0", "rainbow", 1)
        fprint("Goodness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality += 1
        config.experience += 1

    return queue

def d_peerPressure(queue):
    fprint("You're walking through downtown looking for a bite to eat when an adolecent crab runs up to you.\n", "dim", 1)
    fprint("Hey man, you look pretty cool. Wanna try some Benzoylmethylecgonine?\n", "yellow")
    fprint("Well, do you? All the cool crabs are doing it.\n", "green", 1)

    answer = choice(["Sure dude", "Nope"])

    if answer == 1:
        fprint("Well, I aaamm pretty cooool...\n", "cyan")
        fprint("Ayy, aight, well here you go.\n", "yellow", 1)
        fprint("He hands you a brown paper bag that you assume has Benzamyt-", "dim", 1)
        fprint("Benzomythe-", "dim", 1)
        fprint("Bensa-", "dim", 1)
        fprint("Whatever it was.\n", "dim", 1)

        fprint("Aight gotta run.", "yellow")
        fprint("He says as he runs off.\n", "dim", 1)

        fprint("You stand there a bit perplexed.\n", "dim", 1)
        fprint("Where's the ham fisted anti-drug message?\n", "cyan", 1)
        fprint("Suddenly...\n", "dim")
        fprint("HOW DARE YOU!", "rainbow")
        fprint("Says God.\n", "dim", 1)
        fprint("DRUGS? NOT COOL DUDE.\n", "rainbow", 1)
        fprint("Turns out God's a fucking nerd, amirite?\n", "green", 1)

        fprint("Coolness (in the eyes of God) - 100000000000", "rainbow", 1)
        fprint("Badness + 1", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.personality -= 1
        config.experience += 1
    else:
        fprint("Nah dude, drugs AREN'T cool.\n", "cyan")
        fprint("B-But I thought drugs were cool?\n", "yellow")
        fprint("Nope!\n", "cyan", 1)
        fprint("The adolecent crab throws his bag of Benzoylmethylecgonine on the ground and runs off in tears.\n", "dim", 1)
        fprint("God you're an asshole.\n", "green", 1)
        fprint("Uh, experience + 1 ig\n", "rainbow", 1)
        fprint("Not cool.\n", "rainbow", 2)
        config.experience += 1

    return queue

def d_pirates(queue):
    fprint("You're chilling by the beachside when all of a sudden...\n", "dim")

    fprint("AVAST, YE LADDIES! LAND HO!\n", "yellow")

    fprint("Crab pirates? That's a new one.\n", "green")

    fprint("The crabtain of the ship scuttles up to you.", "dim")
    fprint("Ahoy! Would ye like te join me ship? (arrg)\n", "yellow")

    answer = choice(["Hell yeah", "Hell no"])

    if answer == 1:
        fprint("Yeah sure dude.\n", "cyan")
        fprint("What? T'was a chortle, me laddie. Nobody wants your crab headass on thou ship.\n", "yellow")
        fprint("Oof. That's gotta hurt.\n", "green", 1)
        queue.insert(0, "c_supermarketPirate.py")
    else:
        fprint("Nah, not today man.\n", "cyan")
        fprint("B-but I thought you'd w-want to join?", "yellow")
        fprint("The crab says, fighting back tears.\n", "dim", 1)
        fprint("He hops back onto his galleon ship, crying all the way back. You prick.\n", "dim", 1)
    fprint("Disdain for pirates + 3", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def d_prawnShop(queue):
    fprint("Damn, I'm really craving some Taco Bell but I don't have any money.\n", "cyan")
    fprint("Well, what's a fast way to earn clean cash?\n", "green", 1)
    fprint("How about I just pawn some stuff off at a pawnshop? I don't see how this could go wrong in the slightest.\n", "cyan", 2)
    fprint("You approach the shop. The brick walls of the building look very old. The thick layer of dust coating the windows doesn't do much to help alleviate the sense of foreboding.\n", "dim", 1)
    fprint("Hello? Anyone here?", "cyan", 0)
    fprint("You call out while opening the door.\n", "dim", 1)
    fprint("Some noises can be heard from behind the counter, and eventually out pops a small fish.\n", "dim", 1)
    fprint("I'm Rick Herring, and this is my prawn shop. I work here with my old man and my son, Big Haddock. Everything in here has a story and a price. One thing I've learned after 21 years: you never know what is gonna come through that door.\n", "yellow", 1.5)
    fprint("Great, uh, I'm here to pawn off some stuff of mine.\n", "cyan")
    fprint("Well, what do you have in store?\n", "yellow")
    answer = choice(["My old laptop", "My Big Mouth Billy Bass", "My watch"])
    if answer == 1:
        fprint("I got an old laptop here. How much will you take it for?\n", "cyan", 2)
        fprint("...", "yellow", 1)
        fprint("Best I can do is $15.\n", "yellow", 2)
        fprint("With all the money you gained, you decide to buy 15 Beefy Fritos Burritos from Taco Bell.\n", "dim", 1)
        fprint("Old laptop - 1", "rainbow", 1)
        fprint("Beefy Fritos Burrito + 15", "rainbow", 1)
    elif answer == 2:
        fprint("I got a Big Mouth Billy Bass here. How much will you take it for?\n", "cyan", 1)
        fprint("Why tf would you think I want that?\n", "yellow", 1)
        fprint("Oh ok sorry.\n", "cyan", 1)
        fprint("Taco Bell + 0", "rainbow", 1)
    else:
        fprint("I got a watch here. How much will you take for it?\n", "cyan")
        fprint("My oh my, that is a fantastic watch. Tell you what, I'll give you $400 for it.\n", "yellow")
        fprint("Oh dope.\n", "cyan", 2)
        fprint("With all the money you gained, you decide to buy 400 Beefy Fritos Burritos from Taco Bell.\n", "dim", 1)
        fprint("Watch - 1", "rainbow", 1)
        fprint("Beefy Fritos Burrito + 400", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1
    return queue

def d_prisonersDilemma(queue):
    fprint("Blinding lights. You're strapped to a metal chair.\n", "dim")
    fprint("You've been imprisoned, but you have no memory of what you could've done.\n", "green")
    fprint("Hello? HeeeEEeellooOOOOooOO?\n", "cyan")
    fprint("Oh, hey, you're finally awake.", "yellow", 0)
    fprint("Says a crab in a lab coat, passing by your cell door\n", "dim")
    fprint("Don't worry, you're not in any trouble, (yet), we just brought you in for some experimenting.\n", "yellow")
    fprint("What? What?! That can't be legal.\n", "cyan")
    fprint("Idk, probably not but it'll be cool don't worry.\n", "yellow")
    fprint("The crab fiddles around with a clipboard for a second, then resumes his spiel.\n", "dim", 1)
    fprint("So basically there's another crab in the cell next to you. You guys can't hear each other or anything. I have enough evidence to convict both of you, but I'm gonna give you the choice to testify that the other guy did it.\n", "yellow")
    fprint("Okay, yeah, I do that.\n", "cyan")
    fprint("Whoa, hold your horses. If you both testify you'll each serve two years in prison. However, if the other guy testifies and you say nothing, then you're serving three and he's going free. The same goes if you testify and he stays silent.\n", "yellow")
    fprint("So what happens if we both say nothing?\n", "cyan")
    fprint("Then you each only get one year.\n", "yellow")
    fprint("Ok, cool.\n", "cyan")
    fprint("So, what are you gonna do?\n", "yellow")
    fprint("This is quite the ... dilemma.\n", "green")

    answer = choice(["Testify","Say nothing"])
    carlos = random.randint(1,2)


    if answer == 1 and carlos == 1:
        #two years
        clear()
        fprint("Ok, the other guy did it.\n", "cyan")
        fprint("Whoa, cool, let me go see what the other guy's gonna say.\n", "yellow")
        fprint("You wait a bit, tapping a sick 3:4 poly-rhythm on the metal chair.\n", "dim")
        fprint("Ok, I'm back, he says you did it too, have fun in jail for two years.\n", "yellow")
        fprint("What? No, you can't do this.\n", "cyan")
        fprint("Uhh, I can. Wanna meet the other guy?\n", "yellow")
        fprint("He leaves for a bit and escorts in another crab.\n", "dim")
        fprint("Holy shit, is that you Carlos?\n", "cyan")
        fprint("Aww man, what's up dude?\n", "blue")
        fprint("Wait, you know each other?\n", "yellow")
        fprint("Aw hell yeah dude, Carlos is the homie my guy.\n", "cyan")
        fprint("Shit man, we both testified?\n", "blue")
        fprint("Fuck yeaa\n", "cyan")
        fprint("Ayyyyy\n", "blue")
        fprint("Good god stop, okay, you're free, just please get out.\n","yellow")
        fprint("Ayyyy\n", "cyan")
        fprint("Ayyyy\n", "blue", 1)
        fprint("Whew, you got pretty lucky there.\n", "green", 1)
    elif answer == 1 and carlos == 2:
        #free
        clear()
        fprint("Ok, the other guy did it.\n", "cyan")
        fprint("Damn, let me see what he's gonna say.\n", "yellow")
        fprint("While he's gone for a bit you hum a few lines from a Frank Ocean song.\n", "dim")
        fprint("Alright, seems like the other guy doesn't want to talk. You're free, you can leave.\n", "yellow")
        fprint("What? Really? That's great!\n", "cyan")
        fprint("Yeah, yeah. Looks like you've put away a...", "yellow")
        fprint("He checks with clipboard.", "dim", 1)
        fprint("\"Carlos Sandchez\".\n", "yellow")
        fprint("Oh, that's the same Carlos Sandchez that you've known since prawn school.\n", "green")
        fprint("Uhh, cool. Don't know him. Never heard of him.\n", "cyan", 1)
        fprint("...Right. Anyway, yeah, go home.\n", "yellow", 1)
    elif answer == 2 and carlos == 1:
        clear()
        fprint("You just kind of sit there, silently.\n", "dim", 1)
        #three years
        fprint("...\n", "yellow", 1)
        fprint("...\n", "cyan", 1)
        fprint("Ohhh, you're staying silent.\n", "yellow")
        fprint("(Yeah)\n", "cyan")
        fprint("Cool cool. Let me see what the other guy said.\n", "yellow")
        fprint("While he's gone you blink 7 times.\n", "dim", 1)
        fprint("Ok, do you want the good news or the bad news?\n", "yellow")
        fprint("[1] Good news", "cyan", 0,0)
        fprint("[2] Bad news\n", "cyan",0,0)
        fprint(">>\n", "cyan",0,0)
        time.sleep(2)
        fprint("Jk it's just bad, the other guy testified see you in prison.\n", "yellow", 1)
        fprint("Ah fuck\n", "cyan", 2)
        config.state = "You don't aaaactually die, but go to jail for so many years it doesn't make a difference. Rip.13"

    elif answer == 2 and carlos == 2:
        #one year
        clear()
        fprint("You just kind of sit there, silently.\n", "dim", 1)
        fprint("...\n", "yellow", 1)
        fprint("...\n", "cyan", 1)
        fprint("Ohhh, you're staying silent.\n", "yellow")
        fprint("(Yeah)\n", "cyan")
        fprint("Oh nice, let me see what the other guy said.\n", "yellow")
        fprint("While he's gone you do nothing.\n", "dim")
        fprint("Huh, cool, that's never happened before.", "yellow", 0)
        fprint("He says to himself.\n", "dim")
        fprint("What?\n", "cyan")
        fprint("Other guy also said nothing, that's pretty cool.\n", "yellow")
        fprint("Fuck, that means prison for a year right?\n", "cyan")
        fprint("No, no, you won the game. You can leave.\n", "yellow")
        fprint("Oh, you're one of those social experiment guys, right?\n", "cyan")
        fprint("Sure, sure. Just leave.\n", "yellow")
        fprint("Cool.\n", "cyan", 1)

    fprint("Game theory + 2", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience + 1
    return queue

def d_purchaseSomeGoods(queue):
    fprint("I finally made it to Walmart! Let's see what I need to buy on my list...\n", "cyan", 1)
    fprint(" - Old bay", "dim", 1.5, 0)
    fprint(" - Bread", "dim", 1.5, 0)
    fprint(" - Milk\n", "dim", 1.5, 0)
    fprint("...\n", "cyan")
    fprint(" - Chlorine gas?\n", "dim", 1.5, 0)
    fprint("I wonder what I should get first?\n", "cyan")

    shoppingItems = ["Old bay", "Bread", "Milk", "Chlorine gas"]

    while True:
        answer = choice(shoppingItems)
        if shoppingItems[answer - 1] == "Old bay":
            purchaseSomeGoods_oldBay()
        elif shoppingItems[answer - 1] == "Bread":
            purchaseSomeGoods_bread()
        elif shoppingItems[answer - 1] == "Milk":
            purchaseSomeGoods_milk()
        elif shoppingItems[answer - 1] == "Chlorine gas":
            purchaseSomeGoods_chlorineGas()
        shoppingItems.pop(answer - 1)
        if len(shoppingItems) == 0:
            break
    fprint("You stare at your now empty shopping list.\n", "dim")
    fprint("Oh, radical. I'm outta here.\n", "cyan")

    fprint("Old Bay + 4", "rainbow", 1)
    fprint("Bread + 1", "rainbow", 1)
    fprint("Milk + 0", "rainbow", 1)
    fprint("Chlorine gas + 1", "yellow", 1)
    fprint("Wait, no, get out of the stats screen Shia LeBarnacle. Shoo.", "rainbow", 1)
    fprint("Uhh, also experience + 1\n", "rainbow", 2)

    return queue

def purchaseSomeGoods_oldBay():
    fprint("Well, I should obviously pick up the most important thi-\n", "cyan", 0)
    fprint("God, look at you.\n", "green", 2)
    fprint("What?\n", "cyan", 1)
    fprint("You're addicted. It's disgusting.\n", "green")
    fprint("Fuck you, I can stop at any time. I'm serious.\n", "cyan")
    fprint("Really? You can just stop using one of the most addictive drugs under the sea?\n", "green", 1)
    fprint("You guiltily put four cans of Old Bay into your shopping cart and cross it off your list.\n", "dim", 1)
    fprint("Right, now what's next?\n", "cyan")

def purchaseSomeGoods_bread():
    fprint("Oh, I forgot to write down which kind of bread. What should I go for?\n", "cyan")
    answer = choice(["White bread", "Multigrain"])
    if answer == 1:
        fprint("Really? White bread? I'm disappointed.\n", "green")
        fprint("Oh come on! White bread tastes a million times better than multigrain bread could even hope to taste like.\n", "cyan", 1)
        fprint("Alright, I guess I can't really fault you for that...\n", "green")
        fprint("You place a bag of white bread in your shopping cart and cross it off your list.\n", "dim", 1)
    else:
        fprint("Might as well eat healthier now that I'm a crab.\n", "cyan")
        fprint("Wow, only " + str(config.days) + " " + config.dayPlural() + " old and already making good life choices? I'm proud.\n", "green", 1)
        fprint("You proudly place a bag of multigrain bread in your shopping cart and cross it off your list.\n", "dim", 1)
    fprint("Right, what now?\n", "cyan")

def purchaseSomeGoods_milk():
    fprint("Oh wait, I'm lactose intolerant. I probably shouldn't drink that.\n", "cyan")
    fprint("You glumly cross milk off your list.\n", "dim", 1)
    fprint("Hmm, what's the next item I need?\n", "cyan")

def purchaseSomeGoods_chlorineGas():
    fprint("Chlorine gas? I don't remember writing that down...\n", "cyan")
    fprint("Suddenly, out of the corner of your eye you spot him: Shia LeBarnacle.\n", "dim", 1)
    fprint("Goddamn you Shia LeBarnacle and your poor attempts to murder me!\n", "cyan")
    fprint("He scampers off on all fours into the night.\n", "dim")
    fprint("Well, uh, what's next on the list?\n", "cyan")

def d_randomHotCrab(queue):
    fprint("Sigh, just another lonely walk down the street.", "cyan", 0)
    fprint("You think, gloomily scuttling along.\n", "dim")
    fprint("You look around.\n", "dim")
    fprint("A crab sweeping the sidewalk here,\n some kids running around,\n a... crab in a trenchcoat close behind them,\n and...\n", "cyan")
    fprint("Someone waving to me?\n", "cyan")
    fprint("Damn, she's kinda hot tho.\n", "green")
    fprint("Ikr?\n", "cyan")
    fprint("Wave back?\n", "green")
    answer = choice(["Yeah","Nah"])

    if answer == 1:
        fprint("Ok, I'm gonna do it.\n", "cyan")
        fprint("You slow down and quickly wave.\n", "dim")
        fprint("Oh shit she's walking over.\n", "green")
        fprint("You dust off your shell and get ready to talk to her.\n", "dim")
        fprint("Hey, what's up?\n", "cyan")
        fprint("What?\n", "yellow")
        fprint("She seems confused. Quickly, you look behind yourself.\n","dim")
        fprint("Oh god, it's her friend. She was definitely waving to her.\n", "green")
        fprint("Oh, your friend...\n", "cyan", 0.7)
        fprint("Uhh, yeah, cya.\n", "yellow", 2)
        fprint("She and her friend walk off, giggling.\n", "dim")
        fprint("Huh.\n", "cyan", 2)
        fprint("Huh.\n", "green", 2)
        fprint("Experience + 1", "rainbow", 2)
        fprint("Huh.\n", "rainbow", 2)
        queue.insert(0, "c_hotCrabSecondMeeting.py")
        random.shuffle(queue)
        config.experience += 1

    elif answer == 2:
        fprint("No, nevermind, I can't do it.\n", "cyan")
        fprint("Ok, whatever.\n", "green")
        fprint("The girl walks across the street towards you anyway.\n", "dim")
        fprint("Wait, what? What. What.\n", "cyan")
        fprint("Bro just chill, calm down.\n", "green")
        fprint("Ok, ok.\n", "cyan")
        fprint("She walks directly past you to her friend, who was standing behind you.\n", "dim")
        fprint("Holy shit that was close.\n", "green", 1)
        fprint("Relief + 3", "rainbow", 1)
        fprint("Experience + 1\n", "rainbow", 2)
        config.experience += 1
    return queue

def d_tasteTesting(queue):
    fprint("Oh boy, I sure am hungry! I wonder what I have in the fridge.\n", "cyan", 1)
    fprint("WAIT! I've set a curse on your refrigerator tur-\n", "green", 0)
    fprint("What?\n", "cyan", 1.5)
    fprint("A curse? You know?\n", "green", 1)
    fprint("I know what a curse is. What I don't know is why you put one on my refrigerator.\n", "cyan")
    fprint("Yeah I was getting to that, chill.", "green", 1)
    fprint("Anyways, uh, I saw this cool thing in a Vsauce video. Basically there's gonna be three cans of soup in your fridge. Two of them are completely normal, but one of them was made with a crab stock. Choose carefully, or you may be consuming your own brethren!\n", "green", 1)
    fprint("The narrator starts to maniacally laugh. You doubt his legitimacy as a good source of information.\n", "dim")

    cursedCan = random.randint(0, 2)
    cans = ["Blue can", "Red can", "Green can"]
    answer = choice(cans) - 1
    selectionCan = 0
    switchAnswer = 0
    while selectionCan == cursedCan or selectionCan == answer:
        selectionCan += 1
    while switchAnswer == answer or switchAnswer == selectionCan:
        switchAnswer += 1
    fprint("I choose-\n", "cyan", 0)
    fprint("BUT WAIT! The " + cans[selectionCan].lower() + " DOESN'T contain any crab stock! Do you wish to switch your selected can?\n", "green")
    newAnswer = choice(["Keep it on the " + cans[answer].lower(), "Switch it to the " + cans[switchAnswer].lower()])
    if newAnswer == 1:
        fprint("You fool! Switching would increase your chances of getting the cursed can to 2/3! Now let's see what the cursed can really is...\n", "green")
    else:
        fprint("Smart move. Switching increases your chance of getting the cursed can to 2/3. Now let's see what the cursed can really is...\n", "green")
    fprint("You hear a muffled drumroll from inside the fridge.\n", "dim", 1)
    if answer == cursedCan:
        fprint("You chose the " + cans[answer].lower() + ", which is also the cursed can! You imbecile!\n", "green", 1.5)
        fprint("Your heart races as you open the refrigerator door. There lies the " + cans[answer].lower() + ", mocking you. Calling to you as if to say \"please, please eat me\". You shudder, knowing what you must do.", "dim", 1)
        fprint("The microwave beeped deafeningly loud, with a piping hot can of soup inside. What have you become? Eating one of your own kind? Don't think that this isn't your fault. You deserve this.", "dim", 1)
        fprint("Your spoon extends into the surface of the tantalizing crab stock soup. You bring it closer and closer to your mouth.", "dim", 1.5)
        fprint("With a single gulp, you've committed the cardinal sin.", "dim", 2)
        fprint("You collapse to the ground, longing for the days where you didn't have to suffer like this. Tears stream down your eyes as you feel your ancestors looking down upon you in shame. Crabs, crayfish, lobsters, ants, humans, cats, dogs. They peer with a look of disgust over what you have become.\n", "dim", 3)
        fprint("Not bad.\n", "cyan", 1)
        fprint("Cannibalistic tendencies + 9", "rainbow", 1)
    else:
        fprint("You chose the " + cans[answer].lower() + ", but the cursed can was " + cans[cursedCan].lower() + ". You got off lucky THIS time...\n", "green")
        fprint("You reheat the " + cans[answer].lower() + " in the microwave and enjoy a nice dinner while watching the news.\n", "dim", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    config.experience += 1

    return queue

def d_wrongSecretAgent(queue):
    fprint("You're chilling at your house watching Cray's Anatomy on Netflix when your phone rings.\n", "dim", 1)
    fprint("RIIIIING. RIIIIIIIng. riiNIIINGGGN.\n", "red", 1)
    fprint("You pick up the phone.", "dim")
    fprint("Hey man this is Crab, what d-\n", "cyan", 0)
    fprint("Agent F5, your position has been compromised. Leave this building immediately and board the plane to Angola.\n", "yellow", 1)
    fprint("...", "cyan", 1)
    fprint("Who are you?\n", "cyan", 1)
    fprint("Is this not Agent Caspian?\n", "yellow")
    fprint("Nah.\n", "cyan", 1)
    fprint("...", "yellow", 1)
    fprint("Fuck.\n", "yellow", 1)
    fprint("The other crab hangs up the phone.\n", "dim")
    fprint("Wack.\n", "cyan", 1)

    fprint("Stealth - 4", "rainbow", 1)
    fprint("Experience + 1\n", "rainbow", 2)
    return queue

days = {
    "oldGuyDrugs": ["m_oldGuyDrugs_1.py", "m_oldGuyDrugs_2.py", "m_oldGuyDrugs_3.py"],
    "presidentialCampaign": ["m_presidentialCampaign_1.py", "m_presidentialCampaign_2.py", "m_presidentialCampaign_3.py"],
    "robberyTime": ["m_robberyTime_1.py", "m_robberyTime_2.py", "m_robberyTime_3.py", "m_robberyTime_4.py", "m_robberyTime_5.py", "m_robberyTime_6.py"],
    "soccerPractice": ["m_soccerPractice_1.py", "m_soccerPractice_2.py", "m_soccerPractice_3.py"],
    "burnWitch.py": d_burnWitch,
    "cookingCompetition.py": d_cookingCompetition,
    "crabExam.py": d_crabExam,
    "depression.py": d_depression,
    "firstContact.py": d_firstContact,
    "fisherman.py": d_fisherman,
    "forwardScuttle.py": d_forwardScuttle,
    "gameShow.py": d_gameShow,
    "oldMan.py": d_oldMan,
    "paneraBreadGiftcard.py": d_paneraBreadGiftcard,
    "peerPressure.py": d_peerPressure,
    "pirates.py": d_pirates,
    "prawnShop.py": d_prawnShop,
    "prisonersDilemma.py": d_prisonersDilemma,
    "purchaseSomeGoods.py": d_purchaseSomeGoods,
    "randomHotCrab.py": d_randomHotCrab,
    "tasteTesting.py": d_tasteTesting,
    "wrongSecretAgent.py": d_wrongSecretAgent,
    "c_broomHospital.py": c_broomHospital,
    "c_crabExamDeath.py": c_crabExamDeath,
    "c_cringeNarrator.py": c_cringeNarrator,
    "c_hotCrabSecondMeeting.py": c_hotCrabSecondMeeting,
    "c_presidentResign.py": c_presidentResign,
    "c_presidentStay.py": c_presidentStay,
    "c_supermarketPirate.py": c_supermarketPirate,
    "m_oldGuyDrugs_1.py": m_oldGuyDrugs_1,
    "m_oldGuyDrugs_2.py": m_oldGuyDrugs_2,
    "m_oldGuyDrugs_3.py": m_oldGuyDrugs_3,
    "m_presidentialCampaign_1.py": m_presidentialCampaign_1,
    "m_presidentialCampaign_2.py": m_presidentialCampaign_2,
    "m_presidentialCampaign_3.py": m_presidentialCampaign_3,
    "m_robberyTime_1.py": m_robberyTime_1,
    "m_robberyTime_2.py": m_robberyTime_2,
    "m_robberyTime_3.py": m_robberyTime_3,
    "m_robberyTime_4.py": m_robberyTime_4,
    "m_robberyTime_5.py": m_robberyTime_5,
    "m_robberyTime_6.py": m_robberyTime_6,
    "m_soccerPractice_1.py": m_soccerPractice_1,
    "m_soccerPractice_2.py": m_soccerPractice_2,
    "m_soccerPractice_3.py": m_soccerPractice_3
}
