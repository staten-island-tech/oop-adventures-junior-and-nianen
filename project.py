import json
import random
import time
from classes import Fire, Water, Enemy, Boss

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)

with open("fire_abilities.json", encoding="utf8") as fire_ability_file:
    fire_abilities = json.load(fire_ability_file)


enemies_defeated = 0
x = 3

attackchance = random.randint(0, 100)

print("You jave entered a world of unkown magic")
time.sleep(x)


def deal_damage(player, enemy, move):
    hit_chance = random.random()
    if hit_chance <= 0.3:
        print("You missed")
    else:
        damage = move["base"]["Attack"]
        enemy.health -= damage
        print(f"{enemy.name} took {damage} damage")

    energy_cost = move["base"]["Energy"]
    player.energy -= energy_cost
    if player.energy < 0:
        player.energy = 0

    print(f"{player.name} used {move['name']['english']}")
    print(f"Current energy: {player.energy}")
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated")



def take_damage(player, enemy):
    damage = enemy.damage
    print(f"{player.name} took {damage} damage")
    player.health -= damage
    if player.health <= 0:
        print(f"{player.name} has been defeated")
        return True
    return False

def normal_enemy_fight(player, enemies_defeated, abilities):
    randomenemy = random.randint(100, 200)
    enemy = Enemy(0, "Normal Enemy", randomenemy, randomenemy, random.randint(10, 100))
    print(f"You have encountered a normal enemy with {enemy.health} health")
    while player.health > 0 and enemy.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, enemy)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle, Icecle Snipe, Water Slash, Water Blaze, Hail Storm): ")
                for move in abilities:
                    if watermove == move["name"]["english"]:
                        deal_damage(player, enemy, move)
                        if enemy.health > 0:
                            print(f"Enemy's Current Health: {enemy.health}")
                        if enemy.health <= 0:
                            enemies_defeated += 1
                            return True
                        take_damage(player, enemy)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}")
                        if enemy.health <= 0:
                            break
                
            

        elif isinstance(player, Fire):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, enemy)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Lava Cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath, Fire Blast): ")
                for move in abilities:
                    if firemove == move["name"]["english"]:
                        deal_damage(player, enemy, move)
                        if enemy.health > 0:
                            print(f"Enemy's Current Health: {enemy.health}")
                        if enemy.health <= 0:
                            enemies_defeated += 1
                            return True
                        take_damage(player, enemy)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}")
                        if enemy.health <= 0:
                            break
                


def boss_fight(player, enemies_defeated, moves):
    random_boss = random.randint(1000, 3000)
    boss = Boss(1, "Boss", random_boss, random_boss, random.randint(50, 250))
    print(f"You have encountered a boss with {boss.health} health")
    while player.health > 0 and boss.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the boss")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the boss")
                    take_damage(player, boss)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icicle, Icicle Snipe, Water Slash, Water Blaze, Hail Storm): ")
                for move in moves:
                    if watermove == move["name"]["english"]:
                        deal_damage(player, boss, move)
                        if boss.health > 0:
                            print(f"Enemy's Current Health: {boss.health}")
                        if boss.health <= 0:
                            enemies_defeated += 1
                            return True
                        take_damage(player, boss)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}")
                        if boss.health <= 0:
                            break
        elif isinstance(player, Fire):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the boss")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the boss")
                    take_damage(player, boss)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Lava Cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoenix, Fire Breath, Fire Blast): ")
                for move in moves:
                    if firemove == move["name"]["english"]:
                        deal_damage(player, boss, move)
                        if boss.health > 0:
                            print(f"Enemy's Current Health: {boss.health}")
                        if boss.health <= 0:
                            enemies_defeated += 1
                            return True
                        take_damage(player, boss)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}")
                        if boss.health <= 0:
                            break

def add_energy(player):
    player.energy += 30
    if player.energy > player.max_energy:
        player.energy = player.max_energy
    print(f"{player.name} regenerated 30 energy. Current energy: {player.energy}")


def main():
    player_name = input("Enter your name: ")
    player_type = input("Choose an ability type (Water, Fire): ")
    time.sleep(x)
    print('You were traveling to the forest and encounter an enemy')
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
    if descion_1.upper() == 'RIGHT':
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
    if descion_3 == '1':
        time.sleep(x)
        print('A villager asks you why you entered their tent')
        time.sleep(x)
        print('The villager asks you to leave or die')
        descion3_1 = input(print('What do you choose(leave or die'))
        if descion3_1 == 'leave':
            descion_3_2 = input(print('Which village hut do you want(2, 3, 4, or 5)'))
            if descion_3_2 == '2':
                time.sleep(x)
                print('You entered an old abandoned tent')
                time.sleep(x)
                print('You find some sort of potion')
                time.sleep(x)
                print('you descided to drink it')
                time.sleep(x)
                print('You got teleported back to the path you were in')
                descion_3_3 = input(print('Which village hut do you want(3, 4, or 5)'))
                if descion_3_3 == '3':
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
            if descion_3_3 == '4':
                time.sleep(x)
                print('You go out to the village and sleep')
            if descion_3_3 == '5':
                time.sleep(x)
            print('You found a hut and descided to sleep in it since it looks so comfy')
        if descion_3_2 == '3':
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
        if descion_3_2 == '4':
            time.sleep(x)
            print('You go out to the village and sleep')
        if descion_3_2 == '5':
            time.sleep(x)
            print('You found a hut and descided to sleep in it since it looks so comfy')
        else: 
            time.sleep(x)
            print('He was so nice that he let you sleep with him')
        if descion3_1 == '3': 
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
    if descion_3 == '2':
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
        descion_3_6 = input(print('Which village hut do you want(1,3,4,or 5)'))
        if descion_3_6 == '1':
            time.sleep(x)
            print("A villager asks you why you entered their tent")
            time.sleep(x)
            print("He asks you what a foreigner like you is in the village and in his hunt")
            time.sleep(x)
            print('He makes you leave')
            time.sleep(x)
            descion_3_7 = input(print('Which village hut do you want(3, 4, or 5'))
            if descion_3_7 == '3':
                time.sleep(x)
                print("You entered an hut made for the village chief")
                time.sleep(x)
                print("He asks you what a foreigner like you is in the village and in his hunt")
                time.sleep(x)
                descion3_9 = input(print('Show him ability of yours or say you are here to kill the boss'))
                if descion3_2 != 'men':
                    time.sleep(x)
                    print('The Cheif says you look usefu; to the village')
                    time.sleep(x)
                    print('He lets you stay in the village')
            if descion_3_7 == '4':
                time.sleep(x)
                print('You go out to the village and sleep')
            if descion_3_7 == '5':
                time.sleep(x)
                print('You found a hut and descided to sleep in it since it looks so comfy')
    if descion_3 == '3':
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
    if descion_3 == '4':
        time.sleep(x)
        print('You go out to the village and sleep')
    if descion_3 == '5':
        time.sleep(x)
        print('You found a hut and descided to sleep in it since it looks so comfy')

    time.sleep(x)
    print('When you wake up, a cute and beautiful woman looks to you and says what you are doing')
    descion8 = input(print('What do you say to her when she wakes up(1:(I did not know you were there/ (2: did I accedintatly sleep with you))'))
    if descion8 != 'men1':
        time.sleep(x)
        print('She asks you what your name is')
        descion9 = input(print('1: Say your name 2: Be silent'))
        if descion9 == '1':
            time.sleep(x)
            print(f'you say your name is' [player_name]) #change it in final code
            time.sleep(x)
            print('She tells you her name which is Danielle')
        if descion9 == '2':
            time.sleep(x)
            print('You told her you do not feel comfortable saying your name')
            time.sleep(x)
            print(f'She strangles you until your name'[player_name]) #change it in final code 
            time.sleep(x)
            print('She tells you her name which is Danielle')
    time.sleep(x)
    print('You tell her your adeventure plan to fight the biggest enemy in the world')
    time.sleep(x)
    print(f'You also tell her you have' [player_type]) #change it in final code
    time.sleep(x)
    print('She says to you that she will stay in the village until you return')
    time.sleep(x)
    print('New arc begins')
    time.sleep(x)
    print('You travel to a forest to find monsters in the forest')
    time.sleep(x)
    print('You have to fight the countless amount of enemies') # change into the final coide
    #function for player dying


    if player_type.upper() == "WATER":
        player = Water(1, player_name, water_abilities, 250, 250, 100, 100)
        abilities = water_abilities
    elif player_type.upper() == "FIRE":
        player = Fire(1, player_name, fire_abilities, 250, 250, 100, 100)
        abilities = fire_abilities
    else:
        print("Invalid Choice, Setting your ability to water")
        player = Water(1, player_name, water_abilities, 250, 250, 100, 100)
        abilities = water_abilities
    
    round_count = 0  
    while True:
        round_count += 1  
        if round_count % 5 == 0:
            boss_defeated = boss_fight(player, enemies_defeated, abilities)
            if boss_defeated:
                break

        enemy_defeated = normal_enemy_fight(player, enemies_defeated, abilities)
        if enemy_defeated:
            round_count += 1
        else:
            break


main()
