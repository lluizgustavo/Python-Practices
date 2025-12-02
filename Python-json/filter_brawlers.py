import json

with open("list_brawlers.json", 'r') as file:
    brawlers = json.load(file)["brawlers"]

controller_brawlers = []

for brawler in brawlers:
    if "Controller" in brawler["type"]:
        controller_brawlers.append(brawler)

with open("controller_brawlers.json", 'w', encoding='utf-8') as file:
    new_file = json.dumps(controller_brawlers)
    file.write(new_file)
