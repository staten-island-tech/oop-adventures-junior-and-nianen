my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])

import json
with open('water_abilities.json') as water_abilities_file:
    file_contents = water_abilities_file.read()
print(file_contents["id"])