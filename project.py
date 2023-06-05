
import json
import random

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)

with open("fire_abilities.json", encoding="utf8") as fire_ability_file:
    fire_abilities = json.load(fire_ability_file)



damage_dealt = []
enemies_defeated = 0
bosses_defeated = 0


total_damage_dealt = sum(damage_dealt)



class User:
    def __init__(self, id, name, health, max_health, energy, max_energy):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health
        self.energy = energy
        self.max_energy = max_energy


class Fire(User):
    def __init__(self, id, name, moves, health, max_health, energy, max_energy):
        super().__init__(id, name, health, max_health, energy, max_energy)
        self.moves = moves


class Water(User):
    def __init__(self, id, name, moves, health, max_health, energy, max_energy):
        super().__init__(id, name, health, max_health, energy, max_energy)
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


attackchance = random.randint(0, 100)

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

    print(f"{player.name} used {move['name']['english']} Current energy: {player.energy}")
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated")
    


def take_damage(player, enemy, move):
    hit_chance = random.random()
    if hit_chance <= 0.3:
        print("Enemy missed")
    else:
        damage = enemy.damage
        player.health -= damage
        print(f"{player.name} took {damage} damage")

    

def normal_enemy_fight(player, enemies_defeated, abilities):
    randomenemy = random.randint(100, 200)
    enemy = Enemy(0, "Normal Enemy", randomenemy, randomenemy, random.randint(10, 100))
    print(f"You have encountered a normal enemy with {enemy.health} health")
    while enemy.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, enemy, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle, Icecle Snipe, Water Slash, Water Blaze, Hail Storm): ")
                for abilities in water_abilities:
                    if watermove == abilities["name"]["english"]:
                        defeated = deal_damage(player, enemy, abilities)
                        if defeated:
                            enemies_defeated += 1
                            return True
                        take_damage(player, enemy, abilities)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}, Bosses defeated: {bosses_defeated}")
                            return False
            
        elif isinstance(player, Fire):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, enemy, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Lava Cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath, Fire Blast): ")
                for abilities in fire_abilities:
                    if firemove == abilities["name"]["english"]:
                        defeated = deal_damage(player, enemy, abilities)
                        if defeated:
                            enemies_defeated += 1
                            return True
                        take_damage(player, enemy, abilities)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}, Bosses defeated: {bosses_defeated}")
                            return False

def boss_fight(player, enemies_defeated, abilities):
    global bosses_defeated
    random_boss = random.randint(1000, 3000)
    boss = Boss(1, "Boss", random_boss, random_boss, random.randint(50, 250))
    print(f"You have encountered a boss with {boss.health} health")
    while boss.health > 0:
        if isinstance(player, Water):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, boss, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle, Icecle Snipe, Water Slash, Water Blaze, Hail Storm): ")
                for abilities in water_abilities:
                    if watermove == abilities["name"]["english"]:
                        defeated = deal_damage(player, boss, abilities)
                        if defeated:
                            bosses_defeated += 1
                            return True
                        take_damage(player, boss, abilities)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}, Bosses defeated: {bosses_defeated}")
                            return False

            
        elif isinstance(player, Fire):
            attackordefend = input("Do you want to defend or attack: ")
            if attackordefend.upper() == "DEFEND":
                defend_success = random.random()
                if defend_success > 0.3:
                    print("You successfully defended against the enemy")
                    add_energy(player)
                else:
                    print("You unsuccessfully defended against the enemy")
                    take_damage(player, boss, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Fire Ball, Lava cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath): ")
                for abilities in fire_abilities:
                    if firemove == abilities["name"]["english"]:
                        defeated = deal_damage(player, boss, abilities)
                        if defeated:
                            bosses_defeated += 1
                            return True
                        take_damage(player, boss, abilities)
                        if player.health <= 0:
                            print(f"Name: {player.name}, Enemies defeated: {enemies_defeated}, Bosses defeated: {bosses_defeated}")
                            return False



def add_energy(player):
    player.energy += 30
    if player.energy > player.max_energy:
        player.energy = player.max_energy
    print(f"{player.name} regenerated 30 energy. Current energy: {player.energy}")


def main():
    player_name = input("Enter your name: ")
    player_type = input("Choose an ability type (Water, Fire): ")
    if player_type.upper() == "WATER":
        player = Water(1, player_name, water_abilities, 250, 250, 100, 100)
        abilities = water_abilities
    elif player_type.upper() == "FIRE":
        player = Fire(1, player_name, fire_abilities, 250, 250, 100, 100)
        abilities = fire_abilities
    round_count = 0
    while True:
        enemy_defeated = normal_enemy_fight(player, enemies_defeated, abilities)
        if enemy_defeated:
            round_count += 1
            if round_count % 5 == 0:
                bossfight = boss_fight(player, bosses_defeated)
                if bossfight:
                    print(f"Total damage dealt: {total_damage_dealt}, Enemies defeated: {enemies_defeated}, Bosses defeated: {bosses_defeated}")
                    break
        else:
            break
    
    

main()