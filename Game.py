import time
import os
import random
clear = lambda: os.system('cls')
name = ''
health=10
kills=0
warriorL=False
warriorR=False
archerL=False
archerR=False
earth=False
fire=False
def Main():
    print('-------------------------------------------------------------------------------')
    print('___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('|  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('|__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print('-------------------------------------------------------------------------------')
def hp():
    global health
    global name
    print('Health: ',health,' Class: ',name)
def loading():
    for x in range (0,4):
        b = "Loading" + "." * x
        print (b, end="\r")
        time.sleep(1)
def classSelect():
    global name
    failed=False
    if failed == False:
        Main()
        role=input('Pick a class: [1] Warrior  [2] Archer [3] Summoner \n')
        try:
            rolecheck = int(role)
        except ValueError:
            rolecheck = 0
        if rolecheck == 1:
            print('You have selected Warrior',end='\r')
            name='Warrior'
            level1_W()
        elif rolecheck == 2:
            print('You have selected Archer', end='\r')
            name='Archer'
            level1_A()
        elif rolecheck == 3:
            print('You have selected Summoner', end='\r')
            name='Summoner'
            level2_S()
        elif rolecheck == 0:
            failed=True
            print('Please try again...')
            time.sleep(1)
            clear()
            classSelect()
        else:
            failed=True
            print('Please try again...')
            time.sleep(1)
            clear()
            classSelect()
def level1_W():
    global health
    global warriorL
    global warriorR
    clear()
    Main()
    hp()
    print('There are two tunnels.')
    action=input('[1] Left Tunnel [2] Right Tunnel \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        print('Please try again...')
        time.sleep(1)
        clear()
        level1_W()
    else:
        if path_c == 1:
            print('I have a bad feeling about this...')
            time.sleep(1)
            warriorL=True
            level2_W()
        elif path_c == 2:
            print('Alright here we go..')
            time.sleep(1)
            warriorR=True
            level2_W()
        else:
            print('Please try again...')
            time.sleep(1)
            clear()
            level1_W()
def level1_A():
    global health
    global archerL
    global archerR
    clear()
    Main()
    hp()
    print('There are two enemies.')
    print('Which one should we attack?')
    action=input('[1] Orge [2] Bat \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        print('Please try again...')
        time.sleep(1)
        clear()
        level1_A()
    else:
        if path_c == 1:
            print('Yes, the orge is slow. I can continue hitting him.')
            time.sleep(2)
            print('Orge has been defeated.')
            time.sleep(1)
            print('You have now recieved a Sturdy Bow')
            time.sleep(2)
            archerL=True
            level2_A()
        elif path_c == 2:
            print('Arghh, it is too fast. I need to get back.')
            time.sleep(2)
            print('The bat catches up too you, you take 3 damage.')
            time.sleep(2)
            health = health - 3
            clear()
            Main()
            hp()
            print('There are two enemies.')
            print('Which one should we attack?')
            print('[1] Orge [2] Bat')
            print('2')
            print('Arghh, it is too fast. I need to get back.')
            print('The bat catches up too you, you take 3 damage.')
            time.sleep(2)
            archerR=True
            level2_A()
        else:
            print('Please try again...')
            time.sleep(1)
            clear()
            level1_A()
def level1_S():
    global health
    global earth
    global fire
    clear()
    Main()
    hp()
    print('You are given the option to summon one elemental')
    action=input('[1] Earth Elemental [2] Fire Elemental \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level1_S()
    else:
         if path_c == 1:
            print('You have completed the contract with the Earth Elemental')
            earth=True
            level2_S()
         elif path_c == 2:
            print('You have completed the contract with the Fire Elemental')
            fire=True
            level2_S()
         else:
            print('Please try again...')
            time.sleep(1)
            clear()
            level1_S()
def level2_W():
    global health
    clear()
    Main()
    hp()
    if warriorL == True:
        print('You have found a sharp sword, this is better than your current one.')
        time.sleep(2)
        print('You take 1 damage from picking up the sword.')
        time.sleep(2)
        health = health - 1
        clear()
        level2_W2()
    elif warriorR == True:
        print('You have found a rusty sword, this is worse than your current one.')
        print('You pass it without picking it up.')
        print('You see 10 wild boars roaming the area')
        print('What do you do?')
        action=input('[1] Fight [2] Sneak Past \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_W()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                time.sleep(1)
                print('However take 4 damage in the process.')
                health = health - 4
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                print('However take 4 damage in the process.')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('Your attempt to sneak past was successful')
                time.sleep(1)
                print('The wild boars did not even notice you.')
                time.sleep(1)
                print('You pass this stage with full health.')
                time.sleep(3)
            else:
                print('Please try again...')
                time.sleep(2)
                clear()
                level2_W()
    else:
        print('WTF')
def level2_W2():
    global health
    Main()
    hp()
    print('You see 5 armed goblins walking in you direction')
    print('What do you do?')
    action=input('[1] Fight [2] Hide \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        print('Please try again...')
        time.sleep(2)
        clear()
        level2_W2()
    else:
        if path_c == 1:
            print('You successfully defeat the 5 goblins.')
            print('You did not get hit once, it must be because of the sword.')
            time.sleep(2)
        elif path_c == 2:
            print('You attempt to hide however are spotted.')
            time.sleep(2)
            print('The goblins then surrounded you.')
            time.sleep(2)
            print('You eventually defeat them all however take 2 damage in the process.')
            time.sleep(3)
            health = health - 2
            clear()
            Main()
            hp()
            print('You see 5 armed goblins walking in you direction')
            print('What do you do?')
            print('[1] Fight [2] Hide')
            print('2')
            print('You attempt to hide however are spotted.')
            print('The goblins then surrounded you.')
            print('You eventually defeat them all, however take 2 damage in the process.')
            time.sleep(5)
        else:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_W2()
def level2_A():
    global health
    clear()
    Main()
    hp()
    if archerL == True:
        print('You have set off a trap!')
        time.sleep(2)
        print('The ground beneath you will give away any second now!')
        time.sleep(2)
        print('What will you do?')
        action=input('[1] Run Away [2] Hug the wall \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_A2()
        else:
            if path_c == 1:
                print('You managed to run away somewhat safely')
                time.sleep(2)
                print('However trip and fall taking 2 damage.')
                health = health - 2
                time.sleep(2)
                clear()
                Main()
                hp()
                print('You have set off a trap!')
                print('The ground beneath you will give away any second now!')
                print('What will you do?')
                print('[1] Run Away [2] Hug the wall')
                print('1')
                print('You managed to run away somewhat safely')
                print('However trip and fall taking 2 damage.')
                time.sleep(4)
            elif path_c == 2:
                print('You hug the wall, hoping that this area is not affected by the trap.')
                time.sleep(2)
                print('The ground gives way, beneath you see spikes.')
                time.sleep(2)
                print('However you are not affected.')
                time.sleep(1)
                print('you slowly shift your way to the end of the hallway.')
                time.sleep(3)
    elif archerR == True:
        print('You see a Cursed Bow')
        time.sleep(2)
        print('You pick it up, dealing 1 curse damage over time')
        print('For 1 Turn')
        health = health - 1
        time.sleep(3)
        clear()
        level2_A3()
    else:
        print('WTF')
def level2_A2():
    global health
    Main()
    hp()
    print('You have set off a trap!')
    print('The ground beneath you will give away any second now!')
    print('What will you do?')
    action=input('[1] Run Away [2] Hug the wall \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        print('Please try again...')
        time.sleep(2)
        clear()
        level2_A2()
    else:
        if path_c == 1:
            print('You managed to run away somewhat safely')
            time.sleep(2)
            print('However trip and fall taking 2 damage.')
            health = health - 2
            time.sleep(2)
            clear()
            Main()
            hp()
            print('You have set off a trap!')
            print('The ground beneath you will give away any second now!')
            print('What will you do?')
            print('[1] Run Away [2] Hug the wall')
            print('1')
            print('You managed to run away somewhat safely')
            print('However trip and fall taking 2 damage.')
            time.sleep(4)
        elif path_c == 2:
            print('You hug the wall, hoping that this area is not affected by the trap.')
            time.sleep(2)
            print('The ground gives way, beneath you see spikes.')
            time.sleep(2)
            print('However you are not affected.')
            time.sleep(1)
            print('you slowly shift your way to the end of the hallway.')
            time.sleep(3)
        else:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_A2()
def level2_A3():
    global health
    clear()
    Main()
    hp()
    print('In the distance you see 3 guards, they seem to be guarding something.')
    action=input('[1] Fight the Guards [2] Sneak Past \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        print('Please try again...')
        time.sleep(2)
        clear()
        level2_A3()
    else:
        if path_c == 1:
            time.sleep(1)
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            time.sleep(2)
            print('However they have two archers and a warrior.')
            time.sleep(2)
            print('As you defeat one archer the other continues firing at you.')
            time.sleep(3)
            print('You take 2 damage.')
            health = health - 2
            time.sleep(2)
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            time.sleep(2)
            print('You then return fire managing to take him down.')
            time.sleep(2)
            print('However at the same time the warrior attacks you dealing 3 damage.')
            time.sleep(3)
            health = health - 3
            time.sleep(2)
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            print('You then return fire managing to take him down.')
            print('However at the same time the warrior attacks you dealing 3 damage.')
            time.sleep(3)
            print('You open the door that they were guarding.')
            time.sleep(2)
            print('Inside you see some health you pick up.')
            time.sleep(2)
            print('You gain 1 health.')
            health = health + 1
            time.sleep(2)
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            print('You then return fire managing to take him down.')
            print('However at the same time the warrior attacks you dealing 3 damage.')
            print('You open the door that they were guarding.')
            print('Inside you see some health you pick up.')
            print('You gain 1 health.')                          #2 Health
            time.sleep(3)
            print('Curse Bow inflicts 1 curse damage.')
            time.sleep(2)
            health = health - 1
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            print('You then return fire managing to take him down.')
            print('However at the same time the warrior attacks you dealing 3 damage.')
            print('You open the door that they were guarding.')
            print('Inside you see some health you pick up.')
            print('You gain 1 health.')
            print('Curse Bow inflicts 1 curse damage.')
            print('Curse Bow, damage over time effect has ended.')
            time.sleep(3)
        elif path_c == 2:
            time.sleep(1)
            clear()
            Main()
            hp()
            print('Your attempt to sneak past was successful!')
            time.sleep(2)
            print('The guards did not notice you.')
            time.sleep(3)
        else:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_A3()
def level2_S():
    global health
    clear()
    Main()
    hp()
    if earth == True:
        print('You see a master wizzard ahead')
        time.sleep(2)
        print('He seems to be holding a legendary staff')
        time.sleep(2)
        print('What do you do?')
        action=input('[1] Fight [2] Sneak Past \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_S()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                time.sleep(1)
                print('However take 4 damage in the process.')
                health = health - 4
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                print('However take 4 damage in the process.')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('Your attempt to sneak past was successful')
                time.sleep(1)
                print('The wild boars did not even notice you.')
                time.sleep(1)
                print('You pass this stage with full health.')
                time.sleep(3)
            else:
                print('Please try again...')
                time.sleep(2)
                clear()
                level2_W()
        action
        clear()
        level2_W2()
    elif warriorR == True:
        print('You have found a rusty sword, this is worse than your current one.')
        print('You pass it without picking it up.')
        print('You see 10 wild boars roaming the area')
        print('What do you do?')
        action=input('[1] Fight [2] Sneak Past \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            print('Please try again...')
            time.sleep(2)
            clear()
            level2_W()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                time.sleep(1)
                print('However take 4 damage in the process.')
                health = health - 4
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                print('However take 4 damage in the process.')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('Your attempt to sneak past was successful')
                time.sleep(1)
                print('The wild boars did not even notice you.')
                time.sleep(1)
                print('You pass this stage with full health.')
                time.sleep(3)
            else:
                print('Please try again...')
                time.sleep(2)
                clear()
                level2_W()
    else:
        print('WTF')

classSelect()
