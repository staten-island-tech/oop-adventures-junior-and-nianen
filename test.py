import json 

with open("water_abilities.json", encoding="utf8") as water_ability_file:
    water_abilities = json.load(water_ability_file)
empty_list = []
damage_dealty = (empty_list)
watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle): ")
for abilities in water_abilities:
    if watermove == abilities["name"]["english"]:
        print(abilities['base']['Attack']) and empty_list.append(abilities.copy(['base']['Attack']))

print('You have encountered another enemy')
watermove = input("Choose a water move (Ice Breath, Tsunami, Icecle): ")
for abilities in water_abilities:
    if watermove == abilities["name"]["english"]:
        print(abilities['base']['Attack']) and empty_list.append(abilities.copy(['base']['Attack']))

print(f'You Dealt A total Damage of'[damage_dealty])