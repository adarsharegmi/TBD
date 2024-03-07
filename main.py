import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        "pokemon:app",
        host=os.getenv("CONTAINER_HOST", "0.0.0.0") if os.getenv("ENVIRONMENT")=="PROD" else  os.getenv("HOST", "127.0.0.1"),
        port=os.getenv("PORT",8000),
    )