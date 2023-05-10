import random
random_boss = random.randint(300,500)
damage_dealt_list = []
damage_taken_list = []

total_damage_taken = sum(damage_taken_list)
total_damage_dealt = sum(damage_dealt_list)

def stats_print():
    print(f'Damage taken was'[total_damage_dealt])
    print(f'Damage dealth is'[total_damage_taken])


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
            return "Test max_health:% s health:% s" % (self.max_health, self.health) 

        boss_health = Boss
        
