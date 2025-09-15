# movies.py
from fastapi import APIRouter, Query
from dotenv import load_dotenv
import os
import requests


load_dotenv()

api_key = os.getenv("API_KEY")
url = "https://api.themoviedb.org/3/discover/movie"

general_params = {
    "api_key": api_key,
    "language": "en-US",
    "sort_by": "popularity.desc",
    "include_adult": "false"
}

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/{movie_runtime}")
async def get_movies(
    movie_runtime: int,
    page: int = 1,
    genres: str = Query(None, description="Comma-separated genre IDs, e.g., '28,12'"),
    release_year: str = Query(None, description="Filter by primary release year, e.g., 2023")
):
    """
    Get movies under `movie_runtime` minutes.
    Optionally filter by genre IDs and release year.
    Adult movies are excluded by default.
    Only returns top 10% by vote_average in the page.
    """
    params = general_params.copy()
    params["with_runtime.lte"] = movie_runtime
    params["page"] = page

    if genres:
        params["with_genres"] = genres

    if release_year:
        params["primary_release_year"] = release_year

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return {"error": "Failed to fetch movies", "status_code": response.status_code}

    return response.json().get("results", [])
    

    
