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
        
            
class Water:
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id,name, health, max_health)
        self.moves = moves
    


ability = input("What ability do you want? WATER/FIRE")



if ability.upper() == "WATER":
    watermove = input("Choose a water move" )
    for abilities in data1:
        if watermove == abilities["name"]:
            print("d")

if ability.upper() == "FIRE":
    firemove = input("Choose a fire move" )
    for abilities in data:
        if firemove in abilities["name"]:
            if firemove == abilities["name"]["english"]["Fire Ball"]:
                print("efwfweoi")
            elif firemove == "Fire Ball":
                print("efwrgeegr")
            