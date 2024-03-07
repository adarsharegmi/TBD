from pokemon.core.db.get_connection import get_dbConnection

async def store_data_in_database(pokemon_data: list[dict]):
    # Build the database connection
    conn = await get_dbConnection()
    if not conn:
        return {"error": "Error Connecting to Database"}


    try:

        # Execute Sql to insert the data
        await conn.executemany('''
            INSERT INTO "public"."Pokemon" (name, image, type)
            VALUES ($1, $2, $3)
        ''', pokemon_data)  

    finally:
        if conn:
            await conn.close()