import json
water = open("./water_abilities.json", encoding="utf8")
data = json.load(water)
print (water[1]["name"])