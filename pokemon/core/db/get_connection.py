import asyncpg
import os

async def get_dbConnection():
    try:
        return  await asyncpg.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB"),
            host=os.getenv("HOST"),
            port=os.getenv("CONTAINER_DB_PORT") if os.getenv("HOST")=="PROD" else os.getenv("DB_PORT")
        )
    except Exception as e:
        return None