from dotenv import load_dotenv
from os import getenv

load_dotenv()

DEFAULT_ADMIN_PASSWORD = "risky-default"

CORS_ALLOWED = getenv("CORS_ALLOWED", "localhost")
ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", DEFAULT_ADMIN_PASSWORD)
