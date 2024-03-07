import aiohttp
import httpx

from typing import Union

from fastapi import FastAPI, HTTPException
from pokemon.core.accessor.handler import fetch_pokemon

from pokemon.core.db.database_access import get_data_from_database

app = FastAPI()


@app.get("/api/v1/pokemons")
async def get_pokemon_info():
    '''
        route handler for pokemon
    '''
    async with aiohttp.ClientSession() as session:
        tempRecords = await get_data_from_database()
        return tempRecords if len(tempRecords) else await fetch_pokemon(session)
