#!/usr/bin/python3
"""
returns top ten hot posts
"""
import requests
import json

def top_ten(subreddit):
    """ """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'})
    js = response.json()
    l = js.get("data").get("children")
    for i in l:
        print(i.get("data").get("title").encode())
