#!/usr/bin/python3
"""  """
import requests
import json

def number_of_subscribers(subreddit):
    """returns number of subscribers from reddit api"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'})
    js = response.json()
    subs = js.get("data", {}).get("subscribers", 0)
    return subs
