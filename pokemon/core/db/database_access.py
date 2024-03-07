import asyncpg
from pokemon.core.db.get_connection import get_dbConnection


async def get_data_from_database():
    conn = await get_dbConnection()
    if not conn:
        return {"error": "Error Connecting to Database"}
    try:
        # Execute SQL query to fetch all rows from the 'Pokemon' table
        rows = await conn.fetch('''SELECT * FROM "public"."Pokemon"''')

        # Process the fetched data
        pokemon_data = []
        for row in rows:
            pokemon_data.append({
                'name': row['name'],
                'image': row['image'],
                'type': row['type']
            })

        return pokemon_data

    except asyncpg.PostgresError as e:
        print(f"Error fetching data from database: {e}")
        return None

    finally:
        # Close the database connection
        if conn:
            await conn.close() 
