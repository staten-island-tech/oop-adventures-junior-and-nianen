import json
import random

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)

with open("fire_abilities.json", encoding="utf8") as fire_ability_file:
    fire_abilities = json.load(fire_ability_file)


enemies_defeated = 0


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

    print(f"{player.name} used {move['name']['english']}")
    print(f"Current energy: {player.energy}")
    if enemy.health <= 0:
        print(f"You defeated the enemy")


def take_damage(player, enemy, move):
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
                for move in abilities:
                    if watermove == move["name"]["english"]:
                        deal_damage(player, enemy, move)
                        take_damage(player, enemy, move)
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
                    take_damage(player, enemy, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Lava Cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath, Fire Blast): ")
                for move in abilities:
                    if firemove == move["name"]["english"]:
                        deal_damage(player, enemy, move)
                        take_damage(player, enemy, move)
                        break


def boss_fight(player, enemies_defeated, abilities):
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
                    take_damage(player, boss, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle, Icecle Snipe, Water Slash, Water Blaze, Hail Storm): ")
                for ability in abilities:
                    if watermove == ability["name"]["english"]:
                        deal_damage(player, boss, ability)
                        take_damage(player, boss, ability)
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
                    take_damage(player, boss, abilities)
            elif attackordefend.upper() == "ATTACK":
                if player.energy <= 0:
                    print("You don't have enough energy to use a move")
                    continue
                firemove = input("Choose a fire move (Fire Fist, Fire Ball, Lava cannon, Lava Rise, Magma Shot, Fire Blaze, Fire Phoneix, Fire Breath): ")
                for ability in abilities:
                    if firemove == ability["name"]["english"]:
                        deal_damage(player, boss, ability)
                        take_damage(player, boss, ability)
                        break


def add_energy(player):
    player.energy += 10
    if player.energy > player.max_energy:
        player.energy = player.max_energy
    print(f"{player.name} gained 10 energy")


def main():
    player_name = input("Enter your name: ")
    player_class = input("Choose your class (Water/Fire): ")
    if player_class.upper() == "WATER":
        player = Water(1, player_name, water_abilities, 200, 200, 100, 100)
    elif player_class.upper() == "FIRE":
        player = Fire(2, player_name, fire_abilities, 200, 200, 100, 100)
    else:
        print("Invalid class. Defaulting to Water.")
        player = Water(1, player_name, water_abilities, 200, 200, 100, 100)

   

    enemies_defeated = 0
    bosses_defeated = 0

    while True:
        enemy_or_boss = input("Do you want to encounter a normal enemy or a boss? (Enemy/Boss): ")
        if enemy_or_boss.upper() == "ENEMY":
            enemy = normal_enemy_fight(player, enemies_defeated, player.moves)
            if enemy is not None:
                enemies_defeated += 1
                
        elif enemy_or_boss.upper() == "BOSS":
            boss = boss_fight(player, enemies_defeated, player.moves)
            if boss is not None:
                bosses_defeated += 1
        else:
            print("Invalid choice")

        if player.health <= 0:
            print(f"{player.name} was defeated.")
            print(f"Enemies defeated:{enemies_defeated}")
            print(f"Bosses defeated:{bosses_defeated}")
            break

        play_again = input("Do you want to play again? (Yes/No): ")
        if play_again.upper() == "NO":
            break



main()
