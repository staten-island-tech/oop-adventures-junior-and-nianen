import time
x = 3

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
if descion_1_1 == 'FIGHT':
            time.sleep(x)
            print("You got flung back and ended up in a village")
if descion_1 == 'Left':
    time.sleep(x)
    print("You went downa  path with herbs and unkown plants in the area")
    time.sleep(x)

print('When travelling to the village, you need some sleep')
time.sleep(x)
print('Which village hut do you want(1, 2, 3, 4, or 5)')



    