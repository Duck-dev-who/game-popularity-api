from fastapi import FastAPI, Query
import steam_api
import utils

app = FastAPI(title="Game Popularity API")


@app.get("/")
def home():
    return {"message": "Game Popularity API is running!"}

@app.get("/trending")
def trending():
    data = steam_api.get_most_played()
    return data


@app.get("/players/{appid}")
def players(appid: int):
    data = steam_api.get_current_players(appid)
    return data

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    """Search trending games by name"""
    data = steam_api.get_most_played()["response"]["ranks"]
    results = utils.search_games(data, query)
    for game in results:
        game["hotness"] = utils.calculate_hotness(game)
    return results