#!/usr/bin/python3

import requests

def get_nairobi_subscriber_count():
    url = "https://www.reddit.com/r/nairobi/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscriber_count = data["data"]["active_user_count"]
        return subscriber_count
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
subscriber_count = get_nairobi_subscriber_count()
if subscriber_count is not None:
    print("Nairobi subreddit has", subscriber_count, "subscribers.")

