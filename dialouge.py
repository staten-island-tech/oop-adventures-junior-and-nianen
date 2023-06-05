import time
x = 3

print("YYou jave entered a world of unkown magic")
time.sleep(x)
print('You have been granted two abilities Fire or Water')
time.sleep(x)
print(" Choose an ability")

time.sleep(x)
print('You were traveling to the forest and encounter an enemy')
time.sleep(x)
print('Choose an ability')

time.sleep(x)
print('You try to attack it but couldnt land a hit')
time.sleep(x)
print("You ran instead of fighting")


time.sleep(x)
print('You have survied the enemy')
time.sleep(x)
print('Theres a right path and a left path')
time.sleep(x)
descion_1 = input(print('Which path do you take'))
if descion_1 == 'RIGHT':
    print('You travel through another forest filled with stronger enemies')
    time.sleep(x)
    print("You enter a cave where a powerful monster lies")
    time.sleep(x)
    descion_1_1 = input(print('Go back or try to fight the monster'))
    if descion_1_1 == 'GO BACK':
            time.sleep(x)
            print("You went downa  path with herbs and unkown plants in the area")
            time.sleep(x)
    else:
            time.sleep(x)
            print("You got flung back and ended up in a village")
else: 
    time.sleep(x)
    print("You went downa  path with herbs and unkown plants in the area")
    time.sleep(x)

print('When travelling to the village, you need some sleep')
time.sleep(x)
descion_3 = input(print('Which village hut do you want(1, 2, 3, 4, or 5)'))
if descion_3 == 1:
    time.sleep(x)
    print('A villager asks you why you entered their tent')
    time.sleep(x)
    print('The villager asks you to leave or die')
    descion3_1 = input(print('What do you choose(leave or die'))
    if descion3_1 == 'leave':
        descion_3 = input(print('Which village hut do you want(2, 3, 4, or 5)'))
        if descion_3 == 2:
            time.sleep(x)
            print('You entered an old abandoned tent')
            time.sleep(x)
            print('You find some sort of potion')
            time.sleep(x)
            print('you descided to drink it')
            time.sleep(x)
            print('You got teleported back to the path you were in')
            descion_3 = input(print('Which village hut do you want(3, 4, or 5)'))
            if descion_3 == 3:
                time.sleep(x)
                print("You entered an hut made for the village chief")
                time.sleep(x)
                print("He asks you what a foreigner like you is in the village and in his hunt")
                time.sleep(x)
                descion3_2 = input(print('Show him ability of yours or say you are here to kill the boss'))
                if descion3_2 != 'men':
                    time.sleep(x)
                    print('The Cheif says you look usefu; to the village')
                    time.sleep(x)
                    print('He lets you stay in the village')
        if descion_3 == 3:
            time.sleep(x)
            print("You entered an hut made for the village chief")
            time.sleep(x)
            print("He asks you what a foreigner like you is in the village and in his hunt")
            time.sleep(x)
            descion3_2 = input(print('Show him ability of yours or say you are here to kill the boss'))
            if descion3_2 != 'men':
                time.sleep(x)
                print('The Cheif says you look usefu; to the village')
                time.sleep(x)
                print('He lets you stay in the village')
if descion_3 == 2:
    time.sleep(x)
    print('You entered an old abonded tent')
    time.sleep(x)
    print('You find some sort of potion')
    time.sleep(x)
    print('Drink it or die')
    time.sleep(x)
    print('You descided to drink it')
    time.sleep(x)
    print('You got teleported back to the path you were in')
    descion_3 = input(print('Which village hut do you want(1,2,4,or 5)'))


    