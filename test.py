import json 
with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)
empty_list = []
watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle): ")

def appening_function ():
    for abilities in water_abilities:
        if watermove == abilities["name"]["english"]:
            print(abilities['base']['Attack'])
            for abilities in water_abilities:
                if watermove == abilities["name"]["english"]:
                    empty_list.append(abilities['base']['Attack'])
