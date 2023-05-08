import json
import random

waterability = open("water_abilities.json", encoding="utf8")
data = json.load(waterability)

fireability = open("fire_abilities.json", encoding="utf8")
data1 = json.load(fireability)

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
        moves = data1["name"]

class Water:
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id,name, health, max_health)
        self.moves = moves
        moves = data["name"]
       
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
    for abilities in data:
        print(abilities["name"]["english"])
    watermove = input("Choose a water move" )
    for abilities in data:
        if watermove in abilities["name"]["english"]:
            if random > 0:
                print("Your move was effective")
            elif random == 0:
                print("Your move was ineffective")

        
if ability.upper() == "FIRE":
    for abilities in data1:
        print(abilities["name"]["english"])
    firemove = input("Choose a fire move" )
    for abilities in data1:
        if firemove in abilities["name"]["english"]:
            if random > 0:
                print("Your move was effective")
            elif random == 0:
                    print("Your move was ineffective")
    
        



