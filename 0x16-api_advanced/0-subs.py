#!/usr/bin/python3
"""  """
import requests
import json
def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'})
    if response is None:
        print("0")
        return 0
    js = response.json()
    subs = js.get("data").get("subscribers")
    return subs
