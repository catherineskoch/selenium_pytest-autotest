import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {
   'Content-Type' : 'application/json', 
   'trainer_token' : TOKEN
}
body_data_post_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 7
}

body_data_patch_pokemons = {
    "pokemon_id": '414037',
    "name": "автотестик"
}


body_data_add_pokeball = {
    "pokemon_id": '414037'
}

response_post_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_data_post_pokemon)
print(response_post_pokemon.text)

response_patch_pokemons = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json= body_data_patch_pokemons)
print(response_patch_pokemons.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_data_add_pokeball)
print(response_add_pokeball.text)