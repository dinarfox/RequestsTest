import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '54e32106ee2cea8ada47d2e460b9fc05'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "dinarosben@yandex.ru",
    "password": "1231423"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

response_name = requests.patch(url = f'{URL}/pokemons', headers= HEADER, json= body_name)
print(response_name.text)

body_pokeball ={
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)
