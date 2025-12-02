import json

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

grass_type_pokemons = []
for pokemon in pokemons:
    if "Grass" in pokemon["type"]:
        grass_type_pokemons.append(pokemon)



with open("grass_pokemons.json", 'w') as file:
    new_file = json.dumps(
        grass_type_pokemons
    )

    file.write(new_file)

