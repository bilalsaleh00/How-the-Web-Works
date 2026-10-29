import requests


def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        pokemon_name = data["name"]
        height = data["height"]
        weight = data["weight"]

        types = [
            item["type"]["name"]
            for item in data["types"]
        ]

        print(f"--- {pokemon_name} ---")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Types: {', '.join(types)}")
        print()

    elif response.status_code == 404:
        print(f"--- {name} ---")
        print(
            f"Error: Pokémon '{name}' not found "
            f"(Status 404). Check your spelling!"
        )
        print()

    else:
        print(f"--- {name} ---")
        print(
            f"Error: Request failed "
            f"(Status {response.status_code})"
        )
        print()


pokemon_names = [
    "pikachu",
    "charizard",
    "bulbasaur",
    "pikacu",
]


for pokemon in pokemon_names:
    fetch_pokemon(pokemon)