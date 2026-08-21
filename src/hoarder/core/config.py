from dotenv import load_dotenv
from os import getenv

load_dotenv()

DEFAULT_ADMIN_PASSWORD = "risky-default"
DEFAULT_DATABASE_URL = "postgresql+psycopg://hoarder:hoarder@localhost:5432/hoarder"

DATABASE_URL = getenv("DATABASE_URL", DEFAULT_DATABASE_URL)

DATA_FOLDER = getenv("DATA_FOLDER", "resources")
CORS_ALLOWED = getenv("CORS_ALLOWED", "localhost")
ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", DEFAULT_ADMIN_PASSWORD)
