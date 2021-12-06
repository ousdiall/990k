
import time
from time import sleep
import sys
import os
from idlecolors import *
####INTRODUCTION
n = input("Old man; Welcome, wandering warrior. What might your name be?: ")
for i in n:
    if i.isdigit():
       print("Old man; A numbered name, huh? Odd...")
       break
    else:
        n = n.capitalize()
        print("Old man; Welcome,",n,"!")
        break

n = n.capitalize()

##sleep(3)
##print("Old man; We've had an infestation of goblites recently!")
##sleep(3)
##print("Old man; No one in the town is capable of stopping those Goblites!")
##sleep(3)
##print("Old man; Unless")
##sleep(3)
##unless = "..."
##for i in unless:
##    print(i, end=" ")
##    sleep(0.5)
##print("Old man;",n,",can you help us?")
##while True:
##    m = input("(Y/N): ")
##    if m == "y" or m == "Yes" or m == "Y" or m == "yes":    
##        print("Old man; Thank you,",  n, "! But you need a weapon!")
##        sleep(1)
##        break
##    elif m == "n" or m == "No" or m == "N" or m == "no":
##        
##        print("Old man; Sucks to be you, you'll still help us!")
##        sleep(1)
##        break
##    else:
##        print("Old man; I don't quite understand...")
####CHOOSE A WEAPON
##print("Old man; Choose a sword, warrior.  Each sword has different properties")
##sleep(3)
##print("Old man; The Sword of Excalibur is a basic sword, but it works in all situations!")
##sleep(5)
##print("Old man; The Sword of Gemini is a chance-based sword. It's capable of dealing high damage, but gaze out, as you could take high damage as well!")
##sleep(5)
##print("Old man; The sword of Valkyrie is a sword yond heals for every successful attack, but deals low damage.")
##sleep(5)
##print("Old man; Which sword will you choose,", n, "?")

while True:
    o = input("1, 2, or 3? ")
    if o == "1" or o == "2" or o == "3":
        break
    else:
        print("Enter 1, 2, or 3.")
        sleep(1)
        
##print("Old man; Good choice, warrior")
##sleep(3)   
##print("Old man; Over there, warrior! A goblite! You will take care of it, will you?")
##sleep(3)

##BATTLE
enemy = 10
boss = 10
player = 30
healup = 2
powerup = 0
hypheal = 0
allpurp = 0


import random

def game():
    global enemy
    global player
    global healup
    global powerup
    global hypheal
    global allpurp
    for i in range(0, 1):
        while True:
            r = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            if r == 1 or r == 3 or r == 5 or r == 7 or r == 9:
                ##Goblin gets damaged
                
                    p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
                    p = p.lower()
                    if p == "p" or p == "power":
                        while True:
                            q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
                            q = q.lower()
                            if q == "hp" or q == "heal" or q == "pp" or q == "power" or q == "sp" or q == "super" or q == "ap" or q == "all":
                                break
                        if q == "hp" or q == "heal":
                            healup = healup - 1
                            if healup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                healup = 0
                                continue
                            else:
                                player = player + 5 
                                print("You have healed up for 5 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "pp" or q == "power":
                            powerup = powerup - 1
                            if powerup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                powerup = 0
                                continue
                            else:
                                print("You have powered up and hit the enemy for for 10 extra damage!")
                                enemy = enemy - 10
                                sleep(1)
                        if q == "sp" or q == "super":
                            hypheal = hypheal - 1
                            if hypheal < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                hypheal = 0
                                continue
                            else:
                                player = player + 25 
                                print("You have healed for 25 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "ap" or q == "all":
                            allpurp = allpurp - 1
                            if allpurp < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                allpurp = 0
                                continue
                            else:
                                player = player + 25
                                enemy = enemy - 30
                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
            
                    
                    elif p == "F" or p == "f" or p == "fight" or p == "Fight":
                            if o == "1":
                                print("The enemy took",r,"damage!")
                                enemy = enemy - r
                                sleep(1)
                                print("The enemy has",enemy,"Health left!")
                                sleep(1)
                            elif o == "2":
                                geminidamage = random.randint(5, 10)
                                r = r + geminidamage
                                print("The enemy took",r,"damage!")
                                enemy = enemy - r
                                sleep(1)
                                print("The enemy has",enemy,"Health left!")
                                sleep(1)
                            elif o == "3":
                                if r == 5:
                                    r = 3
                                    player = player + 3
                                    print("The enemy took",r,"damage, and you gained 3 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                elif r == 3:
                                    r == 1
                                    player = player + 1
                                    print("The enemy took",r,"damage, and you gained 1 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                elif r == 1:
                                    r = 0 
                                    print("The enemy took",r,"damage, and you gained no health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                else:
                                    r = r - 4
                                    player = player + 5
                                    print("The enemy took",r,"damage, and you gained 5 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)                           
                    
                    if enemy <= 0:
                        printc(green("The enemy has been defeated! Well done"))
                        sleep(1)
                        player = 30
                        break
            if r == 2 or r == 4 or r == 6 or r == 8:
                ##Player gets damaged          
                p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
                p = p.lower()
                if p == "p" or p == "power":
                        q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
                        q = q.lower()
                        if q == "hp" or q == "heal":
                            healup = healup - 1
                            if healup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                healup = 0
                                continue
                            else:
                                player = player + 5 
                                print("You have healed up for 5 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "pp" or q == "power":
                            powerup = powerup - 1
                            if powerup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                powerup = 0
                                continue
                            else:
                                print("You have powered up and hit the enemy for for 10 extra damage!")
                                enemy = enemy - 10
                                sleep(1)
                        if q == "sp" or q == "super":
                            hypheal = hypheal - 1
                            if hypheal < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                hypheal = 0
                                continue
                            else:
                                player = player + 25 
                                print("You have healed for 25 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "ap" or q == "all":
                            allpurp = allpurp - 1
                            if allpurp < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                allpurp = 0
                                continue
                            else:
                                player = player + 25
                                enemy = enemy - 30
                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                elif p == "F" or p == "f" or p == "Fight" or p == "fight":
                        if o == "1" or o == "3":
                            print("You took",r,"damage!")
                            player = player - r
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)
                        elif o == "2":
                            geminidamage = random.randint(5, 14)
                            r = r + geminidamage
                            print("You took",r,"damage!")
                            player = player - r
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)

                        
                if player <= 0:
                    printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
                    sleep(2)
                    m = input("Do you want to restart? (Y/N): ")
                    m = m.lower()
                    if m == "y" or m == "yes":
                        enemy = boss
                        player = 30
                        continue
                    elif m == "n" or m == "no":
                       sys.exit()
##game()
##creds = 0                
        
def finished():
        global player
        global c
        c = random.randint(150, 300)
        global creds   
        creds = creds + c
        sleep(1)
        print("You gained" ,c,"credits! You now have",creds,"credits!") 
        sleep(1)
        while True:
            m = input("Continue? (Y/N): ")
            m = m.lower()
            if m == "y" or m == "yes" or m == "n" or m == "no":
                break
        if m == "y" or m == "yes":
            pass
        elif m == "n" or m == "no":
            sys.exit()
        print(n,", You fought well! But danger lurks deep in the outside! ")
        sleep(1)
        while True:
            m = input("Would you like to buy something to help with your journey? (Y/N): ")
            m = m.lower()
            if m == "y" or m == "yes" or m == "n" or m == "no":
                break
        while m == "y" or m == "yes":
            printc(black("Potions For Sale!:"))
            sleep(0.5)
            printc(blue("Heal Potions (HP)- 50 Credits"))
            sleep(0.5)
            printc(green("Power Potions (PP)- 150 Credits"))
            sleep(0.5)
            printc(orange("Super Heal Potion (SP)- 200 Credits"))
            sleep(0.5)
            printc(red("All-Purpose Potion (AP)- 500 Credits"))
            sleep(1)
            print("You have",creds,"Credits.")
            
            while True:
                q = input("Which would you like to buy? (HP, PP, SP, AP)(N if none): ")
                q = q.lower()
                if q == "hp" or q == "pp" or q == "sp" or q == "ap" or q == "n" or q == "ba" or q == "sa" or q == "ga":
                    break
            #HEALTH    
            if q == "hp":
                if creds < 50:
                    print("You don't have enough!")
                    while True:
                        r = input("Would you like to go back to the shop? (Y/N): ")
                        r = r.lower()
                        if r == "y" or r == "yes" or r == "n" or r == "no":
                            break
                    if r == "y" or r == "yes":
                        continue
                    elif r == "n" or r == "no":
                        break 
                else:
                     global healup
                     healup += 1
                     creds = creds - 50
                     print("You now have", healup, "Heal Potions")
                     sleep(1)
                     print("You have", creds, "Credits left.")
              #POWER UP      
            elif q == "pp":
                if creds < 150:
                        print("You don't have enough!")
                        while True:
                            r = input("Would you like to go back to the shop? (Y/N): ")
                            r = r.lower()
                            if r == "y" or r == "yes" or r == "n" or r == "no":
                                break
                        if r == "y" or r == "yes":
                            continue
                        elif r == "n" or r == "no":
                            break
                else:
                        global powerup
                        powerup += 1
                        creds = creds - 150
                        print("You now have", powerup,"Power Potions!")
                        sleep(1) 
                        print("You have", creds, "Credits left.")
             #SUPER HEAL           
            elif q == "sp":
                if creds < 200:
                    print("You don't have enough!")
                    while True:
                            r = input("Would you like to go back to the shop? (Y/N): ")
                            r = r.lower()
                            if r == "y" or r == "yes" or r == "n" or r == "no":
                                break
                    if r == "y" or r == "yes":
                        continue
                    elif r == "n" or r == "no":
                        break
                else:
                    global hypheal
                    hypheal += 1
                    print("You now have", hypheal,"Super Healing Potions!")
                    sleep(1)
                    creds = creds - 200
                    print("You have", creds, "Credits left.")
             #ALL PURPOSE           
            elif q == "ap":
                if creds < 500:
                    print("You don't have enough!")
                    while True:
                            r = input("Would you like to go back to the shop? (Y/N): ")
                            r = r.lower()
                            if r == "y" or r == "yes" or r == "n" or r == "no":
                                break
                    if r == "y" or r == "yes":
                        continue
                    elif r == "n" or r == "no":
                        break
                else:
                    global allpurp
                    allpurp += 1
                    print("You now have", allpurp,"All-Purpose Potions!")
                    sleep(1)
                    creds = creds - 500
                    print("You have", creds, "Credits left.")
            elif q == "n":
                break
            sleep(1)
            while True:
                r = input("Would you like to buy something else?(Y/N): ")
                r = r.lower()
                if r == "y" or r == "yes" or r == "n" or r == "no":
                    break
            if r == "y" or r == "yes":
                continue
            elif r == "n" or r == "no":
                break
        while m == "n" or m == "no":
             break
            

############## BIG BOSS

##            
##finished()
##sleep(1)
##printc(orange("Let's move on"))
##sleep(3)
##print("Old man; ",n,", Before you venture out, I need to remind you that there are different types of Goblites.")
##sleep(3)
##print("Old man; Even some that I haven't seen before.")
##sleep(3)
##print("Old man; You must be careful! You're our town's only hope!")
##sleep(3)
##printc(orange("You venture out of the town to seek the leader of the Goblites"))
##sleep(3)
##printc(orange("Suddenly, you feel a rumble, almost like an earthquake. You stand still and hold your sword firm."))
##sleep(3)
##printc(red("There appears a Bigoblite! Equppied with 2 swords and 20 Health!"))
##sleep(3)
##printc(orange("Defend yourself!"))
##sleep(2)
##
##boss = 20
##enemy = 20
##game()
##finished()
##
################          BOMB BOSS
##
##            
##print("Good Job,",n,"!")
##sleep(3)
##printc(orange("You make your way through the forest, and you see a fortress ahead!"))
##sleep(3)
##printc(orange("Maybe this is where the Goblite hideout is at?"))
##sleep(3)
##printc(orange("As you walk towards the fortress, you hear a click sound as you step"))
##sleep(3)
##printc(orange("You stand still, but then a fizzing sound"))
##unless = "..."
##for i in unless:
##  print(i, end=" ")
##  sleep(0.5)
##
##printc(red("BOOOOOOMMMM"))
##player = player - 6
##sleep(3)
##printc(orange("A blast that blazes through the forest!"))
##sleep(3)
##printc(orange("You are damaged, but you are still able to fight!"))
##sleep(3)
##printc(orange("You hear a giggle from one of the trees"))
##sleep(3)
##printc(orange("It's a goblite, but not no ordinary one!"))
##sleep(3)
##printc(orange("Defend yourself, and dodge the dynamites!"))
##sleep(3)
##
##boss = 27
##enemy = 27
##
##
##while True:
##    now = time.time()
##    time_limit = 1.3
##    end_time = now + time_limit
##    letter = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
##    print("Type the letter",letter,"within 1 seconds!")
##    i = input()
##    if time.time() >= end_time:
##        player = player - 6
##        printc(red("You took a hit! The enemy blew away 6 of your Health!"))
##        sleep(1)
##        print("You have",player,"Health left!")
##        sleep(1)
##    elif i != letter:
##        player = player - 6
##        printc(red("You took a hit! The enemy blew away 6 of your Health!"))
##        sleep(1)
##        print("You have",player,"Health left!")
##        sleep(1)
##    if i == letter and time.time() <= end_time:
##        enemy = enemy - 3
##        print("You dodged and attacked! The enemy has",enemy,"Health left!")
##        sleep(1)
##    
##    if enemy <= 0:
##        print("The Bomber Goblite has no more bombs, but he still has a wooden sword! Fight,",n,"!")
##        sleep(1)
##        break
##    if player <= 0:
##        printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
##        sleep(2)
##        m = input("Do you want to restart? (Y/N): ")
##        m = m.lower()
##        if m == "y" or m == "yes":
##            enemy = boss
##            player = 30
##            continue
##        elif m == "n" or m == "no":
##           sys.exit()
######Most of the timer code from https://www.reddit.com/r/learnpython/comments/63b6tp/any_way_to_have_a_countdown_while_basic_guessing/
##           
##boss = 10
##enemy = 10
##game()
##finished()
##
##############             WIZARD BOSS
##print("Good Job,",n,"!")
##sleep(3)
##printc(orange("After getting the ringing out of your ears from the explosions, you carry on."))
##sleep(3)
##printc(orange("You make your way towards the walls of the fortress, trying to find a way in other than the gate in the front."))
##sleep(3)
##printc(orange("You find a window, and you climb through it."))
##sleep(3)
##printc(orange("As you get in, you notice the vast amounts beakers, test tubes, and organisms which you have never seen before."))
##sleep(3)
##printc(orange("You explore the room, but you accidentally trip over a wire, which causes a beaker to fall."))
##sleep(3)
##printc(orange("The door behind opens, and reveals a Mad Goblite Wizard!"))
##sleep(3)
##print("Defend yourself,",n,"!")
##sleep(1)
##printc(red("As the wizard is above 20 Health, he can parry attacks!"))
##boss = 30
##enemy = 30
##
##for i in range(0, 1):
##        while True:
##            r = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
##            if r == 1 or r == 3 or r == 5 or r == 7:
##                
##                ##Goblin gets damaged
##                
##                    p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
##                    p = p.lower()
##                    if p == "p" or p == "power":
##                        while True:
##                            q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
##                            q = q.lower()
##                            if q == "hp" or q == "heal" or q == "pp" or q == "power" or q == "sp" or q == "super" or q == "ap" or q == "all":
##                                break
##                        if q == "hp" or q == "heal":
##                            healup = healup - 1
##                            if healup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                healup = 0
##                                continue
##                            else:
##                                player = player + 5 
##                                print("You have healed up for 5 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "pp" or q == "power":
##                            powerup = powerup - 1
##                            if powerup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                powerup = 0
##                                continue
##                            else:
##                                print("You have powered up and hit the enemy for for 10 extra damage!")
##                                enemy = enemy - 10
##                                sleep(1)
##                        if q == "sp" or q == "super":
##                            hypheal = hypheal - 1
##                            if hypheal < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                hypheal = 0
##                                continue
##                            else:
##                                player = player + 25
##                                print("You have healed for 25 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "ap" or q == "all":
##                            allpurp = allpurp - 1
##                            if allpurp < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                allpurp = 0
##                                continue
##                            else:
##                                player = player + 25
##                                enemy = enemy - 30
##                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##            
##                    
##                    elif p == "F" or p == "f" or p == "fight" or p == "Fight":
##                        if r == 3 and enemy >= 20:
##                            player = player - r
##                            print("The Wizard reflected the attack! You took",r,"damage!")
##                            sleep(1)
##                            print("You have",player,"Health left!")
##                            sleep(1)
##                        elif r == 3 and enemy <= 20:
##                            print("The Wizard tried to put a spell on you, but you reflect the damage back!")
##                            sleep(1)
##                            r = r + 9
##                            enemy = enemy - r
##                            print("The enemy has",enemy,"Health left!")
##                            sleep(1)
##                        else:
##                            if o == "1":
##                                print("The enemy took",r,"damage!")
##                                enemy = enemy - r
##                                sleep(1)
##                                print("The enemy has",enemy,"Health left!")
##                                sleep(1)
##                            elif o == "2":
##                                geminidamage = random.randint(5, 10)
##                                r = r + geminidamage
##                                print("The enemy took",r,"damage!")
##                                enemy = enemy - r
##                                sleep(1)
##                                print("The enemy has",enemy,"Health left!")
##                                sleep(1)
##                            elif o == "3":
##                                if r == 5:
##                                    r = 3
##                                    player = player + 3
##                                    print("The enemy took",r,"damage, and you gained 3 health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)
##                                elif r == 1:
##                                    r = 0 
##                                    print("The enemy took",r,"damage, and you gained no health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)
##                                else:
##                                    r = r - 4
##                                    player = player + 5
##                                    print("The enemy took",r,"damage, and you gained 5 health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)                           
##                    
##                    if enemy <= 0:
##                        printc(green("The enemy has been defeated! Well done"))
##                        hypheal = hypheal + 1
##                        powerup = powerup + 1
##                        sleep(1)
##                        print("You gained 1 Super Healing Potion and 1 Powerup Potion!")
##                        sleep(1)
##                        player = 30
##                        break
##                    elif player <= 0:
##                        printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
##                        sleep(2)
##                        m = input("Do you want to restart? (Y/N): ")
##                        m = m.lower()
##                        if m == "y" or m == "yes":
##                            enemy = boss
##                            player = 30
##                            continue
##                        elif m == "n" or m == "no":
##                            sys.exit()
##            if r == 2 or r == 4 or r == 6 or r == 8:
##                ##Player gets damaged          
##                p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
##                p = p.lower()
##                if p == "p" or p == "power":
##                        q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
##                        q = q.lower()
##                        if q == "hp" or q == "heal":
##                            healup = healup - 1
##                            if healup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                healup = 0
##                                continue
##                            else:
##                                player = player + 5 
##                                print("You have healed up for 5 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "pp" or q == "power":
##                            powerup = powerup - 1
##                            if powerup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                powerup = 0
##                                continue
##                            else:
##                                print("You have powered up and hit the enemy for for 10 extra damage!")
##                                enemy = enemy - 10
##                                sleep(1)
##                        if q == "sp" or q == "super":
##                            hypheal = hypheal - 1
##                            if hypheal < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                hypheal = 0
##                                continue
##                            else:
##                                player = player + 25
##                                print("You have healed for 25 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "ap" or q == "all":
##                            allpurp = allpurp - 1
##                            if allpurp < 0:
##                                print("You have no more of these potions!")
##                                sleep(1)
##                                allpurp = 0
##                                continue
##                            else:
##                                player = player + 25
##                                enemy = enemy - 30
##                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                elif p == "F" or p == "f" or p == "Fight" or p == "fight":
##                        if r == 4 and enemy >= 20:
##                            player = player - r
##                            print("The Wizard reflected the attack! You took",r,"damage!")
##                            sleep(1)
##                            print("You have",player,"Health left!")
##                            sleep(1)
##                        elif r == 4 and enemy <= 20:
##                            print("The Wizard tried to put a spell on you, but you reflect the damage back!")
##                            sleep(1)
##                            r = r + 8
##                            enemy = enemy - r
##                            print("The enemy has",enemy,"Health left!")
##                            sleep(1)
##                        else: 
##                            if o == "1":
##                                print("You took",r,"damage!")
##                                player = player - r
##                                sleep(1)
##                                print("You have",player,"Health left!")
##                                sleep(1)
##                            elif o == "2":
##                                geminidamage = random.randint(5, 14)
##                                r = r + geminidamage
##                                print("You took",r,"damage!")
##                                player = player - r
##                                sleep(1)
##                                print("You have",player,"Health left!")
##                                sleep(1)
##                            elif o == "3":
##                                print("You took",r,"damage!")
##                                player = player - r
##                                sleep(1)
##                                print("You have",player,"Health left!")
##                                sleep(1)
##                if player <= 0:
##                    printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
##                    sleep(2)
##                    m = input("Do you want to restart? (Y/N): ")
##                    m = m.lower()
##                    if m == "y" or m == "yes":
##                        enemy = boss
##                        player = 30
##                        continue
##                    elif m == "n" or m == "no":
##                        sys.exit()
##
##                        
##                
##finished()
##
####### KNIGHT FIGHT
##print("Good Job,",n,"!")
##sleep(3)
##printc(orange("You sneak through the fortress, to find who is in charge."))
##sleep(3)
##printc(orange("You then hear the sound of many goblites, seemingly talking."))
##sleep(3)
##printc(orange("You hide behind a barrel, and there you see many goblites carrying heavy items and working hard. "))
##sleep(3)
##printc(orange("And a throne in the middle of the room."))
##sleep(3)
##printc(orange("You realize the King is away, which could be a great opportunity to seize him."))
##sleep(3)
##printc(orange("You sneak through the fortress again, and see a room with a door that's different from the rest..."))
##sleep(3)
##printc(orange("You crank the door open, and you see a crown on a Goblite's head! The King!"))
##sleep(3)
##printc(orange("You wonder how you will deal with him, when suddenly..."))
##sleep(3)
##printc(orange("An armored knight stands behind you, his sword pointed towards your back."))
##sleep(3)
##printc(orange('"You really think you could sneak around?", the Knight says.'))
##sleep(3)
##printc(orange("While the knight boasts, you quickly turn back and draw your sword."))
##sleep(3)
##print("Defend yourself,",n,"!")
##sleep(1)
##printc(red("But beware, he wields the sword of Valkyrie, which can heal him!"))
##sleep(3)
##
##boss = 36
##enemy = 36
##for i in range(0, 1):
##        while True:
##            r = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
##            if r == 1 or r == 3 or r == 5 or r == 7:
##                ##Goblin gets damaged
##                
##                    p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
##                    p = p.lower()
##                    if p == "p" or p == "power":
##                        while True:
##                            q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
##                            q = q.lower()
##                            if q == "hp" or q == "heal" or q == "pp" or q == "power" or q == "sp" or q == "super" or q == "ap" or q == "all":
##                                break
##                        if q == "hp" or q == "heal":
##                            healup = healup - 1
##                            if healup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                healup = 0
##                                continue
##                            else:
##                                player = player + 5 
##                                print("You have healed up for 5 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "pp" or q == "power":
##                            powerup = powerup - 1
##                            if powerup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                powerup = 0
##                                continue
##                            else:
##                                print("You have powered up and hit the enemy for for 10 extra damage!")
##                                enemy = enemy - 10
##                                sleep(1)
##                        if q == "sp" or q == "super":
##                            hypheal = hypheal - 1
##                            if hypheal < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                hypheal = 0
##                                continue
##                            else:
##                                player = player + 25
##                                print("You have healed for 25 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "ap" or q == "all":
##                            allpurp = allpurp - 1
##                            if allpurp < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                allpurp = 0
##                                continue
##                            else:
##                                player = player + 25
##                                enemy = enemy - 30
##                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##            
##                    
##                    elif p == "F" or p == "f" or p == "fight" or p == "Fight":
##                            if o == "1":
##                                print("The enemy took",r,"damage!")
##                                enemy = enemy - r
##                                sleep(1)
##                                print("The enemy has",enemy,"Health left!")
##                                sleep(1)
##                            elif o == "2":
##                                geminidamage = random.randint(5, 10)
##                                r = r + geminidamage
##                                print("The enemy took",r,"damage!")
##                                enemy = enemy - r
##                                sleep(1)
##                                print("The enemy has",enemy,"Health left!")
##                                sleep(1)
##                            elif o == "3":
##                                if r == 5:
##                                    r = 3
##                                    player = player + 3
##                                    print("The enemy took",r,"damage, and you gained 3 health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)
##                                elif r == 3:
##                                    r == 1
##                                    player = player + 1
##                                    print("The enemy took",r,"damage, and you gained 1 health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)
##                                elif r == 1:
##                                    r = 0 
##                                    print("The enemy took",r,"damage, and you gained no health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)
##                                else:
##                                    r = r - 4
##                                    player = player + 5
##                                    print("The enemy took",r,"damage, and you gained 5 health!")
##                                    enemy = enemy - r
##                                    sleep(1)
##                                    print("The enemy has",enemy,"Health left!")
##                                    sleep(1)                           
##                    
##                    if enemy <= 0:
##                        printc(green("The enemy has been defeated! Well done"))
##                        sleep(1)
##                        player = 40
##                        break
##            if r == 2 or r == 4 or r == 6 or r == 8:
##                ##Player gets damaged          
##                p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
##                p = p.lower()
##                if p == "p" or p == "power":
##                        q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
##                        q = q.lower()
##                        if q == "hp" or q == "heal":
##                            healup = healup - 1
##                            if healup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                healup = 0
##                                continue
##                            else:
##                                player = player + 5 
##                                print("You have healed up for 5 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "pp" or q == "power":
##                            powerup = powerup - 1
##                            if powerup < 0: 
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                powerup = 0
##                                continue
##                            else:
##                                print("You have powered up and hit the enemy for for 10 extra damage!")
##                                enemy = enemy - 10
##                                sleep(1)
##                        if q == "sp" or q == "super":
##                            hypheal = hypheal - 1
##                            if hypheal < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                hypheal = 0
##                                continue
##                            else:
##                                player = player + 25 
##                                print("You have healed for 25 Health!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                        if q == "ap" or q == "all":
##                            allpurp = allpurp - 1
##                            if allpurp < 0:
##                                printc(red("You have no more of these potions!"))
##                                sleep(1)
##                                allpurp = 0
##                                continue
##                            else:
##                                player = player + 25
##                                enemy = enemy - 30
##                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
##                                sleep(1)
##                                print("You have",player,"Health now!")
##                                sleep(1)
##                elif p == "F" or p == "f" or p == "Fight" or p == "fight":
##                        if o == "1" or o == "3":
##                            if r == 6 or r == 8:
##                                r = r - 3
##                            print("You took",r,"damage! and the Knight gained",r,"Health!")
##                            player = player - r        
##                            enemy = enemy + r
##                            sleep(1)
##                            print("You have",player,"Health left!")
##                            sleep(1)
##                        elif o == "2":
##                            if r == 6 or r == 8:
##                                r = r - 3
##                            geminidamage = random.randint(5, 14)
##                            enemy = enemy + r
##                            r = r + geminidamage
##                            print("You took",r,"damage! and the Knight gained",r,"Health!")
##                            player = player - r
##                            sleep(1)
##                            print("You have",player,"Health left!")
##                            sleep(1)
##                        
##                if player <= 0:
##                    printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
##                    sleep(2)
##                    m = input("Do you want to restart? (Y/N): ")
##                    m = m.lower()
##                    if m == "y" or m == "yes":
##                        enemy = boss
##                        player = 40
##                        continue
##                    elif m == "n" or m == "no":
##                       sys.exit()
##
##finished()
##
##### THE KING
##print("Good Job,",n,"!")
##sleep(3)
##printc(orange("You make your way towards the room, but you see the king standing in front of the doorway."))
##sleep(3)
##printc(orange('"Filthy humans, I will eradicate your kind!", says the King.'))
##sleep(3)
##printc(red("Be prepared, warrior, this could be the toughest battle yet."))
##sleep(3)
##
##boss = 3
##enemy = 3
##game()
##unless = "..."
##for i in unless:
##    print(i, end=" ")
##    sleep(0.5)
##sleep(3)
##printc(orange("You stand dazed at what just happened..."))
##sleep(3)
##printc(orange('You wonder to yourself "That was way too easy".'))
##sleep(3)
##printc(orange("Suddenly, you hear clapping at the corner, a shadow-y figure."))
##sleep(3)
##printc(orange('"Good job, but I would not celebrate if I were you".'))
##sleep(3)
##printc(orange("The figure raises his arm, a pale human arm? This isn't no Goblite..."))
##sleep(3)
##printc(orange("Suddenly, he chants something, and then something appears!"))
##sleep(3)
##printc(orange("And then something else!"))
##sleep(3)
##printc(orange("And another!"))
##sleep(3)
##printc(orange("These are"))
##sleep(3)
##for i in unless:
##    print(i, end=" ")
##    sleep(0.5)
##    
##printc(orange("All the Goblites that you've slain?!?"))
##sleep(3)
##printc(orange("That's not all, he's combining them into one!"))
##sleep(3)
##printc(orange("The burliness of the Bigoblite!"))
##sleep(3)
##printc(orange("The bombs that belong to the Bomber Goblite!"))
##sleep(3)
##printc(orange("The potions and brains, that of the Mad Wizard!"))
##sleep(3)
##printc(orange("The sword of Valkyrie, belonging to the knight!"))
##sleep(3)
##printc(orange("The creature is unstable, destroying the tables and shaking the ground with it's monstorous stomps!"))
##sleep(3)
##printc(orange("And then it looks at you..."))
##sleep(3)
##print("Defend yourself,",n,"!")
##sleep(3)

boss = 50
enemy = 50
for i in range(0, 1):
        while True:
            r = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
            if r == 1 or r == 3 or r == 5 or r == 7:
                ##Goblin gets damaged
                
                    p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
                    p = p.lower()
                    if p == "p" or p == "power":
                        while True:
                            q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
                            q = q.lower()
                            if q == "hp" or q == "heal" or q == "pp" or q == "power" or q == "sp" or q == "super" or q == "ap" or q == "all":
                                break
                        if q == "hp" or q == "heal":
                            healup = healup - 1
                            if healup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                healup = 0
                                continue
                            else:
                                player = player + 5 
                                print("You have healed up for 5 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "pp" or q == "power":
                            powerup = powerup - 1
                            if powerup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                powerup = 0
                                continue
                            else:
                                print("You have powered up and hit the enemy for for 10 extra damage!")
                                enemy = enemy - 10
                                sleep(1)
                        if q == "sp" or q == "super":
                            hypheal = hypheal - 1
                            if hypheal < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                hypheal = 0
                                continue
                            else:
                                player = player + 25
                                print("You have healed for 25 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "ap" or q == "all":
                            allpurp = allpurp - 1
                            if allpurp < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                allpurp = 0
                                continue
                            else:
                                player = player + 25
                                enemy = enemy - 30
                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
            
                    
                    elif p == "F" or p == "f" or p == "fight" or p == "Fight":
                        if r == 3 or r == 5:
                            player = player - r
                            print("The creature dodged the attack and tackles you! You took",r,"damage!")
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)
                        else:
                            if o == "1":
                                print("The enemy took",r,"damage!")
                                enemy = enemy - r
                                sleep(1)
                                print("The enemy has",enemy,"Health left!")
                                sleep(1)
                            elif o == "2":
                                geminidamage = random.randint(5, 10)
                                r = r + geminidamage
                                print("The enemy took",r,"damage!")
                                enemy = enemy - r
                                sleep(1)
                                print("The enemy has",enemy,"Health left!")
                                sleep(1)
                            elif o == "3":
                                if r == 5:
                                    r = 3
                                    player = player + 3
                                    print("The enemy took",r,"damage, and you gained 3 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                elif r == 3:
                                    r == 1
                                    player = player + 1
                                    print("The enemy took",r,"damage, and you gained 1 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                elif r == 1:
                                    r = 0 
                                    print("The enemy took",r,"damage, and you gained no health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)
                                else:
                                    r = r - 4
                                    player = player + 5
                                    print("The enemy took",r,"damage, and you gained 5 health!")
                                    enemy = enemy - r
                                    sleep(1)
                                    print("The enemy has",enemy,"Health left!")
                                    sleep(1)                           
                    
                    if enemy <= 0:
                        printc(green("The enemy has been defeated! Well done"))
                        sleep(1)
                        player = 40
                        break
                    elif player <= 0:
                        printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
                        sleep(2)
                        m = input("Do you want to restart? (Y/N): ")
                        m = m.lower()
                        if m == "y" or m == "yes":
                            enemy = boss
                            player = 40
                            continue
                        elif m == "n" or m == "no":
                           sys.exit()
            if r == 2 or r == 4 or r == 6 or r == 8:
                ##Player gets damaged          
                p = input("Would you like to fight or use a powerup? (P to power up, F to fight.): ")
                p = p.lower()
                if p == "p" or p == "power":
                        q = input("Would you like to Heal(HP), Power Boost(PP), Super Heal(SP), or use an All-Purpose(AP)?")
                        q = q.lower()
                        if q == "hp" or q == "heal":
                            healup = healup - 1
                            if healup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                healup = 0
                                continue
                            else:
                                player = player + 5 
                                print("You have healed up for 5 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "pp" or q == "power":
                            powerup = powerup - 1
                            if powerup < 0: 
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                powerup = 0
                                continue
                            else:
                                print("You have powered up and hit the enemy for for 10 extra damage!")
                                enemy = enemy - 10
                                sleep(1)
                        if q == "sp" or q == "super":
                            hypheal = hypheal - 1
                            if hypheal < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                hypheal = 0
                                continue
                            else:
                                player = player + 25
                                print("You have healed for 25 Health!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                        if q == "ap" or q == "all":
                            allpurp = allpurp - 1
                            if allpurp < 0:
                                printc(red("You have no more of these potions!"))
                                sleep(1)
                                allpurp = 0
                                continue
                            else:
                                player = player + 25
                                enemy = enemy - 30
                                print("You have healed for 25 Health and hit the enemy for 30 extra damage!")
                                sleep(1)
                                print("You have",player,"Health now!")
                                sleep(1)
                elif p == "F" or p == "f" or p == "Fight" or p == "fight":
                    if r == 2:
                            r = r + 3
                            player = player - r
                            printc(red("The creature spat out a toxic substance onto you! You took extra damage!"))
                            sleep(1)
                            print("You took",r,"damage!")
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)
                    elif r == 6 or r == 8:
                        printc(red("The creature is rumbling, prepare to dodge the explosive potions!"))
                        sleep(2)
                        enemyB = 9
                        while True:
                                now = time.time()
                                time_limit = 1.4
                                end_time = now + time_limit
                                letter = random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
                                print("Type the letter",letter,"within 1 seconds!")
                                i = input()
                                if time.time() >= end_time:
                                    player = player - 10
                                    printc(red("You took a hit! The creature blew away 10 of your Health!"))
                                    sleep(1)
                                    print("You have",player,"Health left!")
                                    sleep(1)
                                if i == letter and time.time() <= end_time:
                                    enemyB = enemyB - 3
                                    print("You dodged and attacked!")
                                    sleep(1)
                                elif i != letter:
                                    player = player - 10
                                    printc(red("You took a hit! The creature blew away 10 of your Health!"))
                                    sleep(1)
                                    print("You have",player,"Health left!")
                                    sleep(1)
                                if enemyB <= 0:
                                    print("The creature has no more explosive potions")
                                    sleep(1)
                                    print("For now...")
                                    sleep(1)
                                    enemy = enemy - 10
                                    break
                                if player <= 0:
                                    printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
                                    sleep(2)
                                    m = input("Do you want to restart? (Y/N): ")
                                    m = m.lower()
                                    if m == "y" or m == "yes":
                                        enemy = 50
                                        player = 40
                                        break
                                    elif m == "n" or m == "no":
                                       sys.exit()
                    else:
                        if o == "1" or o == "3":
                            print("You took",r,"damage!")
                            player = player - r        
                            enemy = enemy + r
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)
                        elif o == "2":
                            geminidamage = random.randint(5, 14)
                            enemy = enemy + r
                            r = r + geminidamage
                            print("You took",r,"damage!")
                            player = player - r
                            sleep(1)
                            print("You have",player,"Health left!")
                            sleep(1)
                        
                if player <= 0:
                    printc(red("Warrior......Warrior?!?!? WAAAARRRRIIIOOOOOOORRRRRR!!!!!"))
                    sleep(2)
                    m = input("Do you want to restart? (Y/N): ")
                    m = m.lower()
                    if m == "y" or m == "yes":
                        enemy = boss
                        player = 40
                        continue
                    elif m == "n" or m == "no":
                       sys.exit()
printc(orange("After slaying the monster, you find the shadow figure mumbling to himself"))
sleep(3)
printc(orange("You wonder if the goblites actually had anything to do with these invasions..."))
sleep(3)
printc(orange("You draw your sword towards the shadow figure, and force him out of hiding"))
sleep(3)
printc(orange("You uncloak the hood that he wears"))
sleep(3)
printc(orange("It was"))
sleep(3)
unless = "..."
for i in unless:
    print(i, end=" ")
    sleep(0.5)
printc(orange("The Old Man from the town?!?"))
sleep(3)
printc(orange("But why? Why would he do this?"))
sleep(3)
printc(orange("Find out next time in the next game, with loads of new adventures, bosses, and features for only $59.99!"))
sleep(3)
printc(green("Thanks for playing!"))
sys.exit()
