import json
import random

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)

with open("fire_abilities.json", encoding="utf8") as fire_ability_file:
    fire_abilities = json.load(fire_ability_file)

normal_enemy_health = 100
normal_enemy_max_health = 100
damage_dealt = []



total_damage_dealt = sum(damage_dealt)

class User:
    def __init__(self, id, name, health, max_health):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health

class Fire(User):
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id, name, health, max_health)
        self.moves = moves

class Water(User):
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id, name, health, max_health)
        self.moves = moves

class Enemy: 
    def __init__(self, id, name, health, max_health, damage):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health
        self.damage = damage


class Boss:
    def __init__(self, id, name, health, max_health, damage):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health
        self.damage = damage

    def __repr__(self): 
        return "max_health:% s and the health:% s" % (self.max_health, self.health) 

def deal_damage(player, enemy, move):
    damage = move["base"]["Attack"]
    enemy.health -= damage
    print(f"{enemy.name} took {damage} damage")
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated")
        damage_dealt.append(damage)
        return True
    return False
def take_damage(player, enemy, move):
    damage = enemy.damage
    player.health -= damage
    print(f"{player.name} took {damage} damage")
    if player.health <= 0:
        print(f"{player.name} has been defeated")
        return True
    return False


def normal_enemy_fight(player):
    enemy = Enemy(0, "Normal Enemy", normal_enemy_health, normal_enemy_max_health, 50)
    print(f"You have encountered a normal enemy with {enemy.health} health")
    while enemy.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack")
            if attackordefend == "DEFEND".upper ():
                print("You defended against the enemy")
            elif attackordefend == "ATTACK".upper():
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle): ")
                for abilities in water_abilities:
                    if watermove == abilities["name"]["english"]:
                        defeated = deal_damage(player, enemy, abilities)
                        if defeated:
                            print("You have defeated the normal enemy")
                        lost = take_damage(player, enemy, abilities)
                        if lost:
                            print("You lost")
                          


           
                
            
                        
                        
        elif isinstance(player, Fire):
            attackordefend = input("Do you want to defend or attack")
            if attackordefend == "DEFEND".upper ():
                print("You defended against the enemy")
            elif attackordefend == "ATTACK".upper():
                firemove = input("Choose a fire move (Fire Fist, Fire Ball, Lava cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath): ")
                for abilities in fire_abilities:
                    if firemove == abilities["name"]["english"]:
                        defeated = deal_damage(player, enemy, abilities)
                        if defeated:
                            print("You have defeated the normal enemy")
                        lost = take_damage(player, enemy, abilities)
                        if lost:
                            print("You lost")
                            
    
                        return True
                    break

def boss_fight(player):
    random_boss = random.randint(500, 1000)
    boss = Boss(1, "Boss", random_boss, random_boss, 50)
    print(f"You have encountered a boss with {boss.health} health")
    while boss.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack")
            if attackordefend == "DEFEND".upper ():
                print("You defended against the enemy")
            elif attackordefend == "ATTACK".upper():
                watermove = input("Choose a water move (Ice Breath): ")
                for abilities in water_abilities:
                    if watermove == abilities["name"]["english"]:
                        defeated = deal_damage(player, boss, abilities)
                        if defeated:
                            print("You have defeated the boss")
                        lost = take_damage(player, boss, abilities)
                        if lost:
                            print("You lost")
                        return True
                    break
        elif isinstance(player, Fire):
            while boss.health > 0:
                attackordefend = input("Do you want to defend or attack")
                if attackordefend == "DEFEND".upper ():
                    print("You defended against the enemy")
                elif attackordefend == "ATTACK".upper():
                    firemove = input("Choose a fire move (Fire Fist, Fire Ball): ")
                    for abilities in fire_abilities:
                        if firemove == abilities["name"]["english"]:
                            defeated = deal_damage(player, boss, abilities)
                            if defeated:
                                print("You have defeated the boss")
                            lost = take_damage(player, boss, abilities)
                            if lost:
                                print("You lost")
                            return True
                        break

name = input("What is your name?")

ability = input("What ability do you want? WATER/FIRE")

if ability.upper() == "WATER":
    player = Water(0, name, [], 500, 500)
elif ability.upper() == "FIRE":
    player = Fire(0, name, [], 500, 500)

round_count = 1
while True:
    if round_count % 5 == 0:
        boss_defeated = boss_fight(player)
        if boss_defeated:
            break
    else:
        enemy_defeated = normal_enemy_fight(player)
        if enemy_defeated:
            round_count += 1
        else:
            break


def __repr__(self): 
    return "max_health:% s and the health:% s" % (self.max_health, self.health) 
    
    



        
