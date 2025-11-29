import json
from agents import function_tool

USER_PROFILE_FILE = "user_profile.json"

@function_tool
def read_user_profile():
    """Reads the user profile from the JSON file."""
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@function_tool
def update_user_profile(key: str, value: str):
    """Updates a specific key in the user profile and saves it."""
    profile = read_user_profile()
    profile[key] = value
    with open(USER_PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)
    return {"status": "success", "key": key, "value": value}
