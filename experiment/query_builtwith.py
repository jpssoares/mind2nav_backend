import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def make_get_request(url, params):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Failed to make GET request. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    # Get API key from environment variable
    api_key = os.getenv("BUILTWITH_API_KEY")
    if api_key is None:
        print("Error: API_KEY is not set in the .env file.")
        return

    url = "https://api.builtwith.com/free1/api.json"
    lookup = "builtwith.com"
    params = {"KEY": api_key, "LOOKUP": lookup}
    
    data = make_get_request(url, params)
    if data:
        print(data)  # Do something with the response data
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
