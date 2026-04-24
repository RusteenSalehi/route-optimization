from backend.maps_api import get_distance, API_KEY

time = get_distance("Time Square, New York", "Central Park, New York")

print(f"Travel time is {time / 60:.2f} minutes")