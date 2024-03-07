from pokemon.core.accessor.data_access import fetch_pokemon_info
from pokemon.core.db.database_store import store_data_in_database


async def fetch_pokemon(session) :
    base_url = "https://pokeapi.co/api/v2/"
    async with session.get(base_url + 'pokemon/?limit=400') as response:
        data = await response.json()

    pokemon_info_data = []
    for pokemon_record in data['results']:
        pokemon_info_data.append(await fetch_pokemon_info(session, pokemon_record))

    await store_data_in_database(pokemon_info_data)

    return [{"name":data[0], "image":data[1], "type":data[2]}for data in pokemon_info_data]
