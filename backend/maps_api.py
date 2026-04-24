from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_distance(origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": origin,
        "destinations": destination,
        "key": API_KEY,
        "mode": "driving",
        "departure_time": "now",
        "traffic_model": "best_guess"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["rows"][0]["elements"][0]["duration"]["value"]