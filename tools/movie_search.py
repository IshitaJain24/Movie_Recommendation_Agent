import json
import requests

from langchain.tools import Tool
from config import TMDB_API_KEY

GENRE_MAP = {
    "horror": 27,
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "thriller": 53,
    "sci-fi": 878,
}


def search_tmdb_movies(tool_input: str) -> str:
    try:
        data = json.loads(tool_input)

        genre = data["genre"]
        year_range = data["year_range"]
        rating = data["rating"]

    except Exception:
        return "Invalid JSON input."

    genre_id = GENRE_MAP.get(genre.lower())

    if not genre_id:
        return "Unsupported genre."

    start_year = year_range["start"]
    end_year = year_range["end"]

    response = requests.get(
        "https://api.themoviedb.org/3/discover/movie",
        params={
            "api_key": TMDB_API_KEY,
            "with_genres": genre_id,
            "primary_release_date.gte": f"{start_year}-01-01",
            "primary_release_date.lte": f"{end_year}-12-31",
            "certification_country": "US",
            "certification": rating,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1000,
        },
        timeout=10,
    )

    response.raise_for_status()

    movies = response.json().get("results", [])

    if not movies:
        return "No matching movies found."

    best_movie = movies[0]

    return json.dumps(
        {
            "title": best_movie["title"],
            "year": best_movie["release_date"][:4],
            "score": best_movie["vote_average"],
            "overview": best_movie["overview"],
        }
    )


movie_tool = Tool(
    name="search_tmdb_movies",
    func=search_tmdb_movies,
    description="""
Search TMDB and return the highest-ranked movie.

Input Example:

{
  "genre": "horror",
  "year_range": {
      "start": 1990,
      "end": 1999
  },
  "rating": "R"
}
""",
)