
async def fetch_pokemon_info(session, pokemon_record: dict) -> tuple:
    async with session.get(pokemon_record['url']) as pokemon_info_response:
        pokemon_info = await pokemon_info_response.json()

        pokemon_info_data = pokemon_record['name'], pokemon_info['sprites']['front_default'],pokemon_info['species']['name']

    return pokemon_info_data
