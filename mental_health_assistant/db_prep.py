from tqdm.auto import tqdm
from dotenv import load_dotenv

from mental_health_assistant.db import init_db

load_dotenv()


if __name__ == "__main__":
    print("Initializing database...")
    init_db()
