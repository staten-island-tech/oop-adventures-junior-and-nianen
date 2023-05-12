import json
import random

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)

with open("fire_abilities.json", encoding="utf8") as fire_ability_file:
    fire_abilities = json.load(fire_ability_file)

normal_enemy_health = 100
normal_enemy_max_health = 100
boss_health = []
damage_dealt_list = []
damage_taken_list = []

total_damage_taken = sum(damage_taken_list)
total_damage_dealt = sum(damage_dealt_list)

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
    def __init__(self, id, name, health, max_health):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health

class Boss:
    def __init__(self, id, name, health, max_health):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health

    def __repr__(self): 
        return "max_health:% s and the health:% s" % (self.max_health, self.health) 

def deal_damage(attacker, enemy, move):
    damage = move["base"]["Attack"]
    enemy.health -= damage
    print(f"{enemy.name} took {damage} damage")
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated")
        return True
    return False

def stats_print():
    print(f"Total damage taken: {total_damage_dealt}")
    print(f"Total damage dealt: {total_damage_taken}")

def normal_enemy_fight(player):
    enemy = Enemy(0, "Normal Enemy", normal_enemy_health, normal_enemy_max_health)
    print(f"You have encountered a {enemy.name} with {enemy.health} health!")
    while enemy.health > 0:
        if isinstance(player, Water):
            watermove = input("Choose a water move (Ice Breath): ")
            for abilities in water_abilities:
                if watermove == abilities["name"]["english"]:
                    defeated = deal_damage(player, enemy, abilities)
                    if defeated:
                        print(f"You have defeated the {enemy.name}!")
                        damage_dealt_list.append(player.health)
                        damage_taken_list.append(enemy.health)
                        stats_print()
                        return True
                    break
        elif isinstance(player, Fire):
            firemove = input("Choose a fire move (Fire Fist, Fire Ball): ")
            for abilities in fire_abilities:
                if firemove == abilities["name"]["english"]:
                    defeated = deal_damage(player, enemy, abilities)
                    if defeated:
                        print(f"You have defeated the {enemy.name}!")
                        damage_dealt_list.append(player.health)
                        damage_taken_list.append(enemy.health)
                        stats_print()
                        return True
                    break

def boss_fight(player):
    random_boss = random.randint(300, 500)
    boss = Boss(1, "Boss", random_boss, random_boss)
    print(f"You have encountered a {boss.name} with {boss.health} health!")
    while boss.health > 0:
        if isinstance(player, Water):
            watermove = input("Choose a water move (Ice Breath): ")
            for abilities in water_abilities:
                if watermove == abilities["name"]["english"]:
                    defeated = deal_damage(player, boss, abilities)
                    if defeated:
                        print(f"You have defeated the {boss.name}!")
                        damage_dealt_list.append(player.health)
                        damage_taken_list.append(boss.health)
                        stats_print()
                        return True
                    break
        elif isinstance(player, Fire):
            firemove = input("Choose a fire move (Fire Fist, Fire Ball): ")
            for abilities in fire_abilities:
                if firemove == abilities["name"]["english"]:
                    defeated = deal_damage(player, boss, abilities)
                    if defeated:
                        print(f"You have defeated the {boss.name}!")
                        damage_dealt_list.append(player.health)
                        damage_taken_list.append(boss.health)
                        stats_print()
                        return True
                    break

name = input("What is your name?")

ability = input("What ability do you want? WATER/FIRE")

if ability.upper() == "WATER":
    player = Water(0, name, [], 100, 100)
elif ability.upper() == "FIRE":
    player = Fire(0, name, [], 100, 100)

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
