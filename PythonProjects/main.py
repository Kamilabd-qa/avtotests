import requests
add_pokemon_responce = requests.post('https://pokemonbattle.me:9104/pokemons',  headers = {'Content-Type' : 'application/json', "trainer_token": "27c578d309102228f5e85a5b169af19f"},
json = {
    "name": "Будьбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})
print(add_pokemon_responce.text)

add_pokemon_responce = requests.put('https://pokemonbattle.me:9104/pokemons', 
headers = {'Content-Type' : 'application/json', "trainer_token": "27c578d309102228f5e85a5b169af19f"},
json = {
    "pokemon_id": "6466",
    "name": "Пикачу"
})
print(add_pokemon_responce.text)

add_pokemon_responce = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
headers = {'Content-Type' : 'application/json', "trainer_token": "27c578d309102228f5e85a5b169af19f"},
json = {
    "pokemon_id": "6466",
})
print(add_pokemon_responce.text)
