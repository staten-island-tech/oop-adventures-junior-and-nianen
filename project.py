import fire_abilities
import water_abilities
import random


name = input("What is your name?")
class User:
    def __init__ (self, id, name):
        self.id = id
        self.name = name

class Fire:
    def __init__(self, id, name, moves):
        super().__init__(id,name)
        self.moves
        moves = fire_abilities["name"]

class Water:
    def __init__(self, id, name, moves):
        super().__init__(id,name)
        self.moves
        moves = water_abilities["name"]

ability = input("What ability do you want? WATER/FIRE")
if ability.upper() == "WATER":
    watermove = input("Choose a water move")
    random = random.randint(0,4)
    while random > 0:
        print("Your move was effective")
        
if ability.upper() == "FIRE":
    random = random.randint(0,4)
    while random > 0:
        print("Your move was effective")