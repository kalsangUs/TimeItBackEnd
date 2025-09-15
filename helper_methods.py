import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
response = requests.get(url)
genres = response.json().get("genres", [])
for i in genres:
    print(f"{i['id']}: {i['name']}")
