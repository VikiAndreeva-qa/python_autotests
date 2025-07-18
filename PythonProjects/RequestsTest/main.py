import requests
URL = "https://api.pokemonbattle.ru/v2"
Token = "user_token"
Header = {"Content-Type": "application/json", "trainer_token": Token}

body_create = {
    "name": "Krotik",
    "photo_id": 22
}
in_pokeball = 1

response_create = requests.post(url=f"{URL}/pokemons", headers= Header, json = body_create)
print(response_create.text)
pokemon_id = response_create.json().get("id")

body_put_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}
response_put_pokemon = requests.put(url=f"{URL}/pokemons", headers=Header, json=body_put_pokemon)
print(response_put_pokemon.text)

body_add_pokeball= {
    "pokemon_id": pokemon_id
}
response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=Header, json=body_add_pokeball)
print(response_add_pokeball.text)

response_get_pokemons =requests.get(url=f'{URL}/pokemons', headers=Header, params= {'in_pokeball': 1})
print(response_get_pokemons.text)

id_enemy = response_get_pokemons.json()['data'][2]['id']

body_battle = {
    "attacking_pokemon": pokemon_id,
    "defending_pokemon": id_enemy
}
 
response_battle = requests.post(url=f'{URL}/battle', headers=Header, json = body_battle)
print(response_battle.text)