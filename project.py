import json
import random

fire_abilities = open("fire_abilities.json", encoding="utf8")
water_abilities = open("water_abilities.json", encoding="utf8")
data = json.load(fire_abilities)
name = input("What is your name?")
class User:
    def __init__ (self, id, name, health, max_health):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health

class Fire:
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id, name, health, max_health)
        self.moves = moves
        moves = water_abilities["name"]

class Water:
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id,name, health, max_health)
        self.moves = moves
        moves = fire_abilities["name"]
       
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



random = random.randint(0,4)

ability = input("What ability do you want? WATER/FIRE")



if ability.upper() == "WATER":
    watermove = input("Choose a water move" )
    if watermove == water_abilities["name"]:
        if random > 0:
            print("Your move was effective")
        elif random == 0:
            print("Your move was ineffective")

        
if ability.upper() == "FIRE":
    firemove = input("Choose a fire move" )
    for abilities in data:
        if firemove in abilities["name"]:
            if random > 0:
                print("Your move was effective")
            elif random == 0:
                    print("Your move was ineffective")
    
        



