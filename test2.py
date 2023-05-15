import json
with open('water_abilities.json') as water_abilities_file:
    file_contents = water_abilities_file.read()

print ("Name:" + file_contents[150:200])

