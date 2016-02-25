import time
import os
import msvcrt
import pyglet
import sys
from msvcrt import getch
clear = lambda: os.system('cls')
name = ''
summon=''
mode=''
Title="Dungeon Simulator"
gold=0
health=10
Check=False
Music=False
Dialog=1
warriorL=False
warriorR=False
warriorRL=False
warriorRR=False
warriorLL=False
warriorLR=False
warriorLLL=False
warriorLRR=False
warriorRLR=False
warriorRRR=False
warriorLRRL=False
archerL=False
archerR=False
earth=False
fire=False
player = pyglet.media.Player()
music = pyglet.media.load('Epic.mp3')
os.system("title "+Title)
def Main():
    global mode
    print('-----------------------------------------------------------------------------------------')
    print('      ___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('      |  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('      |__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print("      Playthrough Mode:", mode, '\n')
    print('-----------------------------------------------------------------------------------------')
def Main2():
    print('-----------------------------------------------------------------------------------------')
    print('      ___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('      |  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('      |__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print('      Dialog Speed: [1] Original Dialog [2] Quick Dialog [3] Instant Dialog \n')
    print('-----------------------------------------------------------------------------------------')
def Main3():
    global mode
    print('-----------------------------------------------------------------------------------------')
    print('      ___  _  _ _  _ ____ ____ ____ _  _    ____ _ _  _ _  _ _    ____ ___ ____ ____')
    print('      |  \ |  | |\ | | __ |___ |  | |\ |    [__  | |\/| |  | |    |__|  |  |  | |__/')
    print('      |__/ |__| | \| |__] |___ |__| | \|    ___] | |  | |__| |___ |  |  |  |__| |  \ \n')
    print("      Playthrough Mode:", mode, '\n')
    print('      Options: [Q] Quit [P] Play Music [S] Stop Music [B] Back to Dialog Speed \n')
    print('-----------------------------------------------------------------------------------------')
def hp():
    global health
    global name
    global gold
    print('Health: ',health,' Gold: ',gold,' Class: ',name)
def hp2():
    global health
    global name
    global summon
    global gold
    print('Health: ',health,' Gold: ',gold,' Class: ',name,' Elemental: ',summon)
def dialog():
    global Dialog
    if Dialog == 1:
        time.sleep(2.5)
    elif Dialog == 2:
        time.sleep(1)
    elif Dialog == 3:
        pass
    else:
        print('Error!')

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
    os.system("mode con: cols=90 lines=20")
    global gold
    global player
    global Music
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
    global warriorLLL
    global warriorLRR
    global warriorRLR
    global warriorRRR
    global warriorLRRL
    global archerL
    global archerR
    global earth
    global fire
    name = ''
    summon=''
    mode=''
    gold=0
    health=10
    Check=False
    Dialog=0
    warriorL=False
    warriorR=False
    warriorRL=False
    warriorRR=False
    warriorLL=False
    warriorLR=False
    warriorLLL=False
    warriorLRR=False
    warriorRLR=False
    warriorRRR=False
    warriorLRRL=False
    archerL=False
    archerR=False
    earth=False
    fire=False
    if Music == False:
        player.queue(music)
        player.play()
        Music = True
    elif Music == True:
        pass
    clear()
    Main2()
    while True:
        key = ord(getch())
        if key == 49:
            Dialog = 1
            mode='Original Dialog'
            break
        elif key == 50:
            Dialog = 2
            mode='Quick Dialog'
            break
        elif key == 51:
            Dialog = 3
            mode='Instant Dialog'
            break
        else:
            if Check == False:
                print("Please Select [1] or [2] or [3] to Continue. ")
                Check = True
            elif Check == True:
                pass
            continue
    classSelect2()
def classSelect2():
    os.system("mode con: cols=90 lines=35")
    global gold
    global player
    global Music
    global health
    global name
    global summon
    global warriorL
    global warriorR
    global warriorRL
    global warriorRR
    global warriorLL
    global warriorLR
    global warriorLLL
    global warriorLRR
    global warriorRLR
    global warriorRRR
    global warriorLRRL
    global archerL
    global archerR
    global earth
    global fire
    name = ''
    summon=''
    gold=0
    health=10
    warriorL=False
    warriorR=False
    warriorRL=False
    warriorRR=False
    warriorLL=False
    warriorLR=False
    warriorLLL=False
    warriorLRR=False
    warriorRLR=False
    warriorRRR=False
    warriorLRRL=False
    archerL=False
    archerR=False
    earth=False
    fire=False
    while True:
        clear()
        Main3()
        role=input('Pick a class: [1] Warrior  [2] Archer [3] Summoner \n')
        if role == '1':
            print('You have selected Warrior',end='\r')
            name='Warrior'
            level1_W()
        elif role == '2':
            print('You have selected Archer', end='\r')
            name='Archer'
            level1_A()
        elif role == '3':
            print('You have selected Summoner', end='\r')
            name='Summoner'
            level1_S()
        elif role == 'Q' or role == 'q':
            quit()
        elif role == 'B' or role == 'b':
            classSelect()
        elif role == 'P' or role =='p':
            songR()
        elif role == 'S' or role == 's':
            songS()
        else:
            continue
def songR():
    global Music
    if Music == True:
        player.pause()
        player.play()
    elif Music == False:
        player.pause()
        player.play()
def songS():
    global Music
    if Music == True:
        player.pause()
    elif Music == False:
        pass
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
            dialog()
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
            dialog()
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
            print('With my ranged bow I can continue hitting this Orge!')
            dialog()
            print("He can't catch up to me because of his speed.")
            dialog()
            print('The Orge has been defeated!')
            dialog()
            print('You have now recieved a Sturdy Bow.')
            dialog()
            while True:
                clear()
                Main()
                hp()
                print('With my ranged bow I can continue hitting this Orge!')
                print("He can't catch up to me because of his speed.")
                print('The Orge has been defeated!')
                print('You have now recieved a Sturdy Bow.')
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
            dialog()
            print('The bat catches up too you, you take 3 damage.')
            dialog()
            health = health - 3
            clear()
            Main()
            hp()
            print('Arghh, it is too fast. I need to get back.')
            print('The bat catches up too you, you take 3 damage.')
            dialog()
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
            dialog()
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
            dialog()
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
    global gold
    global warriorRL
    global warriorRR
    clear()
    Main()
    hp()
    if warriorL == True:
        print('You have found a sharp sword, this is better than your current one.')
        dialog()
        print('You take 1 damage from picking up the sword.')
        health = health - 1
        dialog()
        while True:
            clear()
            Main()
            hp()
            print('You have found a sharp sword, this is better than your current one.')
            print('You take 1 damage from picking up the sword.')
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
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                dialog()
                print('However take 4 damage in the process.')
                health = health - 4
                dialog()
                print('You gain 10 gold.')
                gold = gold + 10
                dialog()
                clear()
                Main()
                hp()
                print('You successfully defeat the 10 wild boars.')
                print('However take 4 damage in the process.')
                print('You recieve 10 gold.')
                dialog()
                while True:
                    clear()
                    Main()
                    hp()
                    print('You successfully defeat the 10 wild boars.')
                    print('However take 4 damage in the process.')
                    print('You recieve 10 gold.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        warriorRL=True
                        level3_WR1()
                    else:
                        continue

            elif path_c == 2:
                clear()
                Main()
                hp()
                print('Your attempt to sneak past was successful')
                dialog()
                print('The wild boars did not notice you.')
                dialog()
                print('You pass this stage with full health.')
                dialog()
                while True:
                    clear()
                    Main()
                    hp()
                    print('Your attempt to sneak past was successful')
                    print('The wild boars did not notice you.')
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
    global gold
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
            dialog()
            print('You did not get hit once, it must be because of the Sharp Sword.')
            dialog()
            print('One of the goblins was carrying some rope.')
            dialog()
            print('You proceed to pick it up and attach it to your belt.')
            dialog()
            print('You recieve 5 gold.')
            gold = gold + 5
            dialog()
            while True:
                clear()
                Main()
                hp()
                print('You successfully defeat the 5 goblins.')
                print('You did not get hit once, it must be because of the Sharp Sword.')
                print('One of the goblins was carrying some rope.')
                print('You proceed to pick it up and attach it to your belt.')
                print('You recieve 5 gold.')
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
            dialog()
            print('The goblins then surrounded you.')
            dialog()
            print('You eventually defeat them all, however take 2 damage in the process.')
            dialog()
            health = health - 2
            clear()
            Main()
            hp()
            print('You attempt to hide however are spotted.')
            print('The goblins then surrounded you.')
            print('You eventually defeat them all, however take 2 damage in the process.')
            print('You recieve 5 gold.')
            gold = gold + 5
            dialog()
            while True:
                clear()
                Main()
                hp()
                print('You attempt to hide however are spotted.')
                print('The goblins then surrounded you.')
                print('You eventually defeat them all, however take 2 damage in the process.')
                print('You recieve 5 gold.')
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
        print('The ground beneath you will give away any second now!')
        print('What will you do?')
        action=input('[1] Run Away [2] Hug the wall \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level2_A()
        else:
            if path_c == 1:
                clear()
                Main()
                hp()
                print('You managed to run away somewhat safely')
                dialog()
                print('However trip and fall taking 2 damage.')
                health = health - 2
                dialog()
                clear()
                Main()
                hp()
                print('You managed to run away somewhat safely')
                print('However trip and fall taking 2 damage.')
                dialog()
                while True:
                    clear()
                    Main()
                    hp()
                    print('You managed to run away somewhat safely')
                    print('However trip and fall taking 2 damage.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('Path ends here....')
                        time.sleep(2)
                        classSelect2()
                    else:
                        continue
            elif path_c == 2:
                clear()
                Main()
                hp
                print('You hug the wall, hoping that this area is not affected by the trap.')
                dialog()
                print('The ground gives way, beneath you see spikes.')
                dialog()
                print('You start falling back first into the spikes, staring at the ceiling.')
                dialog()
                print('You are killed insantly.')
                dialog()
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect2()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level2_ALR()

    elif archerR == True:
        print('You see a Cursed Bow')
        print('You pick it up, dealing 1 curse damage over time')
        print('The cursed effect seems to only last for 1 turn.')
        health = health - 1
        while True:
            clear()
            Main()
            hp()
            print('You see a Cursed Bow')
            print('You pick it up, dealing 1 curse damage over time')
            print('The cursed effect seems to only last for 1 turn.')
            action=input('[Enter/Return] to Continue \n')
            if action == "":
                level2_A3()
            else:
                continue
    else:
        print('WTF')
def level2_ALR():
    clear()
    Main()
    hp
    print('You hug the wall, hoping that this area is not affected by the trap.')
    print('The ground gives way, beneath you see spikes.')
    print('You start falling back first into the spikes, staring at the ceiling.')
    print('You are killed insantly.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level2_ALR()
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
        level2_A3()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            dialog()
            print('However they have two archers and a warrior.')
            dialog()
            print('As you defeat one archer the other continues firing at you.')
            dialog()
            print('You take 2 damage.')
            health = health - 2
            dialog()
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            dialog()
            print('You then return fire managing to take him down.')
            dialog()
            print('However at the same time the warrior attacks you dealing 3 damage.')
            dialog()
            health = health - 3
            dialog()
            clear()
            Main()
            hp()
            print('You start engaging in combat.')
            print('However they have two archers and a warrior.')
            print('As you defeat one archer the other continues firing at you.')
            print('You take 2 damage.')
            print('You then return fire managing to take him down.')
            print('However at the same time the warrior attacks you dealing 3 damage.')
            dialog()
            print('You open the door that they were guarding.')
            dialog()
            print('Inside you see some health you pick up.')
            dialog()
            print('You gain 1 health.')
            health = health + 1
            dialog()
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
            dialog()
            print('Curse Bow inflicts 1 curse damage.')
            dialog()
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
            while True:
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
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    print('Path ends here....')
                    time.sleep(2)
                    classSelect2()
                else:
                    continue
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('Your attempt to sneak past was successful!')
            dialog()
            print('The guards did not notice you.')
            while True:
                clear()
                Main()
                hp()
                print('Your attempt to sneak past was successful!')
                print('The guards did not notice you.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    print('Path ends here....')
                    time.sleep(2)
                    classSelect2()
                else:
                    continue
        else:
            level2_A3()
def level2_S():
    global health
    clear()
    Main()
    hp2()
    if earth == True:
        print('You see a master wizzard ahead')
        print('He seems to be holding a Legendary Staff')
        print('What do you do?')
        action=input('[1] Fight [2] Sneak Past \n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level2_S()
        else:
            if path_c == 1:
                clear()
                Main()
                hp2()
                print('You start engaging in combat')
                dialog()
                print('You send your Earth Elemental ahead to attack.')
                dialog()
                print('The Master Wizzard casts a fireball and shoots it at you.')
                dialog()
                print('The Earth Elemental shields you from damage.')
                dialog()
                print('You then charge together with your Earth Elemental.')
                dialog()
                print('You catch the Master Wizzard off guard.')
                dialog()
                print('The Master Wizzard is defeated.')
                dialog()
                print('Legendary Staff Acquired!')
                while True:
                    clear()
                    Main()
                    hp2()
                    print('You start engaging in combat')
                    print('You send your Earth Elemental ahead to attack.')
                    print('The Master Wizzard casts a fireball and shoots it at you.')
                    print('The Earth Elemental shields you from damage.')
                    print('You then charge together with your Earth Elemental.')
                    print('You catch the Master Wizzard off guard.')
                    print('The Master Wizzard is defeated.')
                    print('Legendary Staff Acquired!')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('Path ends here....')
                        time.sleep(2)
                        classSelect2()
                    else:
                        continue
            elif path_c == 2:
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                dialog()
                print('The Master Wizzard notices you and starts casting fireball.')
                dialog()
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                dialog()
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                dialog()
                health = health - 5
                clear()
                Main()
                hp2()
                print('You attempt to sneak past, however your Earth Elemental is too big.')
                print('The Master Wizzard notices you and starts casting fireball.')
                print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                dialog()
                print('You then attack together with your Earth Elemental.')
                dialog()
                print('You finally defeat the Master Wizzard however the legendary staff...')
                dialog()
                print('Was destroyed in the battle.')
                while True:
                    clear()
                    Main()
                    hp2()
                    print('You attempt to sneak past, however your Earth Elemental is too big.')
                    print('The Master Wizzard notices you and starts casting fireball.')
                    print('You panic and send your Earth Elemental to attack the Master Wizzard.')
                    print('The fireball goes past the Earth Elemental and inflicts 5 damage.')
                    print('You then attack together with your Earth Elemental.')
                    print('You finally defeat the Master Wizzard however the legendary staff...')
                    print('Was destroyed in the battle.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('Path ends here....')
                        time.sleep(2)
                        classSelect2()
                    else:
                        continue
            else:
                clear()
                level2_S()
    elif fire == True:
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
            level2_S()
        else:
            if path_c == 1:
                clear()
                Main()
                hp2()
                print('You close in on the Water Elemental together.')
                dialog()
                print("However your Fire Elemental can't damage the Water Elemental!")
                dialog()
                print('The Water Elemental sees an opportunity to attack!')
                dialog()
                print('The Water Elemental attacks you both inflicting 4 damage.')
                dialog()
                health = health - 4
                print('Your Fire Elemental is heavily wounded, you must now fight alone.')
                dialog()
                clear()
                Main()
                hp2()
                print('You close in on the Water Elemental together.')
                print("However your Fire Elemental can't damage the Water Elemental!")
                print('The Water Elemental sees an opportunity to attack!')
                print('The Water Elemental attacks you both inflicting 4 damage.')
                print('Your Fire Elemental is heavily wounded, you must now fight alone.')
                dialog()
                print('You eventually defeat the Water Elemental however it leaves you wounded.')
                while True:
                    clear()
                    Main()
                    hp2()
                    print('You close in on the Water Elemental together.')
                    print("However your Fire Elemental can't damage the Water Elemental!")
                    print('The Water Elemental sees an opportunity to attack!')
                    print('The Water Elemental attacks you both inflicting 4 damage.')
                    print('Your Fire Elemental is heavily wounded, you must now fight alone.')
                    print('You eventually defeat the Water Elemental however it leaves you wounded.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('Path ends here....')
                        time.sleep(2)
                        classSelect2()
                    else:
                        continue
            elif path_c == 2:
                clear()
                Main()
                hp2()
                print('You draw your sword preparing for battle.')
                dialog()
                print('Your Fire Elemental would not be very useful in this fight.')
                dialog()
                print('You attack, catching the Water Elemental off guard killing him instantly.')
                while True:
                    clear()
                    Main()
                    hp2()
                    print('You draw your sword preparing for battle.')
                    print('Your Fire Elemental would not be very useful in this fight.')
                    print('You attack, catching the Water Elemental off guard killing him instantly.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        print('Path ends here....')
                        time.sleep(2)
                        classSelect2()
                    else:
                        continue
            else:
                clear()
                level2_S()
    else:
        print('WTF')
def level3_WL1():
    global health
    global warriorLLL
    global warriorLRR
    clear()
    Main()
    hp()
    if warriorLL == True:
        print('You see a ledge up ahead.')
        print('You slowly approach it and lean over the edge.')
        print("It's pitch black...")
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
                clear()
                Main()
                hp()
                print('You proceed to use the rope to climb down the ledge.')
                dialog()
                print('On the way down you notice that the area below you is getting brighter.')
                dialog()
                print('You then touch down on the ground, and around you are bright torches.')
                dialog()
                print('You see one two hallways ahead of you...')
                while True:
                    clear()
                    Main()
                    hp()
                    print('You proceed to use the rope to climb down the ledge.')
                    print('On the way down you notice that the area below you is getting brighter.')
                    print('You then touch down on the ground, and around you are bright torches.')
                    print('You see one two hallways ahead of you...')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        level5_W()
                    else:
                        continue
            elif path_c == 2:
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                dialog()
                print('You suddenly spot a Legendary Eagle Master.')
                dialog()
                print('He notices you insantly and begins to ready himself for battle.')
                dialog()
                print('You get caught off guard and proceed to retreat back to ready yourself.')
                dialog()
                print('The Legendary Eagle Master starts shooting at you with his Legendary Bow.')
                dialog()
                print('The 3 arrows that hit inflict 6 damage.')
                dialog()
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
                dialog()
                print('The Legendary Eagle Master catches up too you starts swinging his sword.')
                dialog()
                print('You block with your Sharp Sword and swing at him with full force.')
                dialog()
                print('The Legendary Eagle Master blocks with ease and swings back.')
                dialog()
                print('His sword cuts into your flesh causing a deep wound.')
                dialog()
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
                dialog()
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
                dialog()
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
                    classSelect2()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WLL()
            else:
                clear()
                level3_WL1()
    elif warriorLR == True:
        print('At your left you spot a Treasure Chest.')
        dialog()
        print('However around it are many spike traps.')
        dialog()
        print('But on the right you see a Skeleton Warrior.')
        dialog()
        print('He seems...')
        dialog()
        level3_WL2()
    else:
        print('WTF')
def level3_WL2():
    global health
    global gold
    global warriorLRR
    clear()
    Main()
    hp()
    print('At your left you spot a Treasure Chest.')
    print('However around it are many spike traps.')
    print('But on the right you see a Skeleton Warrior.')
    print('He seems to be holding a Ring?')
    print("Yes. It's a Ring, a gold one.")
    print('What do you do?')
    action=input('[1] Treasure Chest [2] Skeleton Warrior \n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level3_WL2()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('You turn left heading towards the Treasure Chest.')
            dialog()
            print('As you get closer you notice that the lighting had gotten darker.')
            dialog()
            print('Then without realising you trigger a trip wire.')
            dialog()
            print('Suddenly the ground below you disappears and you fall into spikes.')
            dialog()
            health = 0
            clear()
            Main()
            hp()
            print('You turn left heading towards the Treasure Chest.')
            print('As you get closer you notice that the lighting had gotten darker.')
            print('Then without realising you trigger a trip wire.')
            print('Suddenly the ground below you disappears and you fall into spikes.')
            dialog()
            print('\nGAME OVER!')
            action=input('Try Again? [Y/N]\n')
            if action == 'Y' or action =='y':
                classSelect2()
            elif action =='N' or action =='n':
                quit()
            else:
                level3_WLR()
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('You turn right heading towards the Skeleton Warrior.')
            dialog()
            print('As you get closer the Skeleton Warrior notices you.')
            dialog()
            print('You both ready yourselves for battle.')
            dialog()
            print('You thrust with your Sharp Sword.')
            dialog()
            print('It hits his left leg disconnecting it from his main body.')
            dialog()
            print('As he falls forward onto the ground he swings wildly.')
            dialog()
            print('The Skeleton Warrior manages to cut your leg inflicting 3 damage.')
            dialog()
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
            dialog()
            print('In his left palm you see the gold ring.')
            dialog()
            print("You pick it up, on the ring it says: 'Legendary Eagle Master'")
            dialog()
            print('What could this mean?')
            dialog()
            print('You recieve 5 gold.')
            gold = gold + 5
            dialog()
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
                print('You recieve 5 gold.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    level4_W()
                else:
                    continue

        else:
            clear()
            level3_WL2()
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
        classSelect2()
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
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WLR()
def level3_WR1():
    global health
    global warriorRLR
    global warriorRRR
    clear()
    Main()
    hp()
    if warriorRL == True:
        print('You see a door ahead...')
        dialog()
        print('However there seems to be 10 guards in front of it.')
        dialog()
        print('What do you do?')
        dialog()
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
                clear()
                Main()
                hp()
                print('With the sword in your hand, you start attacking.')
                dialog()
                print('You take down 3, this is looking good.')
                dialog()
                print('However from the door appears a Legendary Eagle Master.')
                dialog()
                print('The rest of the guardsmen are fueled with confidence.')
                dialog()
                print('They all start charging, you try to parry them away..')
                dialog()
                print('They eventually overwhelm you.')
                dialog()
                print('They inflict 6 damage.')
                health = health - 6
                dialog()
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
                dialog()
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect2()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WRL()
            elif path_c == 2:
                clear()
                Main()
                hp()
                print('You plan out your route.')
                dialog()
                print("You see 4 Archers and 6 Warriors.")
                dialog()
                print('You follow the right wall, however half-way through..')
                dialog()
                print('An Archer spots you, he shouts out to the other guards. You start running.')
                dialog()
                print('The archers fire at you, one arrow hits your back, the other hits your leg.')
                dialog()
                print("However you make it to the exit, they won't be able to follow you now.")
                dialog()
                print('In total they dealt 4 damage.')
                dialog()
                health = health - 4
                clear()
                Main()
                hp()
                print('You plan out your route.')
                print("You see 4 Archers and 6 Warriors.")
                print('You follow the right wall, however half-way through..')
                print('An Archer spots you, he shouts out to the other guards. You start running.')
                print('The archers fire at you, one arrow hits your back, the other hits your leg.')
                print("However you make it to the exit, they won't be able to follow you now.")
                print('In total they dealt 4 damage.')
                while True:
                    clear()
                    Main()
                    hp()
                    print('You plan out your route.')
                    print("You see 4 Archers and 6 Warriors.")
                    print('You follow the right wall, however half-way through..')
                    print('An Archer spots you, he shouts out to the other guards. You start running.')
                    print('The archers fire at you, one arrow hits your back, the other hits your leg.')
                    print("However you make it to the exit, they won't be able to follow you now.")
                    print('In total they dealt 4 damage.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        warriorRLR=True
                        level4_WRLR()
                    else:
                        continue
            else:
                clear()
                level3_WR1()
    elif warriorRR == True:
        print('Up ahead you see an old witch.')
        dialog()
        print('She seems to be making Health Potions.')
        dialog()
        print('Behind her are a stack off 3 Health Potions.')
        dialog()
        print('They seem to recover 1 Health per use.')
        dialog()
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
                clear()
                Main()
                hp()
                print('You ready yourself for battle.')
                dialog()
                print('The old witch notices you and she quickly retreats back into her home.')
                dialog()
                print('You follow her, however...')
                dialog()
                print('She had actually laid traps around the area, and you have set them off.')
                dialog()
                print('They deal 1 poison damage.')
                dialog()
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
                dialog()
                print('But she splashes a potion onto you that makes you fall asleep.')
                dialog()
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
                dialog()
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
                dialog()
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
                dialog()
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
                dialog()
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
                dialog()
                clear()
                Main()
                hp()
                print("You wake up to find that you've been stripped of all your belongings.")
                dialog()
                print("She has also taken your Sword.")
                dialog()
                print("You walk back the way you came until you see the Witch's home again.")
                dialog()
                print('You begin knocking on the door asking for your items back.')
                dialog()
                print('In return she stabs you through the door with your very own Sword.')
                dialog()
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
                dialog()
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect2()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level3_WRR()

            elif path_c == 2:
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                dialog()
                print('You offer your Sword and in return she gives you a health potion.')
                dialog()
                health = health + 1
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                print('You offer your Sword and in return she gives you a health potion.')
                dialog()
                print('She then beckons you to come to her home.')
                dialog()
                print('You comply and follow her.')
                dialog()
                print('Inside her home she offers you more health potions.')
                dialog()
                print('You now feel overcharged.')
                health = 15
                dialog()
                clear()
                Main()
                hp()
                print('You approach the old witch.')
                print('You offer your Sword and in return she gives you a health potion.')
                print('She then beckons you to come to her home.')
                print('You comply and follow her.')
                print('Inside her home she offers you more health potions.')
                print('You now feel overcharged.')
                while True:
                    clear()
                    Main()
                    hp()
                    print('You approach the old witch.')
                    print('You offer your Sword and in return she gives you a health potion.')
                    print('She then beckons you to come to her home.')
                    print('You comply and follow her.')
                    print('Inside her home she offers you more health potions.')
                    print('You now feel overcharged.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        warriorRRR=True
                        level4_WRRR()
                    else:
                        continue
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
        classSelect2()
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
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level3_WRR()
def level4_W():
    global health
    global gold
    clear()
    Main()
    hp()
    print('You see a ledge up ahead.')
    print('You slowly approach it and lean over the edge.')
    print("It's pitch black...")
    print('What do you do?')
    action=input('[1] Climb down [2] Find another route.\n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level4_W()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('As you begin climbing down you notice how dark it really is.')
            dialog()
            print('After a while it starts getting harder to find footings in the rocks.')
            dialog()
            print('Suddenly you lose grip on the rock and start falling.')
            dialog()
            print('You hit the ground killing you instantly.')
            dialog()
            print('\nGAME OVER!')
            action=input('Try Again? [Y/N]\n')
            if action == 'Y' or action =='y':
                classSelect2()
            elif action =='N' or action =='n':
                quit()
            else:
                level4_WLRR()
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('As you begin look around for another passageway..')
            dialog()
            print('You suddenly spot someone to your right wearing heavy armour.')
            dialog()
            print('He notices you insantly and begins to ready himself for battle.')
            dialog()
            print('You do the same drawing your sword.')
            dialog()
            print('As he closes in for the attack...')
            dialog()
            print('He suddenly screams in pain.')
            dialog()
            print('The ring you are wearing is now shining brightly.')
            dialog()
            print('You wave the ring in his direction only causing more pain.')
            dialog()
            print("It all makes sense now.. he must be the 'Legendary Eagle Master' ")
            dialog()
            print('The ring must be keeping him away.')
            dialog()
            print('Using the ring I quickly end his life, on his belt is some rope.')
            dialog()
            print('With this rope I can climb down the ledge now.')
            dialog()
            print('You proceed to use the rope to climb down the ledge.')
            dialog()
            print('On the way down you notice that the area below you is getting brighter.')
            dialog()
            print('You then touch down on the ground, and around you are bright torches.')
            dialog()
            print('You see one two hallways ahead of you...')
            dialog()
            print('You recieve 10 gold.')
            gold = gold + 10
            dialog()
            while True:
                clear()
                Main()
                hp()
                print('As you begin look around for another passageway..')
                print('You suddenly spot someone to your right wearing heavy armour.')
                print('He notices you insantly and begins to ready himself for battle.')
                print('You do the same drawing your sword.')
                print('As he closes in for the attack...')
                print('He suddenly screams in pain.')
                print('The ring you are wearing is now shining brightly.')
                print('You wave the ring in his direction only causing more pain.')
                print("It all makes sense now.. he must be the 'Legendary Eagle Master' ")
                print('The ring must be keeping him away.')
                print('Using the ring I quickly end his life, on his belt is some rope.')
                print('With this rope I can climb down the ledge now.')
                print('You proceed to use the rope to climb down the ledge.')
                print('On the way down you notice that the area below you is getting brighter.')
                print('You then touch down on the ground, and around you are bright torches.')
                print('You see one two hallways ahead of you...')
                print('You recieve 10 gold.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    warriorLRRL=True
                    level5_W()
                else:
                    continue
        else:
            clear()
            level4_W()
def level4_WLLL():
    clear()
    Main()
    hp()
    print('You start walking towards the Left Hallway.')
    print('The walk slowly turns into a job.')
    print('You now sprinting towards the Opening.')
    print('As you step out, you feel a warm ray shine onto you.')
    print('You look around and notice that you are on a deserted island.')
    print('Behind you the exit from the Dungeon disappears.')
    print('Days past without access to fresh water, you start to dehydrate.')
    print('Before long, you die of both starvation and dehydration.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level4_WLLL()
def level4_WLRR():
    clear()
    Main()
    hp()
    print('As you begin climbing down you notice how dark it really is.')
    print('After a while it starts getting harder to find footings in the rocks.')
    print('Suddenly you lose grip on the rock and start falling.')
    print('You hit the ground killing you instantly.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level4_WLRR()
def level4_WRLR():
    global warriorRLR
    global health
    clear()
    Main()
    hp()
    if warriorRLR==True:
        print('After narrowly escaping death, you continue moving forward.')
        dialog()
        print("At the same time pulling out the arrows that made it's mark")
        dialog()
        print('Ultimately collapsing from blood loss.')
        dialog()
        print('You wake up to find yourself surrounded by a breed of hybrids?')
        dialog()
        print('They seem to have scales on their legs, perhaps half-dragon?')
        dialog()
        print("'You Seem to be awake, Adventurer we are of the Dragonrace.'")                                                      #UP TO HERE
        dialog()
        print("'We are both half-dragon and half-human.'")
        dialog()
        print('You quickly get up on my feet and look for the source of the voice')
        dialog()
        print("You promptly identify him through his decorative necklace.")
        dialog()
        print('He must be the leader you thought.')
        dialog()
        print('You turn towards him and start walking towards him.')
        dialog()
        print('However the pain in your leg and arm seem to have... vanished?')
        dialog()
        print('You look at your wounds and they seem to have been healed.')
        dialog()
        print('You gain 3 health.')
        dialog()
        health = health + 3
        level4_WRLR2()
    elif warriorLRR == True:
        print('You see a ledge up ahead.')
        print('You slowly approach it and lean over the edge.')
        print("It's pitch black...")
        print('What do you do?')
        action=input('[1] Climb down [2] Find another route.\n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level4_W()
        else:
            if path_c == 1:
                clear()
                Main()
                hp()
            elif path_c == 2:
                clear()
                Main()
                hp()
            else:
                clear()
                level4_WRLR()
    else:
        print('WTF')
def level4_WRLR2():
    global health
    global gold
    clear()
    Main()
    hp()
    print('After narrowly escaping death, you continue moving forward.')
    print("At the same time pulling out the arrows that made it's mark")
    print('Ultimately collapsing from blood loss.')
    print('You wake up to find yourself surrounded by a breed of hybrids?')
    print('They seem to have scales on their legs, perhaps half-dragon?')
    print("'You Seem to be awake, Adventurer we are of the Dragonrace.'")                                                      #UP TO HERE
    print("'We are both half-dragon and half-human.'")
    print('You quickly get up on my feet and look for the source of the voice')
    print("You promptly identify him through his decorative necklace.")
    print('He must be the leader you thought.')
    print('You turn towards him and start walking towards him.')
    print('However the pain in your leg and arm seem to have... vanished?')
    print('You look at your wounds and they seem to have been healed.')
    print('You gain 3 health.')
    print("You address him and ask: 'Did you heal me?' ")
    print("'Yes we of the Dragonrace come in peace.'")
    print("'We do not wish to engage in violence.'")
    print('What do you do?')
    action=input('[1] Turn Hostile [2] Accept Hospitality\n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level4_WRLR2()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('You quickly draw your sword and swing towards the crowd.')
            dialog()
            print('Causing a massive outcry from the Dragonrace, 3 bodies slump to the ground.')
            dialog()
            print('The rest back off preparing for battle, you count 4 more excluding the Leader.')
            dialog()
            print('To your right you spot a incline, you run towards it.')
            dialog()
            print('Having the height advantage in this situation would be good.')
            dialog()
            print('I slash downwards downing another Dragonrace enemy.')
            dialog()
            print('The rest seem more experienced with battle hardened faces. You prepare for a rush however...')
            dialog()
            print('Instead they begin breathing in air..?')
            dialog()
            print('You back off, confused as to what they are doing.')
            dialog()
            print('Suddenly a burst of flame come out of their mouths, Instantly scorching the ground in front, leaving heat marks.')
            dialog()
            print('Of course I thought to myself, they are half-dragon. I need to be careful from now on.')
            dialog()
            print('They approach you with fists, perhaps experts in hand to hand combat.')
            dialog()
            print('You keep your distance while at the same time slashing down, another 2 bite the dust.')
            dialog()
            print("Only two more remain. You jump off the incline, landing on the Dragonrace's head.")
            dialog()
            print('Then kicking off instantly knocking him down, you land and in front of is their leader.')
            dialog()
            print('Behind you hear the body hit the ground.')
            dialog()
            print("'We are of the proud Dragonrace we will not go down so easily.'")
            dialog()
            print('He seems to be holding a staff, perhaps a magic user?')
            dialog()
            print('Suddenly he summons a Water Elemental, It attacks slasheing your arm dealing 2 damage.')
            dialog()
            health = health - 2
            clear()
            Main()
            hp()
            print('You quickly draw your sword and swing towards the crowd.')
            print('Causing a massive outcry from the Dragonrace, 3 bodies slump to the ground.')
            print('The rest back off preparing for battle.')
            print('You count 4 more excluding the Leader.')
            print('To your right you spot a incline, you run towards it.')
            print('Having the height advantage in this situation would be good.')
            print('I slash downwards downing another Dragonrace enemy.')
            print('The rest seem more experienced with battle hardened faces.')
            print('You prepare for a rush however... Instead they begin breathing in air..?')
            print('You back off, confused as to what they are doing.')
            print('Suddenly a burst of flame come out of their mouths, scorching the ground in front.')
            print('Of course I thought to myself, they are half-dragon. I need to be careful from now on.')
            print('They approach you with fists, perhaps experts in hand to hand combat.')
            print('You keep your distance while at the same time slashing down, another 2 bite the dust.')
            print("Only two more remain. You jump off the incline, landing on the Dragonrace's head.")
            print('Then kicking off instantly knocking him down, you land and in front of is their leader.')
            print('Behind you hear the body hit the ground.')
            print("'We are of the proud Dragonrace we will not go down so easily.'")
            print('He seems to be holding a staff, perhaps a magic user?')
            print('Suddenly he summons a Water Elemental, It attacks slasheing your arm dealing 2 damage.')
            dialog()
            print('Unfazed you charge foward dealing the fatal blow.')
            dialog()
            print('It connects it pierces right through his scales killing him. You emerge victorious.')
            dialog()
            print('Up ahead you spot two hallways...')
            dialog()
            print('You recieve 10 gold.')
            gold = gold + 10
            dialog()
            while True:
                clear()
                Main()
                hp()
                print('You quickly draw your sword and swing towards the crowd.')
                print('Causing a massive outcry from the Dragonrace, 3 bodies slump to the ground.')
                print('The rest back off preparing for battle.')
                print('You count 4 more excluding the Leader.')
                print('To your right you spot a incline, you run towards it.')
                print('Having the height advantage in this situation would be good.')
                print('I slash downwards downing another Dragonrace enemy.')
                print('The rest seem more experienced with battle hardened faces.')
                print('You prepare for a rush however... Instead they begin breathing in air..?')
                print('You back off, confused as to what they are doing.')
                print('Suddenly a burst of flame come out of their mouths, scorching the ground in front.')
                print('Of course I thought to myself, they are half-dragon. I need to be careful from now on.')
                print('They approach you with fists, perhaps experts in hand to hand combat.')
                print('You keep your distance while at the same time slashing down, another 2 bite the dust.')
                print("Only two more remain. You jump off the incline, landing on the Dragonrace's head.")
                print('Then kicking off instantly knocking him down, you land and in front of is their leader.')
                print('Behind you hear the body hit the ground.')
                print("'We are of the proud Dragonrace we will not go down so easily.'")
                print('He seems to be holding a staff, perhaps a magic user?')
                print('Suddenly he summons a Water Elemental, It attacks slasheing your arm dealing 2 damage.')
                print('Unfazed you charge foward dealing the fatal blow.')
                print('It connects it pierces right through his scales killing him. You emerge victorious.')
                print('Up ahead you spot two hallways...')
                print('You recieve 10 gold.')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    level5_W()
                else:
                    continue
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('You slowly pick yourself up, turn and thank each individual.')
            dialog()
            print('After a full circle you had counted 8 Dragonrace.')
            dialog()
            print('With thanks you quickly turn and leave.')
            dialog()
            print('However they do not let you out.')
            dialog()
            print('Instead they ready themselves for battle.')
            dialog()
            print("Confused you ask: 'What's going on?'")
            dialog()
            print("The Leader replies with: 'We did not heal you so that you can continue fighting.'")
            dialog()
            print('You will stay with us or die.')
            dialog()
            print('You draw your sword bracing for impact.')
            dialog()
            print('All 8 attack at the same time, instantly knocking you down.')
            dialog()
            print('They continue beating you until you die.')
            dialog()
            health = 0
            print('\nGAME OVER!')
            action=input('Try Again? [Y/N]\n')
            if action == 'Y' or action =='y':
                classSelect2()
            elif action =='N' or action =='n':
                quit()
            else:
                level4_WRLR3()
        else:
            clear()
            level4_WRLR2()

def level4_WRLR3():
    clear()
    Main()
    hp()
    print('You slowly pick yourself up, turn and thank each individual.')
    print('After a full circle you had counted 8 Dragonrace.')
    print('With thanks you quickly turn and leave.')
    print('However they do not let you out.')
    print('Instead they ready themselves for battle.')
    print("Confused you ask: 'What's going on?'")
    print("The Leader replies with: 'We did not heal you so that you can continue fighting.'")
    print('You will stay with us or die.')
    print('You draw your sword bracing for impact.')
    print('All 8 attack at the same time, instantly knocking you down.')
    print('They continue beating you until you die.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level4_WRLR3()
def level4_WRRR():
    global gold
    global health
    global warriorRRR
    clear()
    Main()
    hp()
    if warriorRRR==True:
        print('Feeling energized you continue on your journey.')
        print('You then spot a Golden Sword that appears to be stuck within this stone.')
        print('What do you do?')
        action=input('[1] Pull out the Sword [2] Keep going Forward\n')
        try:
            path_c = int(action)
        except ValueError:
            path_c = 0
        if path_c == 0:
            clear()
            level4_WRRR()
        else:
            if path_c == 1:
                clear()
                Main()
                hp()
                print('You slowly approach the sword, putting one foot in front of the other.')
                dialog()
                print('You put both hands on the handle of the sword and proceed to pull.')
                dialog()
                print("It doesn't budge, suddenly a flash of lightning strikes down.")
                dialog()
                print('It hits you directly, killing you instantly.')
                dialog()
                health = 0
                clear()
                Main()
                hp()
                print('You slowly approach the sword, putting one foot in front of the other.')
                print('You put both hands on the handle of the sword and proceed to pull.')
                print("It doesn't budge, suddenly a flash of lightning strikes down.")
                print('It hits you directly, killing you instantly.')
                print('\nGAME OVER!')
                action=input('Try Again? [Y/N]\n')
                if action == 'Y' or action =='y':
                    classSelect2()
                elif action =='N' or action =='n':
                    quit()
                else:
                    level4_WRRR2()
            elif path_c == 2:
                clear()
                Main()
                hp()
                print('You deem that you are not worthy enough for the Golden Sword and continue on.')
                dialog()
                print('As you continue walking along the path, the ceiling widens.')
                dialog()
                print('You look around to find yourself in a giant courtyard. However at the centre.')
                dialog()
                print("Lie another Golden Sword. Suddenly you hear a voice: 'This is the Golden Sword.'")
                dialog()
                print('You look around searching for the source of the voice.')
                dialog()
                print('You spot a Pudding, a Magical Pudding, it seems to have a face, arms and legs.')
                dialog()
                print("You ask: 'I just saw a Golden Sword earlier.'")
                dialog()
                print("The Magical Pudding replies with: 'That is a trap used to trick thieves.'")
                dialog()
                print("The Magical Pudding continues: 'You however are the first to make it this far.'")
                dialog()
                print('Thus you may inherit the Swords power and continue on in your journey.')
                dialog()
                print('I approach the Golden Sword and place both hands on the handle.')
                dialog()
                print('Suddenly there is a ray of light and you fall back with Sword in hand.')
                dialog()
                print('However in the process you take 10 damage as compensation.')
                health = health - 10
                dialog()
                clear()
                Main()
                hp()
                print('You deem that you are not worthy enough for the Golden Sword and continue on.')
                print('As you continue walking along the path, the ceiling widens.')
                print('You look around to find yourself in a giant courtyard. However at the centre.')
                print("Lie another Golden Sword. Suddenly you hear a voice: 'This is the Golden Sword.'")
                print('You look around searching for the source of the voice.')
                print('You spot a Pudding, a Magical Pudding, it seems to have a face, arms and legs.')
                print("You ask: 'I just saw a Golden Sword earlier.'")
                print("The Magical Pudding replies with: 'That is a trap used to trick thieves.'")
                print("The Magical Pudding continues: 'You however are the first to make it this far.'")
                print('Thus you may inherit the Swords power and continue on in your journey.')
                print('I approach the Golden Sword and place both hands on the handle.')
                print('Suddenly there is a ray of light and you fall back with the sword in hand.')
                print('However in the process you take 10 damage as compensation.')
                print('You pick yourself up, however you are surrounded.')
                print('Your enemies seem to be Magical Puddings, you charge aiming to make a clearing.')
                dialog()
                print('Bracing for impact, you expect to hit the Magical Pudding, however instead...')
                dialog()
                print('You had been teleported into a room with two hallways.')
                dialog()
                print('Did they do this?')
                dialog()
                print('You recieve 15 gold.')
                gold = gold + 15
                while True:
                    clear()
                    Main()
                    hp()
                    print('You deem that you are not worthy enough for the Golden Sword and continue on.')
                    print('As you continue walking along the path, the ceiling widens.')
                    print('You look around to find yourself in a giant courtyard. However at the centre.')
                    print("Lie another Golden Sword. Suddenly you hear a voice: 'This is the Golden Sword.'")
                    print('You look around searching for the source of the voice.')
                    print('You spot a Pudding, a Magical Pudding, it seems to have a face, arms and legs.')
                    print("You ask: 'I just saw a Golden Sword earlier.'")
                    print("The Magical Pudding replies with: 'That is a trap used to trick thieves.'")
                    print("The Magical Pudding continues: 'You however are the first to make it this far.'")
                    print('Thus you may inherit the Swords power and continue on in your journey.')
                    print('I approach the Golden Sword and place both hands on the handle.')
                    print('Suddenly there is a ray of light and you fall back with the sword in hand.')
                    print('However in the process you take 10 damage as compensation.')
                    print('You pick yourself up, however you are surrounded.')
                    print('Your enemies seem to be Magical Puddings, you charge aiming to make a clearing.')
                    print('Bracing for impact, you expect to hit the Magical Pudding, however instead...')
                    print('You had been teleported into a room with two hallways.')
                    print('Did THEY do this?')
                    print('You recieve 15 gold.')
                    action=input('[Enter/Return] to Continue \n')
                    if action == "":
                        level5_W()
                    else:
                        continue
            else:
                level4_WRRR()
def level4_WRRR2():
    clear()
    Main()
    hp()
    print('You slowly approach the sword, putting one foot in front of the other.')
    print('You put both hands on the handle of the sword and proceed to pull.')
    print("It doesn't budge, suddenly a flash of lightning strikes down.")
    print('It hits you directly, killing you instantly.')
    print('\nGAME OVER!')
    action=input('Try Again? [Y/N]\n')
    if action == 'Y' or action =='y':
        classSelect2()
    elif action =='N' or action =='n':
        quit()
    else:
        level4_WRRR2()
def level5_W():
    global health
    global gold
    clear()
    Main()
    hp()
    print('The Left Hallway has many torches and seems to lead to some sort of Opening?')
    print('Yes a Dungeon Opening, from here I can faintly hear the sound of the wind.')
    print('However the Right Hallway is giving the opposite effect.')
    print('It is dimly lit, with human skeleton bones scattered throughout the hallway.')
    print('What do you do?')
    action=input('[1] Left Hallway [2] Right Hallway\n')
    try:
        path_c = int(action)
    except ValueError:
        path_c = 0
    if path_c == 0:
        clear()
        level5_W()
    else:
        if path_c == 1:
            clear()
            Main()
            hp()
            print('You start walking towards the Left Hallway.')
            dialog()
            print('The walk slowly turns into a job.')
            dialog()
            print('You now sprinting towards the Opening.')
            dialog()
            print('Suddenly the ground beneath you disappears, below you is molten lava.')
            dialog()
            print('You drop and die insantly.')
            health = 0
            clear()
            Main()
            hp()
            print('You start walking towards the Left Hallway.')
            print('The walk slowly turns into a job.')
            print('You now sprinting towards the Opening.')
            print('Suddenly the ground beneath you disappears, below you is molten lava.')
            print('You drop and die insantly.')
            print('\nGAME OVER!')
            action=input('Try Again? [Y/N]\n')
            if action == 'Y' or action =='y':
                classSelect2()
            elif action =='N' or action =='n':
                quit()
            else:
                level4_WLLL()
        elif path_c == 2:
            clear()
            Main()
            hp()
            print('With one hand on the right wall you begin to advance forward.')
            dialog()
            print('*Clack*, you feet bump into some bones laying on the ground.')
            dialog()
            print('A cold shiver runs down your spine as you continue onwards.')
            dialog()
            print('Suddenly you hear a *Creak*.')
            dialog()
            print('You look down and notice that the surface of the ground is now wood.')
            dialog()
            print('With a confused look you continue forward.')
            dialog()
            print('Ahead you see a lantern emitting a warm ray of light.')
            dialog()
            print('You push forward and find yourself in a room.')
            dialog()
            print('To the left you see a rack of weapons and armour.')
            dialog()
            print('To the right you see shelves of potions and books.')
            dialog()
            print("At the back of the room is a sign it reads: 'The Screaming Fire' ")
            dialog()
            print('Below that was the Shopkeeper, he was a Dwarf')
            dialog()
            print('His head barely reaching over the stand.')
            dialog()
            print('You slowly approach him...')
            while True:
                clear()
                Main()
                hp()
                print('With one hand on the right wall you begin to advance forward.')
                print('*Clack*, you feet bump into some bones laying on the ground.')
                print('A cold shiver runs down your spine as you continue onwards.')
                print('Suddenly you hear a *Creak*.')
                print('You look down and notice that the surface of the ground is now wood.')
                print('With a confused look you continue forward.')
                print('Ahead you see a lantern emitting a warm ray of light.')
                print('You push forward and find yourself in a room.')
                print('To the left you see a rack of weapons and armour.')
                print('To the right you see shelves of potions and books.')
                print("At the back of the room is a sign it reads: 'The Screaming Fire' ")
                print('Below that was the Shopkeeper, he was a Dwarf')
                print('His head barely reaching over the stand.')
                print('You slowly approach him...')
                action=input('[Enter/Return] to Continue \n')
                if action == "":
                    print('Path ends here....')
                    time.sleep(2)
                    classSelect2()
                else:
                    continue
        else:
            level5_W()
classSelect()
