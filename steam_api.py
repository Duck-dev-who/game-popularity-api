import requests

BASE = "https://api.steampowered.com"

def get_most_played():
    url = f"{BASE}/ISteamChartsService/GetMostPlayedGames/v1/"
    r = requests.get(url)
    return r.json()

def get_current_players(appid: int):
    url = f"{BASE}/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={appid}"
    r = requests.get(url)
    return r.json()
