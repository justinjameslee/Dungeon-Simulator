import time
import os
import random
import curses
import msvcrt
from msvcrt import getch
clear = lambda: os.system('cls')
name = ''
summon=''
mode=''
health=10
Check=False
Dialong=True
warriorL=False
warriorR=False
warriorRL=False
warriorRR=False
warriorLL=False
warriorLR=False
warriorLLL=False
warriorLLR=False
warriorLRL=False
warriorLRR=False
archerL=False
archerR=False
earth=False
fire=False
def Main():
    global mode
    print('-------------------------------------------------------------------------------')
    print('___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('|  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('|__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print("Playthrough Mode:", mode, '\n')
    print('-------------------------------------------------------------------------------')
def Main2():
    print('-------------------------------------------------------------------------------')
    print('___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('|  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('|__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print('[O] Original Dialog [Q] Quick Dialog \n')
    print('-------------------------------------------------------------------------------')
def hp():
    global health
    global name
    print('Health: ',health,' Class: ',name)
def hp2():
    global health
    global name
    global summon
    print('Health: ',health,' Class: ',name,' Elemental: ',summon)
def loading():
    os.system("mode con: cols=41 lines=7")
    print('----------------------------------------')
    print('  _    ____ ____ ___  _ _  _ ____')
    print('  |    |  | |__| |  \ | |\ | | __')
    print('  |___ |__| |  | |__/ | | \| |__] \n')
    print('----------------------------------------')
    time.sleep(1)
    clear()
    for x in (1,2):
        print('----------------------------------------')
        print('  _    ____ ____ ___  _ _  _ ____')
        print('  |    |  | |__| |  \ | |\ | | __')
        print('  |___ |__| |  | |__/ | | \| |__] . \n')
        print('----------------------------------------')
        time.sleep(1)
        clear()
        print('----------------------------------------')
        print('  _    ____ ____ ___  _ _  _ ____')
        print('  |    |  | |__| |  \ | |\ | | __')
        print('  |___ |__| |  | |__/ | | \| |__] . . \n')
        print('----------------------------------------')
        time.sleep(1)
        clear()
        print('----------------------------------------')
        print('  _    ____ ____ ___  _ _  _ ____')
        print('  |    |  | |__| |  \ | |\ | | __')
        print('  |___ |__| |  | |__/ | | \| |__] . . .\n')
        print('----------------------------------------')
        time.sleep(1)
        clear()
def classSelect():
    os.system("mode con: cols=80 lines=30")
    global mode
    global Check
    global Dialog
    global health
    global name
    global summon
    global warriorL
    global warriorR
    global warriorRL
    global warriorRR
    global warriorLL
    global warriorLR
    global archerL
    global archerR
    global earth
    global fire
    name = ''
    summon=''
    mode=''
    health=10
    Check=False
    Dialong=True
    warriorL=False
    warriorR=False
    warriorRL=False
    warriorRR=False
    warriorLL=False
    warriorLR=False
    warriorLLL=False
    warriorLLR=False
    warriorLRL=False
    warriorLRR=False
    archerL=False
    archerR=False
    earth=False
    fire=False
    clear()
    Main2()
    while True:
        key = ord(getch())
        if key == 111:
            Dialog = True
            mode='Original Dialog'
            break
        elif key == 113:
            Dialog = False
            mode='Quick Dialog'
            break
        else:
            if Check == False:
                print("Please Select [O] or [Q] to Continue. ")
                Check = True
            elif Check == True:
                pass
            continue
    clear()
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
        level1_S()
    elif rolecheck == 0:
        clear()
        classSelect()
    else:
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
        clear()
        level1_W()
    else:
        if path_c == 1:
            print('I have a bad feeling about this...')
            time.sleep(1)
            while True:
                clear()
                Main()
                hp()
                print('There are two tunnels.')
                print('[1] Left Tunnel [2] Right Tunnel')
                print('1')
                print('I have a bad feeling about this...')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    warriorL=True
                    level2_W()
                else:
                    continue
        elif path_c == 2:
            print('Alright here we go..')
            time.sleep(1)
            while True:
                clear()
                Main()
                hp()
                print('There are two tunnels.')
                print('[1] Left Tunnel [2] Right Tunnel')
                print('2')
                print('Alright here we go..')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    warriorR=True
                    level2_W()
                else:
                    continue
        else:
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
        clear()
        level1_A()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('Yes, the orge is slow. I can continue hitting him.')
            time.sleep(2)
            print('Orge has been defeated.')
            time.sleep(1)
            print('You have now recieved a Sturdy Bow')
            time.sleep(2)
            while True:
                clear()
                Main()
                hp()
                print('Yes, the orge is slow. I can continue hitting him.')
                print('Orge has been defeated.')
                print('You have now recieved a Sturdy Bow')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    archerL=True
                    level2_A()
                else:
                    continue
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('Arghh, it is too fast. I need to get back.')
            time.sleep(2)
            print('The bat catches up too you, you take 3 damage.')
            time.sleep(2)
            health = health - 3
            clear()
            Main()
            hp()
            print('Arghh, it is too fast. I need to get back.')
            print('The bat catches up too you, you take 3 damage.')
            time.sleep(2)
            while True:
                clear()
                Main()
                hp()
                print('Arghh, it is too fast. I need to get back.')
                print('The bat catches up too you, you take 3 damage.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    archerR=True
                    level2_A()
                else:
                    continue
        else:
            clear()
            level1_A()
def level1_S():
    global health
    global earth
    global fire
    global summon
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
            time.sleep(2)
            while True:
                clear()
                Main()
                hp()
                print('You are given the option to summon one elemental')
                print('[1] Earth Elemental [2] Fire Elemental')
                print('1')
                print('You have completed the contract with the Earth Elemental')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    earth=True
                    summon='Earth Elemental'
                    level2_S()
                else:
                    continue

         elif path_c == 2:
            print('You have completed the contract with the Fire Elemental')
            time.sleep(2)
            while True:
                clear()
                Main()
                hp()
                print('You are given the option to summon one elemental')
                print('[1] Earth Elemental [2] Fire Elemental')
                print('2')
                print('You have completed the contract with the Fire Elemental')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    fire=True
                    summon='Fire Elemental'
                    level2_S()
                else:
                    continue
         else:
            clear()
            level1_S()
def level2_W():
    global health
    global warriorRL
    global warriorRR
    clear()
    Main()
    hp()
    if warriorL == True:
        print('You have found a sharp sword, this is better than your current one.')
        time.sleep(2)
        print('You take 1 damage from picking up the sword.')
        health = health - 1
        time.sleep(2)
        print('You also find some rope next to the sword.')
        time.sleep(3)
        while True:
            clear()
            Main()
            hp()
            print('You have found a sharp sword, this is better than your current one.')
            print('You take 1 damage from picking up the sword.')
            print('You also find some rope next to the sword.')
            action=input('[Enter/Return] to Continue \n')
            if action == "":
                clear()
                level2_W2()
            else:
                continue

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
                while True:
                    clear()
                    Main()
                    hp()
                    print('You successfully defeat the 10 wild boars.')
                    print('However take 4 damage in the process.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        warriorRL=True
                        level3_WR1()
                    else:
                        continue

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
                while True:
                    clear()
                    Main()
                    hp()
                    print('Your attempt to sneak past was successful')
                    print('The wild boars did not even notice you.')
                    print('You pass this stage with full health.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        warriorRR=True
                        level3_WR1()
                    else:
                        continue

            else:
                clear()
                level2_W()
    else:
        print('WTF')
def level2_W2():
    global health
    global warriorLL
    global warriorLR
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
        clear()
        level2_W2()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('You successfully defeat the 5 goblins.')
            time.sleep(2)
            print('You did not get hit once, it must be because of the sword.')
            time.sleep(3)
            while True:
                clear()
                Main()
                hp()
                print('You successfully defeat the 5 goblins.')
                print('You did not get hit once, it must be because of the sword.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    warriorLL=True
                    level3_WL1()
                else:
                    continue

        elif path_c == 2:
            clear()
            Main()
            hp()
            print('You attempt to hide however are spotted.')
            time.sleep(2)
            print('The goblins then surrounded you.')
            time.sleep(2)
            print('You eventually defeat them all, however take 2 damage in the process.')
            time.sleep(3)
            health = health - 2
            clear()
            Main()
            hp()
            print('You attempt to hide however are spotted.')
            print('The goblins then surrounded you.')
            print('You eventually defeat them all, however take 2 damage in the process.')
            time.sleep(5)
            while True:
                clear()
                Main()
                hp()
                print('You attempt to hide however are spotted.')
                print('The goblins then surrounded you.')
                print('You eventually defeat them all, however take 2 damage in the process.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    warriorLR=True
                    level3_WL1()
                else:
                    continue

        else:
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
            clear()
            level2_A2()
        else:
            if path_c == 1:
                clear()
                Main()
                hp()
                print('You managed to run away somewhat safely')
                time.sleep(2)
                print('However trip and fall taking 2 damage.')
                health = health - 2
                time.sleep(2)
                clear()
                Main()
                hp()
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
            clear()
            level2_A3()
def level2_S():
    global health
    clear()
    Main()
    hp2()
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
            clear()
            level2_S2()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You start engaging in combat')
                time.sleep(2)
                print('You send your Earth Elemental ahead to attack.')
                time.sleep(2)
                print('The Master Wizzard casts a fireball and shoots it at you.')
                time.sleep(2)
                print('The Earth Elemental shields you from damage.')
                time.sleep(2)
                print('You then charge together with your Earth Elemental.')
                time.sleep(2)
                print('You catch the Master Wizzard off guard.')
                time.sleep(2)
                print('The Master Wizzard is defeated.')
                time.sleep(2)
                print('Legendary Staff Acquired!')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                time.sleep(2)
                print('The Master Wizzard notices you and starts casting fireball.')
                time.sleep(2)
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                time.sleep(3)
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                time.sleep(2)
                health = health - 5
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                print('The Master Wizzard notices you and starts casting fireball.')
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                time.sleep(2)
                print('You then attack together with your Earth Elemental.')
                time.sleep(2)
                print('You finally defeat the Master Wizzard however the legendary staff...')
                time.sleep(2)
                print('Was destroyed in the midst.')
                time.sleep(3)
            else:
                clear()
                level2_W()
    elif fire == True:
        print('Up ahead you see a rouge Water Elemental.')
        time.sleep(2)
        print('It seems to be blocking the exit')
        time.sleep(2)
        print('What do you do?')
        time.sleep(2)
        action=input('[1] Fight Together [2] Fight Alone \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level2_S3()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You close in on the Water Elemental together.')
                time.sleep(2)
                print("However your Fire Elemental can't damage the Water Elemental!")
                time.sleep(2)
                print('The Water Elemental sees an opportunity to attack!')
                time.sleep(2)
                print('The Water Elemental attacks you both inflicting 4 damage.')
                time.sleep(2)
                health = health - 4
                print('Your Fire Elemental is heavily wounded, you must now fight alone.')
                time.sleep(2)
                clear()
                Main()
                hp2()
                print('You close in on the Water Elemental together.')
                print("However your Fire Elemental can't damage the Water Elemental!")
                print('The Water Elemental sees an opportunity to attack!')
                print('The Water Elemental attacks you both inflicting 4 damage.')
                print('Your Fire Elemental is heavily wounded, you must now fight alone.')
                time.sleep(3)
                print('You eventually defeat the Water Elemental however it leaves you wounded.')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You draw your sword preparing for battle.')
                time.sleep(2)
                print('Your Fire Elemental would not be very useful in this fight.')
                time.sleep(2)
                print('You attack, catching the Water Elemental off guard killing him instantly.')
                time.sleep(3)
            else:
                clear()
                level2_W()
    else:
        print('WTF')
def level2_S2():
    global health
    clear()
    Main()
    hp2()
    if earth == True:
        print('You see a master wizzard ahead')
        print('He seems to be holding a legendary staff')
        print('What do you do?')
        action=input('[1] Fight [2] Sneak Past \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level2_S2()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You start engaging in combat')
                time.sleep(2)
                print('You send your Earth Elemental ahead to attack.')
                time.sleep(2)
                print('The Master Wizzard casts a fireball and shoots it at you.')
                time.sleep(2)
                print('The Earth Elemental shields you from damage.')
                time.sleep(2)
                print('You then charge together with your Earth Elemental.')
                time.sleep(2)
                print('You catch the Master Wizzard off guard.')
                time.sleep(2)
                print('The Master Wizzard is defeated.')
                time.sleep(2)
                print('Legendary Staff Acquired!')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                time.sleep(2)
                print('The Master Wizzard notices you and starts casting fireball.')
                time.sleep(2)
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                time.sleep(3)
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                time.sleep(2)
                health = health - 5
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                print('The Master Wizzard notices you and starts casting fireball.')
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                time.sleep(2)
                print('You then attack together with your Earth Elemental.')
                time.sleep(2)
                print('You finally defeat the Master Wizzard however the legendary staff...')
                time.sleep(2)
                print('Was destroyed in the midst.')
                time.sleep(3)
            else:
                clear()
                level2_S2()
def level2_S3():
    global health
    clear()
    Main()
    hp2()
    print('Up ahead you see a rouge Water Elemental.')
    print('It seems to be blocking the exit')
    print('What do you do?')
    action=input('[1] Fight Together [2] Fight Alone \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level2_S3()
    else:
        if path_c == 1:
            time.sleep(1)
            clear()
            Main()
            hp2()
            print('You close in on the Water Elemental together.')
            time.sleep(2)
            print("However your Fire Elemental can't damage the Water Elemental!")
            time.sleep(2)
            print('The Water Elemental sees an opportunity to attack!')
            time.sleep(2)
            print('The Water Elemental attacks you both inflicting 4 damage.')
            time.sleep(2)
            health = health - 4
            print('Your Fire Elemental is heavily wounded, you must now fight alone.')
            time.sleep(2)
            clear()
            Main()
            hp2()
            print('You close in on the Water Elemental together.')
            print("However your Fire Elemental can't damage the Water Elemental!")
            print('The Water Elemental sees an opportunity to attack!')
            print('The Water Elemental attacks you both inflicting 4 damage.')
            print('Your Fire Elemental is heavily wounded, you must now fight alone.')
            time.sleep(3)
            print('You eventually defeat the Water Elemental however it leaves you wounded.')
            time.sleep(3)
        elif path_c == 2:
            time.sleep(1)
            clear()
            Main()
            hp2()
            print('You draw your sword preparing for battle.')
            time.sleep(2)
            print('Your Fire Elemental would not be very useful in this fight.')
            time.sleep(2)
            print('You attack, catching the Water Elemental off guard killing him instantly.')
            time.sleep(3)
        else:
            clear()
            level2_S3()
def level3_WL1():
    global health
    clear()
    Main()
    hp()
    if warriorLL == True:
        print('You see a ledge up ahead.')
        time.sleep(2)
        print('You slowly approach it and lean over the edge.')
        time.sleep(2)
        print("It's pitch black...")
        time.sleep(2)
        print('What do you do?')
        action=input('[1] Climb down [2] Find another route.\n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level3_WL1()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You proceed to use the rope to climb down the ledge.')
                time.sleep(2)
                print('On the way down you notice that the area below you is getting brighter.')
                time.sleep(2)
                print('You then touch down on the ground, and around you are bright torches.')
                time.sleep(2)
                print('You see one two hallways ahead of you...')
                time.sleep(3)
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                time.sleep(2)
                print('You suddenly spot a Legendary Eagle Master.')
                time.sleep(3)
                print('He notices you insantly and begins to ready himself for battle.')
                time.sleep(3)
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                time.sleep(3)
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                time.sleep(4)
                print('The 3 arrows that hit inflict 6 damage.')
                time.sleep(3)
                health = health - 6
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                print('You suddenly spot a Legendary Eagle Master.')
                print('He notices you insantly and begins to ready himself for battle.')
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                print('The 3 arrows that hit inflict 6 damage.')
                print('You then compose yourself readying yourself for the next blow.')
                time.sleep(3)
                print('The Legendary Eagle Master catches up too you starts swinging his sword.')
                time.sleep(3)
                print('You block with your Sharp Sword and swing at him with full force.')
                time.sleep(3)
                print('The Legendary Eagle Master blocks with ease and swings back.')
                time.sleep(3)
                print('His sword cuts into your flesh causing a deep wound.')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                print('You suddenly spot a Legendary Eagle Master.')
                print('He notices you insantly and begins to ready himself for battle.')
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                print('The 3 arrows that hit inflict 6 damage.')
                print('You then compose yourself readying yourself for the next blow.')
                print('The Legendary Eagle Master catches up too you starts swinging his sword.')
                print('You block with your Sharp Sword and swing at him with full force.')
                print('The Legendary Eagle Master blocks with ease and swings back.')
                print('His sword cuts into your flesh causing a deep wound.')
                print('You begin to lose consciousness..')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                print('You suddenly spot a Legendary Eagle Master.')
                print('He notices you insantly and begins to ready himself for battle.')
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                print('The 3 arrows that hit inflict 6 damage.')
                print('You then compose yourself readying yourself for the next blow.')
                print('The Legendary Eagle Master catches up too you starts swinging his sword.')
                print('You block with your Sharp Sword and swing at him with full force.')
                print('The Legendary Eagle Master blocks with ease and swings back.')
                print('His sword cuts into your flesh causing a deep wound.')
                print('You begin to lose consciousness..')
                print('You then collapse.')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                print('You suddenly spot a Legendary Eagle Master.')
                print('He notices you insantly and begins to ready himself for battle.')
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                print('The 3 arrows that hit inflict 6 damage.')
                print('You then compose yourself readying yourself for the next blow.')
                print('The Legendary Eagle Master catches up too you starts swinging his sword.')
                print('You block with your Sharp Sword and swing at him with full force.')
                print('The Legendary Eagle Master blocks with ease and swings back.')
                print('His sword cuts into your flesh causing a deep wound.')
                print('You begin to lose consciousness..')
                print('You then collapse.')
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WLL()
            else:
                clear()
                level3_WL1()
    elif warriorLR == True:
        print('At your left you spot a Treasure Chest.')
        time.sleep(2)
        print('However around it are many spike traps.')
        time.sleep(2)
        print('But on the right you see a Skeleton Warrior.')
        time.sleep(2)
        print('He seems...')
        time.sleep(3)
        clear()
        Main()
        hp()
        print('At your left you spot a Treasure Chest.')
        print('However around it are many spike traps.')
        print('But on the right you see a Skeleton Warrior.')
        print('He seems to be holding a Ring?')
        time.sleep(2)
        print("Yes. It's a Ring, a gold one.")
        print('What do you do?')
        action=input('[1] Treasure Chest [2] Skeleton Warrior \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level3_WL1()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You turn left heading towards the Treasure Chest.')
                time.sleep(2)
                print('As you get closer you notice that the lighting had gotten darker.')
                time.sleep(2)
                print('Then without realising you trigger a trip wire.')
                time.sleep(2)
                print('Suddenly the ground below you disappears and you fall into spikes.')
                time.sleep(2)
                health = 0
                clear()
                Main()
                hp()
                print('You turn left heading towards the Treasure Chest.')
                print('As you get closer you notice that the lighting had gotten darker.')
                print('Then without realising you trigger a trip wire.')
                print('Suddenly the ground below you disappears and you fall into spikes.')
                time.sleep(2)
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WLR()
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You turn right heading towards the Skeleton Warrior.')
                time.sleep(2)
                print('As you get closer the Skeleton Warrior notices you.')
                time.sleep(2)
                print('You both ready yourselves for battle.')
                time.sleep(2)
                print('You thrust with your Sharp Sword.')
                time.sleep(2)
                print('It hits his left leg disconnecting it from his main body.')
                time.sleep(3)
                print('As he falls forward onto the ground he swings wildly.')
                time.sleep(3)
                print('The Skeleton Warrior manages to cut your leg inflicting 3 damage.')
                time.sleep(3)
                health = health - 3
                clear()
                Main()
                hp()
                print('You turn right heading towards the Skeleton Warrior.')
                print('As you get closer the Skeleton Warrior notices you.')
                print('You both ready yourselves for battle.')
                print('You thrust with your Sharp Sword.')
                print('It hits his left leg disconnecting it from his main body.')
                print('As he falls forward onto the ground he swings wildly.')
                print('The Skeleton Warrior manages to cut your leg inflicting 3 damage.')
                print('You then slice across disconnecting the Skeleton Head.')
                time.sleep(3)
                print('In his left palm you see the gold ring.')
                time.sleep(2)
                print("You pick it up, on the ring it says: 'Legendary Eagle Master'")
                time.sleep(3)
                print('What could this mean?')
                time.sleep(1)
                while True:
                    clear()
                    Main()
                    hp()
                    print('You turn right heading towards the Skeleton Warrior.')
                    print('As you get closer the Skeleton Warrior notices you.')
                    print('You both ready yourselves for battle.')
                    print('You thrust with your Sharp Sword.')
                    print('It hits his left leg disconnecting it from his main body.')
                    print('As he falls forward onto the ground he swings wildly.')
                    print('The Skeleton Warrior manages to cut your leg inflicting 3 damage.')
                    print('You then slice across disconnecting the Skeleton Head.')
                    print('In his left palm you see the gold ring.')
                    print("You pick it up, on the ring it says: 'Legendary Eagle Master'")
                    print('What could this mean?')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('yay')
                        time.sleep(2)
                    else:
                        continue

            else:
                clear()
                level3_WL1()
    else:
        print('WTF')
def level3_WLL():
    clear()
    Main()
    hp()
    print('As you begin look around for another passageway..')
    print('You suddenly spot a Legendary Eagle Master.')
    print('He notices you insantly and begins to ready himself for battle.')
    print('You get caught off guard and proceed to retreat back to ready yourself.')
    print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
    print('The 3 arrows that hit inflict 6 damage.')
    print('You then compose yourself readying yourself for the next blow.')
    print('The Legendary Eagle Master catches up too you starts swinging his sword.')
    print('You block with your Sharp Sword and swing at him with full force.')
    print('The Legendary Eagle Master blocks with ease and swings back.')
    print('His sword cuts into your flesh causing a deep wound.')
    print('You begin to lose consciousness..')
    print('You then collapse.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WLL()
def level3_WLR():
    clear()
    Main()
    hp()
    print('You turn left heading towards the Treasure Chest.')
    print('As you get closer you notice that the lighting had gotten darker.')
    print('Then without realising you trigger a trip wire.')
    print('Suddenly the ground below you disappears and you fall into spikes.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WLR()
def level3_WR1():
    global health
    clear()
    Main()
    hp()
    if warriorRL == True:
        print('You see a door ahead...')
        time.sleep(2)
        print('However there seems to be 10 guards in front of it.')
        time.sleep(2)
        print('What do you do?')
        time.sleep(1)
        action=input('[1] Fight [2] Sneak Past\n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level3_WR1()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('With the sword in your hand, you start attacking.')
                time.sleep(2)
                print('You take down 3, this is looking good.')
                time.sleep(2)
                print('However from the door appears a Legendary Eagle Master.')
                time.sleep(3)
                print('The rest of the guardsmen are fueled with confidence.')
                time.sleep(2)
                print('They all start charging, you try to parry them away..')
                time.sleep(2)
                print('They eventually overwhelm you.')
                time.sleep(2)
                print('They inflict 6 damage.')
                health = health - 6
                time.sleep(1)
                clear()
                Main()
                hp()
                print('With the sword in your hand, you start attacking.')
                print('You take down 3, this is looking good.')
                print('However from the door appears a Legendary Eagle Master.')
                print('The rest of the guardsmen are fueled with confidence.')
                print('They all start charging, you try to parry them away..')
                print('They eventually overwhelm you.')
                print('They inflict 6 damage.')
                time.sleep(2)
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WRL()
            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You plan out your route.')
                time.sleep(2)
                print("You see 4 Archers and 6 Warriors.")
                time.sleep(2)
                print('You follow the right wall, however half-way through..')
                time.sleep(3)
                print('An Archer spots you, he shouts out to the other guards.')
                time.sleep(2)
                print('You start running. The archers fire at you, one arrow hits your back, the other hits your Legendary Eagle Master.')
                time.sleep(4)
                print("However you make it to the exit, they won't be able to follow you now.")
                time.sleep(3)
                print('In total they dealt 4 damage.')
                time.sleep(2)
                health = health - 4
                clear()
                Main()
                hp()
                print('You plan out your route.')
                print("You see 4 Archers and 6 Warriors.")
                print('You follow the right wall, however half-way through..')
                print('An Archer spots you, he shouts out to the other guards.')
                print('You start running. The archers fire at you, one arrow hits your back, the other hits your leg.')
                print("However you make it to the exit, they won't be able to follow you now.")
                print('In total they dealt 4 damage.')
                time.sleep(3)
            else:
                clear()
                level3_WR1()
    elif warriorRR == True:
        print('Up ahead you see an old witch.')
        time.sleep(2)
        print('She seems to be making Health Potions.')
        time.sleep(2)
        print('Behind her are a stack off 3 Health Potions.')
        time.sleep(2)
        print('They seem to recover 1 Health per use.')
        time.sleep(2)
        print('What do you do?')
        action=input('[1] Fight the Witch and get 3 [2] Buy 1 with your Sword\n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level3_WR1()
        else:
            if path_c == 1:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                time.sleep(2)
                print('The old witch notices you and she quickly retreats back into her home.')
                time.sleep(3)
                print('You follow her, however...')
                time.sleep(2)
                print('She had actually laid traps around the area, and you have set them off.')
                time.sleep(3)
                print('They deal 1 poison damage.')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                time.sleep(3)
                print('But she splashes a potion onto you that makes you fall asleep.')
                time.sleep(3)
                print('You start taking damage...')
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                print('But she splashes a potion onto you that makes you fall asleep.')
                print('You start taking damage...')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                print('But she splashes a potion onto you that makes you fall asleep.')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                print('But she splashes a potion onto you that makes you fall asleep.')
                print('You start taking damage...')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                print('But she splashes a potion onto you that makes you fall asleep.')
                print('You start taking damage...')
                time.sleep(3)
                health = health - 1
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                print('The old witch notices you and she quickly retreats back into her home.')
                print('You follow her, however...')
                print('She had actually laid traps around the area, and you have set them off.')
                print('They deal 1 poison damage.')
                print('You then enter her home hoping to end this quickly.')
                print('But she splashes a potion onto you that makes you fall asleep.')
                print('You start taking damage...')
                time.sleep(4)
                clear()
                Main()
                hp()
                print("You wake up to find that you've been stripped of all your belongings.")
                time.sleep(2)
                print("She has also taken your Sword.")
                time.sleep(2)
                print("You walk back the way you came until you see the Witch's home again.")
                time.sleep(4)
                print('You begin knocking on the door asking for your items back.')
                time.sleep(3)
                print('In return she stabs you through the door with your very own Sword.')
                time.sleep(3)
                print('You begin to lose consciousness and collapse.')
                health = 0
                clear()
                Main()
                hp()
                print("You wake up to find that you've been stripped of all your belongings.")
                print("She has also taken your Sharp Sword.")
                print("You walk back the way you came until you see the Witch's home again.")
                print('You begin knocking on the door asking for your items back.')
                print('In return she stabs you through the door with your very own Sharp Sword.')
                print('You begin to lose consciousness and collapse.')
                time.sleep(2)
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WRR()

            elif path_c == 2:
                time.sleep(1)
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                time.sleep(2)
                print('You offer your Sword and in return she gives you a health potion.')
                time.sleep(2)
                health = health + 1
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                print('You offer your Sword and in return she gives you a health potion.')
                time.sleep(3)
                print('She then beckons you to come to her home.')
                time.sleep(2)
                print('You comply and follow her.')
                time.sleep(2)
                print('Inside her home she offers you more health potions.')
                time.sleep(3)
                print('You now feel overcharged.')
                health = 15
                time.sleep(2)
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                print('You offer your Sword and in return she gives you a health potion.')
                print('She then beckons you to come to her home.')
                print('You comply and follow her.')
                print('Inside her home she offers you more health potions.')
                print('You now feel overcharged.')
                time.sleep(4)
            else:
                clear()
                level3_WR1()
    else:
        print('WTF')
def level3_WRL():
    clear()
    Main()
    hp()
    print('With the sharp sword in your hand, you start attacking.')
    print('You take down 3, this is looking good.')
    print('However from the door appears a Legendary Eagle Master.')
    print('The rest of the guardsmen are fueled with confidence.')
    print('They all start charging, you try to parry them away..')
    print('They eventually overwhelm you.')
    print('They inflict 6 damage.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WRL()
def level3_WRR():
    clear()
    Main()
    hp()
    print("You wake up to find that you've been stripped off all your belongings.")
    print("She has also taken your Sharp Sword.")
    print("You walk back the way you came until you see the Witch's home again.")
    print('You begin knocking on the door asking for your items back.')
    print('In return she stabs you through the door with your very own Sharp Sword.')
    print('You begin to lose consciousness and collapse.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WRR()
classSelect()
