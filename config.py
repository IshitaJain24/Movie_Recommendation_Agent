import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing.")

if not TMDB_API_KEY:
    raise ValueError("TMDB_API_KEY is missing.")