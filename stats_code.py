import random
random_boss = random.randint(300,500)
boss_health = []
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
            return "max_health:% s and the health:% s" % (self.max_health, self.health) 
    
    
Health_of_Boss = Boss(random_boss,random_boss,random_boss,random_boss)

print(Health_of_Boss)
        
