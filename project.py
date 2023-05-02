import random

import fire_abilities
import water_abilities

name = input("What is your name?")
class User:
    def __init__ (self, id, name):
        self.id = id
        self.name = name

class Fire:
    def __init__(self, id, name, moves):
        super().__init__(id,name)
        self.moves = moves
        moves = fire_abilities["name"]

class Water:
    def __init__(self, id, name, moves):
        super().__init__(id,name)
        self.moves = moves
        moves = water_abilities["name"]
class Enemie: 
    def __init__(self, id, name, health):
        super().__init__(id,name)
        self.health = health
class Boss:
     def __init__(self, id, name, health):
        super().__init__(id,name)
        self.health = health

random1 = random.randint(0,4)
random = random.randint(0,4)

ability = input("What ability do you want? WATER/FIRE")



if ability.upper() == "WATER":
    watermove = input("Choose a water move" )
    if random > 0:
        print("Your move was effective")
    elif random == 0:
        print("Your move was ineffective")

        
if ability.upper() == "FIRE":
    if random > 0:
        print("Your move was effective")
    elif random == 0:
        print("Your move was ineffective")
    
        



